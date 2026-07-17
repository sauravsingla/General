# Contributing

Thank you for improving this educational reference repository.

## What a good contribution includes

- A clearly stated problem and expected behaviour
- A readable implementation with type hints
- Time and space complexity where relevant
- Tests for normal cases, edge cases and invalid input
- Reproducible examples without hidden local dependencies
- A focused commit message describing one logical change

## Development workflow

```bash
python -m pip install -e ".[dev]"
ruff check src tests
pytest
```

Keep notebook outputs small. Remove credentials, local paths, large generated files and private data before committing.

## Solution style

Prefer standard-library solutions when they are clear and robust. When adding a modern or optimised method, explain how it differs from the traditional approach and when the added complexity is worthwhile.

## Commit style

Use short, natural messages such as:

- `Add breadth-first graph traversal`
- `Handle empty samples in variance example`
- `Document dynamic programming trade-offs`

Each commit should represent one reviewable idea.
