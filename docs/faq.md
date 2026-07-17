# Frequently asked questions

## Is this repository a Python package or a notebook collection?

It is both. The original notebooks are preserved for exploration, while `src/general_reference/` provides the maintained, reusable API.

## Which Python versions are supported?

Python 3.10, 3.11, and 3.12 are exercised in GitHub Actions.

## Do examples download datasets from the internet?

The open-dataset validation uses datasets bundled with scikit-learn and NetworkX. Normal validation therefore does not require dataset downloads at runtime.

## Are benchmark rankings portable between machines?

No. Absolute timings vary with CPU, operating system, Python version, system load, and dependency versions. Reproduce the benchmark locally and use identical inputs when comparing changes.

## Why rank unrelated algorithms in one leaderboard?

The overall table is a compact execution-cost overview, not a claim that one problem is better than another. Like-for-like comparisons—especially baseline versus optimised LIS—are the meaningful performance comparisons.

## Why keep a slow baseline implementation?

Transparent baselines are useful for teaching, testing, and validating optimised solutions. They should remain clearly labelled so users do not select them accidentally for large inputs.

## Can Dijkstra handle negative edge weights?

No. The implementation rejects negative and non-finite weights because they violate Dijkstra's assumptions.

## What happens when a graph is disconnected?

Path functions return their documented unreachable result. Kruskal returns a minimum spanning forest rather than pretending a single spanning tree exists.

## How do I run all quality checks?

```bash
python -m pip install -e ".[datasets,dev]"
ruff check src tests examples benchmarks
pytest --cov=general_reference --cov-report=term-missing
python examples/open_dataset_validation.py
python benchmarks/run_benchmarks.py --repeats 15
```

## The package cannot be imported

Install the repository in editable mode from its root:

```bash
python -m pip install -e ".[dev]"
```

Avoid running source files from inside `src/general_reference/` because that changes Python's import path.

## A benchmark result changed significantly

First verify that the Python version, platform, dependency versions, input sizes, repetition count, and system load are comparable. Performance differences on tiny workloads may be timer noise.

## How should I contribute a new implementation?

Include a clear problem statement, assumptions, typed implementation, complexity analysis, edge-case tests, and documentation. Add a benchmark only when it measures a meaningful comparison or regression risk.

## Is every notebook production-ready?

No. Notebooks are exploratory learning material. Use the tested APIs under `src/general_reference/` when you need maintained reference implementations.

## Where should a new user begin?

Start with the [learning roadmap](learning_roadmap.md), then use the [complexity guide](complexity_guide.md) and [solution catalogue](solutions.md) to choose a topic.