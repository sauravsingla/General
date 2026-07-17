# Open dataset validation

The integration runner in `examples/open_dataset_validation.py` exercises every public
reference family on small, established datasets that are bundled with maintained Python
libraries. It performs no network download at runtime.

## Datasets

| Dataset | Provider | Shape | Used for |
|---|---|---:|---|
| Iris | scikit-learn | 150 × 4 | Sorting, searching, knapsack, string labels and matrix dimensions |
| Wine | scikit-learn | 178 × 13 | Baseline and optimised longest increasing subsequence comparison |
| Breast Cancer Wisconsin (Diagnostic) | scikit-learn / UCI | 569 × 30 | Streaming mean and variance validation |
| Zachary's Karate Club | NetworkX | 34 nodes, 78 edges | BFS, Dijkstra, Kruskal MST and disjoint graph behaviour |

## Run locally

```bash
python -m pip install -e ".[datasets]"
python examples/open_dataset_validation.py
```

For the complete development checks:

```bash
python -m pip install -e ".[dev]"
ruff check src tests examples
pytest --cov=general_reference --cov-report=term-missing --cov-fail-under=95
python examples/open_dataset_validation.py
```

## Validation principles

- Data loaders are deterministic and bundled with their libraries.
- Assertions check structural invariants rather than hard-coding incidental floating-point output.
- The O(n²) and O(n log n) LIS implementations are cross-checked on the same real feature sequence.
- Graph algorithms operate on both unweighted and weighted views of the same public network.
- CI runs the dataset suite on every supported Python version.

These datasets are intentionally small enough for fast CI. They validate correctness and
reproducibility; they are not presented as large-scale performance benchmarks.
