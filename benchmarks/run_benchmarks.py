"""Generate a reproducible algorithm benchmark leaderboard.

The runner uses fixed seeds and bundled open datasets. Results are written as JSON
and Markdown so they can be compared by humans and consumed by CI.
"""

from __future__ import annotations

import argparse
import json
import platform
import random
import statistics
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable

import networkx as nx
from sklearn.datasets import load_breast_cancer, load_iris, load_wine

from general_reference import (
    FenwickTree,
    breadth_first_path,
    dijkstra_shortest_path,
    edit_distance,
    kmp_search,
    kruskal_minimum_spanning_forest,
    longest_increasing_subsequence,
    longest_increasing_subsequence_dp,
    merge_sort,
    online_mean_variance,
    z_function,
)


@dataclass(frozen=True)
class Result:
    rank: int
    benchmark: str
    dataset: str
    input_size: str
    median_ms: float
    relative_speed: float


def measure(function: Callable[[], object], repeats: int) -> float:
    """Return median wall-clock runtime in milliseconds after one warm-up."""
    function()
    samples = []
    for _ in range(repeats):
        started = time.perf_counter_ns()
        function()
        samples.append((time.perf_counter_ns() - started) / 1_000_000)
    return statistics.median(samples)


def build_cases() -> list[tuple[str, str, str, Callable[[], object]]]:
    iris = load_iris().data[:, 0].tolist()
    wine = load_wine().data[:, 0].tolist()
    cancer = load_breast_cancer().data[:, 0].tolist()
    graph = nx.karate_club_graph()
    unweighted = {node: list(graph.neighbors(node)) for node in graph.nodes}
    weighted = {
        node: [(neighbour, float(data.get("weight", 1.0))) for neighbour, data in graph[node].items()]
        for node in graph.nodes
    }
    edges = [
        (float(data.get("weight", 1.0)), first, second)
        for first, second, data in graph.edges(data=True)
    ]
    rng = random.Random(20260717)
    random_values = [rng.random() for _ in range(5_000)]
    text = "|".join(load_iris().target_names) * 2_000
    pattern = "versicolor"

    return [
        ("Merge sort", "Seeded synthetic", "5,000 values", lambda: merge_sort(random_values)),
        ("LIS dynamic programming", "Wine", "120 rows", lambda: longest_increasing_subsequence_dp(wine[:120])),
        ("LIS patience sorting", "Wine", "178 rows", lambda: longest_increasing_subsequence(wine)),
        ("Online mean/variance", "Breast Cancer Wisconsin", "569 rows", lambda: online_mean_variance(cancer)),
        ("KMP search", "Iris class labels", f"{len(text):,} chars", lambda: kmp_search(text, pattern)),
        ("Z-function", "Iris class labels", f"{len(text):,} chars", lambda: z_function(text)),
        ("Edit distance", "Iris/Wine labels", "3 label pairs", lambda: [edit_distance(a, b) for a, b in zip(load_iris().target_names, load_wine().target_names)]),
        ("Fenwick build and query", "Iris", "150 rows", lambda: FenwickTree(iris).range_sum(0, len(iris))),
        ("Breadth-first path", "Karate Club", "34 nodes / 78 edges", lambda: breadth_first_path(unweighted, 0, 33)),
        ("Dijkstra path", "Karate Club", "34 nodes / 78 edges", lambda: dijkstra_shortest_path(weighted, 0, 33)),
        ("Kruskal spanning tree", "Karate Club", "34 nodes / 78 edges", lambda: kruskal_minimum_spanning_forest(graph.nodes, edges)),
    ]


def run(repeats: int) -> list[Result]:
    measured = [
        (name, dataset, size, measure(function, repeats))
        for name, dataset, size, function in build_cases()
    ]
    fastest = min(runtime for *_, runtime in measured)
    ordered = sorted(measured, key=lambda item: item[3])
    return [
        Result(rank, name, dataset, size, round(runtime, 4), round(runtime / fastest, 2))
        for rank, (name, dataset, size, runtime) in enumerate(ordered, start=1)
    ]


def markdown(results: list[Result], repeats: int) -> str:
    rows = [
        "# Benchmark leaderboard",
        "",
        "Lower median runtime is better. Results use fixed inputs, one warm-up, and "
        f"the median of {repeats} measured runs.",
        "",
        f"**Environment:** Python {platform.python_version()} · {platform.system()} {platform.machine()}",
        "",
        "| Rank | Benchmark | Dataset | Input | Median (ms) | Relative to fastest |",
        "|---:|---|---|---:|---:|---:|",
    ]
    rows.extend(
        f"| {r.rank} | {r.benchmark} | {r.dataset} | {r.input_size} | {r.median_ms:.4f} | {r.relative_speed:.2f}× |"
        for r in results
    )
    rows += [
        "",
        "## Interpretation",
        "",
        "These timings compare different workloads and therefore rank execution cost, not algorithmic quality. "
        "For like-for-like comparison, the most important result is the traditional O(n²) LIS versus the "
        "O(n log n) patience-sorting implementation. Runtimes vary by machine; use the JSON artifact for regression tracking.",
        "",
        "## Reproduce",
        "",
        "```bash",
        "python benchmarks/run_benchmarks.py --repeats 15",
        "```",
    ]
    return "\n".join(rows) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repeats", type=int, default=15)
    parser.add_argument("--markdown", type=Path, default=Path("benchmark-results/leaderboard.md"))
    parser.add_argument("--json", type=Path, default=Path("benchmark-results/results.json"))
    args = parser.parse_args()
    if args.repeats < 3:
        raise SystemExit("--repeats must be at least 3")

    results = run(args.repeats)
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.write_text(markdown(results, args.repeats), encoding="utf-8")
    args.json.write_text(
        json.dumps({"environment": {"python": platform.python_version(), "platform": platform.platform()}, "results": [asdict(result) for result in results]}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(markdown(results, args.repeats))


if __name__ == "__main__":
    main()
