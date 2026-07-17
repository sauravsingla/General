# Repository architecture

This repository separates exploratory learning material from reusable reference code, validation, and performance evidence.

```text
General/
├── src/general_reference/      # Typed, reusable algorithm implementations
├── tests/                      # Unit, edge-case, and integration coverage
├── examples/                   # Executable demonstrations and dataset validation
├── benchmarks/                 # Reproducible runtime benchmark runner
├── benchmark-results/          # Generated Markdown and JSON outputs
├── docs/                       # Learning, complexity, dataset, and benchmark guides
├── .github/workflows/          # Quality and benchmark automation
├── pyproject.toml              # Packaging, dependencies, and tool configuration
└── README.md                   # Project landing page and navigation
```

## Design boundaries

### Exploratory notebooks

The original notebooks remain learning assets. They are useful for visual exploration, experimentation, and explaining how an idea develops.

### Reference package

`src/general_reference/` contains the maintained public API. Code in this package should be:

- deterministic unless randomness is an explicit input;
- typed and documented;
- independent of one fixed dataset;
- validated for unsupported or unsafe inputs;
- covered by focused tests;
- accompanied by explicit time and space complexity.

### Tests

The test suite verifies correctness, numerical behaviour, error handling, and agreement between transparent baselines and optimised implementations.

### Examples and datasets

Examples demonstrate realistic usage. The open-dataset validation runner uses datasets bundled with scikit-learn and NetworkX, avoiding external downloads during normal execution.

### Benchmarks

Benchmarks are evidence, not correctness tests. They use fixed inputs, warm-up runs, repeated measurements, median runtimes, and machine-readable output. Results naturally vary between systems.

## Data flow

```text
Open or seeded input
        │
        ▼
Reference implementation ─────► Unit and integration tests
        │
        ├──────────────────────► Executable examples
        │
        └──────────────────────► Benchmark runner
                                      │
                                      ├── Markdown leaderboard
                                      └── JSON artifact
```

## Adding a new algorithm

A complete contribution normally includes:

1. A public implementation under `src/general_reference/`.
2. Clear assumptions, failure behaviour, and complexity in the docstring.
3. Unit tests covering normal, boundary, and invalid inputs.
4. An export from the package when intended as public API.
5. Documentation in the solution catalogue and complexity guide.
6. An example or benchmark when it adds meaningful educational value.

This structure keeps teaching material approachable while giving practitioners a dependable reference package.