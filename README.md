# General: Practical Python, Statistics and Machine Learning

[![Quality](https://github.com/sauravsingla/General/actions/workflows/quality.yml/badge.svg)](https://github.com/sauravsingla/General/actions/workflows/quality.yml)
[![Benchmarks](https://github.com/sauravsingla/General/actions/workflows/benchmarks.yml/badge.svg)](https://github.com/sauravsingla/General/actions/workflows/benchmarks.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A curated collection of notebooks and reusable Python implementations for common problems in algorithms, statistics, data science and machine learning.

The repository preserves the original exploratory notebooks while adding production-style reference code so readers can compare:

- **Traditional approaches** — transparent, dependency-light methods that explain the fundamentals.
- **Modern approaches** — typed, reusable implementations with validation, tests and scalable complexity.
- **Notebook exploration** — visual experiments that make the underlying ideas easier to understand.
- **Measured performance** — reproducible leaderboards across supported Python versions.

## Repository map

| Area | What you will find |
|---|---|
| Root notebooks | Original Colab experiments and worked examples |
| `src/general_reference/` | Reusable, documented Python implementations |
| `tests/` | Behavioural, numerical and edge-case coverage |
| `benchmarks/` | Reproducible performance leaderboard generator |
| `docs/solutions.md` | Problem-to-solution catalogue with complexity and selection guidance |
| `docs/benchmark_leaderboard.md` | Benchmark methodology, datasets and reproduction guide |
| `.github/workflows/` | Automated linting, testing, coverage and benchmark runs |

## Reference implementations

| Domain | Traditional reference | Optimised or robust reference |
|---|---|---|
| Increasing subsequence | O(n²) dynamic programming | O(n log n) patience sorting |
| Unweighted graph routing | Breadth-first search | Shortest-path reconstruction |
| Weighted graph routing | — | Heap-based Dijkstra with validation |
| Mean and variance | Batch calculation | Welford streaming statistics |
| Searching | Linear reasoning baseline | Standard-library binary search |

See the complete [`solution catalogue`](docs/solutions.md) for assumptions, complexity and selection guidance.

## Benchmark leaderboard

The dedicated [`benchmark leaderboard`](docs/benchmark_leaderboard.md) measures the reusable algorithms on fixed synthetic inputs and bundled open datasets. GitHub Actions publishes ranked Markdown tables and machine-readable JSON for Python 3.10, 3.11 and 3.12.

```bash
python -m pip install -e ".[datasets,dev]"
python benchmarks/run_benchmarks.py --repeats 15
```

## Quick start

```bash
git clone https://github.com/sauravsingla/General.git
cd General
python -m pip install -e ".[dev]"
ruff check src tests
pytest --cov=general_reference --cov-report=term-missing
```

Python 3.10 or newer is supported.

## Examples

```python
from general_reference import (
    breadth_first_path,
    dijkstra_shortest_path,
    longest_increasing_subsequence,
    longest_increasing_subsequence_dp,
    online_mean_variance,
)

values = [3, 1, 5, 2, 6, 4, 9]
baseline_length, baseline_sequence = longest_increasing_subsequence_dp(values)
fast_length, fast_sequence = longest_increasing_subsequence(values)

route = breadth_first_path(
    {"A": ["B", "C"], "B": ["D"], "C": ["D"]},
    "A",
    "D",
)

cost, weighted_route = dijkstra_shortest_path(
    {"A": [("B", 4), ("C", 1)], "C": [("B", 2)]},
    "A",
    "B",
)

summary = online_mean_variance([2.0, 4.0, 4.0, 5.0, 7.0, 9.0])
```

## Quality principles

1. **Correctness before cleverness.** Public functions document assumptions and edge cases.
2. **Baseline before optimisation.** Faster solutions can be checked against transparent references.
3. **Complexity is explicit.** Time and space trade-offs are included with each implementation.
4. **Reproducibility matters.** Random examples should use explicit local generators and seeds.
5. **Generic code is tested.** Algorithms support reusable inputs rather than one fixed demonstration.
6. **Historical work is preserved.** Existing notebooks remain available as learning material.

## Project standards

The project uses `pytest`, coverage enforcement, `ruff`, type hints and GitHub Actions across Python 3.10, 3.11 and 3.12. Security and safe-use expectations are documented in [`SECURITY.md`](SECURITY.md).

## Contributing

Contributions are welcome when they add a clearly explained problem, a correct implementation, complexity analysis and tests. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

Released under the [MIT License](LICENSE).
