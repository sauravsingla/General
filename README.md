# General: Practical Python, Statistics and Machine Learning

A curated collection of notebooks and reusable Python implementations for solving common problems in statistics, algorithms, data science and machine learning.

The repository keeps the original exploratory notebooks and adds production-style reference code so readers can compare:

- **Traditional approaches** — transparent, dependency-light methods that explain the fundamentals.
- **Modern approaches** — typed, reusable implementations with validation, tests and scalable patterns.
- **Notebook exploration** — visual experiments that make the underlying ideas easier to understand.

## Repository map

| Area | What you will find |
|---|---|
| Root notebooks | Original Colab experiments and worked examples |
| `src/general_reference/` | Reusable, documented Python implementations |
| `tests/` | Behavioural tests and edge-case coverage |
| `docs/solutions.md` | Problem-to-solution index with complexity notes |

## Featured topics

- Probability distributions and the Central Limit Theorem
- Ranking and response scoring
- Search, sorting and dynamic programming
- Numerical stability and vectorised computation
- Data validation and reproducible experiments
- Modern Python design: type hints, dataclasses and testable APIs

## Quick start

```bash
git clone https://github.com/sauravsingla/General.git
cd General
python -m pip install -e ".[dev]"
pytest
```

Python 3.10 or newer is recommended.

## Using the reference implementations

```python
from general_reference.algorithms import binary_search, longest_increasing_subsequence
from general_reference.statistics import online_mean_variance

position = binary_search([1, 4, 7, 10], 7)
length, sequence = longest_increasing_subsequence([3, 1, 5, 2, 6, 4, 9])
summary = online_mean_variance([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0])
```

## Design principles

1. **Correctness before cleverness.** Every public function validates assumptions and documents edge cases.
2. **Explain the trade-off.** Implementations include time and space complexity where useful.
3. **Reproducibility.** Random examples use explicit seeds or generators.
4. **Readable APIs.** Solutions are designed for learning and reuse, not just one-off execution.
5. **Backward preservation.** Existing notebooks remain available as historical learning material.

## Quality checks

The project uses `pytest` for tests, `ruff` for linting and GitHub Actions for automated validation.

## Contributing

Contributions are welcome when they add a clearly explained problem, a correct implementation, complexity analysis and tests. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

This repository is provided for educational and reference use. See [`LICENSE`](LICENSE) for terms.
