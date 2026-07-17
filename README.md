# General Reference Algorithms

[![Quality](https://github.com/sauravsingla/General/actions/workflows/quality.yml/badge.svg)](https://github.com/sauravsingla/General/actions/workflows/quality.yml)
[![Benchmarks](https://github.com/sauravsingla/General/actions/workflows/benchmarks.yml/badge.svg)](https://github.com/sauravsingla/General/actions/workflows/benchmarks.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A practical, tested, and reproducible Python reference for algorithms, data structures, graph methods, string processing, dynamic programming, and streaming statistics.

The repository combines **transparent teaching baselines**, **optimised implementations**, **open-dataset validation**, and a **reproducible benchmark leaderboard**. It is designed for students, interview preparation, instructors, contributors, and practitioners who want more than isolated code snippets.

## Why this repository

| Capability | Included |
|---|:---:|
| Traditional and optimised implementations | ✅ |
| Explicit time and space complexity | ✅ |
| Typed reusable Python APIs | ✅ |
| Unit, edge-case, and integration tests | ✅ |
| Open-dataset validation | ✅ |
| Reproducible benchmark leaderboard | ✅ |
| Python 3.10–3.12 CI | ✅ |
| Educational notebooks preserved | ✅ |
| Contribution and security guidance | ✅ |

## Start here

- New learner: follow the [guided learning roadmap](docs/learning_roadmap.md).
- Choosing an algorithm: use the [complexity and selection guide](docs/complexity_guide.md).
- Looking for an implementation: browse the [solution catalogue](docs/solutions.md).
- Understanding the project: read the [architecture guide](docs/architecture.md).
- Reproducing results: see [open-dataset validation](docs/open-dataset-validation.md) and the [benchmark leaderboard](docs/benchmark_leaderboard.md).
- Troubleshooting: check the [FAQ](docs/faq.md).

## Algorithm coverage

| Area | Reference implementations |
|---|---|
| Searching and sorting | Binary search, merge sort |
| Dynamic programming | LIS baseline, optimised LIS, 0/1 knapsack, matrix-chain order |
| Strings | KMP, prefix function, Z-function, edit distance |
| Data structures | Union-Find, Fenwick Tree |
| Graphs | BFS path, Dijkstra, topological sort, Kruskal minimum spanning forest |
| Statistics | Welford online mean and variance |

The longest-increasing-subsequence implementations provide a direct baseline-versus-optimised comparison: O(n²) dynamic programming versus O(n log n) patience sorting.

## Architecture

```text
General/
├── src/general_reference/      # Maintained public APIs
├── tests/                      # Correctness and edge-case coverage
├── examples/                   # Runnable and dataset-backed examples
├── benchmarks/                 # Reproducible timing suite
├── benchmark-results/          # Generated Markdown and JSON outputs
├── docs/                       # Learning and engineering guides
├── .github/workflows/          # CI quality and benchmark automation
└── README.md                   # Project landing page
```

See the [architecture guide](docs/architecture.md) for design boundaries and the expected structure of new contributions.

## Installation

Clone the repository and install it in editable mode:

```bash
git clone https://github.com/sauravsingla/General.git
cd General
python -m pip install -e ".[datasets,dev]"
```

Python 3.10 or newer is supported.

## Quick example

```python
from general_reference import (
    breadth_first_path,
    longest_increasing_subsequence,
    longest_increasing_subsequence_dp,
    online_mean_variance,
)

values = [3, 1, 5, 2, 6, 4, 9]

baseline_length, baseline_sequence = longest_increasing_subsequence_dp(values)
fast_length, fast_sequence = longest_increasing_subsequence(values)

assert baseline_length == fast_length

route = breadth_first_path(
    {"A": ["B", "C"], "B": ["D"], "C": ["D"]},
    "A",
    "D",
)

summary = online_mean_variance([2.0, 4.0, 4.0, 5.0, 7.0, 9.0])
```

## Validate on open datasets

The validation runner uses datasets bundled with scikit-learn and NetworkX, so normal execution does not depend on external dataset downloads.

Datasets currently include Iris, Wine, Breast Cancer Wisconsin, and Zachary's Karate Club graph.

```bash
python examples/open_dataset_validation.py
```

It exercises sorting, searching, dynamic programming, string algorithms, data structures, graph routing, topological ordering, minimum spanning trees, and streaming statistics.

## Benchmark leaderboard

The benchmark suite uses fixed seeds, one warm-up, repeated measurements, median runtime, environment metadata, and both Markdown and JSON output.

```bash
python benchmarks/run_benchmarks.py --repeats 15
```

GitHub Actions publishes benchmark artifacts for Python 3.10, 3.11, and 3.12. Absolute timings vary by machine, so unrelated workloads should not be interpreted as claims of algorithmic superiority. Like-for-like comparisons are the most meaningful.

Read the full [benchmark methodology and leaderboard guide](docs/benchmark_leaderboard.md).

## Run quality checks

```bash
ruff check src tests examples benchmarks
pytest --cov=general_reference --cov-report=term-missing
python examples/open_dataset_validation.py
python benchmarks/run_benchmarks.py --repeats 15
```

## Learning approach

For each implementation:

1. Understand the problem and assumptions.
2. Work through a small input manually.
3. Read the documented time and space complexity.
4. Inspect edge-case tests.
5. Compare a transparent baseline with an optimised version where available.
6. Run the implementation on a modified or open dataset.
7. Explain when the method should not be used.

The goal is not to memorise code; it is to understand why a solution is correct and when its trade-offs are appropriate.

## Quality principles

1. **Correctness before cleverness.** Unsupported inputs and edge cases are explicit.
2. **Baseline before optimisation.** Faster methods can be checked against understandable references.
3. **Complexity is part of the API.** Performance trade-offs are documented, not implied.
4. **Reproducibility matters.** Benchmarks use fixed inputs and report their environment.
5. **Examples are not substitutes for tests.** Correctness, education, and performance are separated.
6. **Notebooks and maintained APIs have different roles.** Exploratory history is preserved without weakening package standards.

## Documentation

| Guide | Purpose |
|---|---|
| [Learning roadmap](docs/learning_roadmap.md) | Beginner-to-advanced study path and problem selection |
| [Solution catalogue](docs/solutions.md) | Problem descriptions, APIs, assumptions, and complexity |
| [Complexity guide](docs/complexity_guide.md) | Quick reference and algorithm-selection rules |
| [Architecture](docs/architecture.md) | Repository boundaries, data flow, and contribution structure |
| [Open-dataset validation](docs/open-dataset-validation.md) | Dataset provenance and reproduction instructions |
| [Benchmark leaderboard](docs/benchmark_leaderboard.md) | Measurement methodology and CI artifacts |
| [FAQ](docs/faq.md) | Common questions and troubleshooting |

## Contributing

Contributions are welcome when they add a clearly scoped problem, a correct and typed implementation, explicit complexity, meaningful tests, and documentation. Benchmarks should be added only for useful comparisons or regression risks.

Read [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md) before submitting changes.

## Citation

Academic or instructional use can cite the repository using [CITATION.cff](CITATION.cff). Please pin a release or commit when reproducibility matters.

## License

Released under the [MIT License](LICENSE).