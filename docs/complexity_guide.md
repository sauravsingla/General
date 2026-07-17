# Complexity and selection guide

Complexity describes how resource use grows with input size. It does not replace measurement: constants, data layout, Python overhead, and the shape of the input still matter.

## Quick reference

| Algorithm | Typical time | Extra space | Best use | Avoid when |
|---|---:|---:|---|---|
| Binary search | O(log n) | O(1) | Lookup in sorted data | Data changes frequently and is unsorted |
| Merge sort | O(n log n) | O(n) | Predictable stable sorting | Auxiliary memory is highly constrained |
| LIS dynamic programming | O(n²) | O(n) | Teaching, reconstruction baseline, small inputs | Large sequences |
| LIS patience sorting | O(n log n) | O(n) | Large sequences | You need the simplest possible explanation |
| Welford statistics | O(n) | O(1) | Streams and numerically stable variance | You need quantiles or the full distribution |
| 0/1 knapsack | O(nC) | Implementation-dependent | Discrete selection with moderate capacity C | Capacity is extremely large or continuous |
| Matrix-chain order | O(n³) | O(n²) | Optimising matrix multiplication order | Matrix order is fixed by other constraints |
| Edit distance | O(nm) | O(nm) | Exact sequence difference | Very long sequences without pruning/banding |
| KMP search | O(n + m) | O(m) | Exact repeated pattern matching | Approximate matching is required |
| Z-function | O(n) | O(n) | Prefix matching and string analysis | The task is approximate matching |
| Fenwick Tree | O(log n) update/query | O(n) | Dynamic prefix sums | Arbitrary range aggregation is required |
| Union-Find | Near O(1) amortised | O(n) | Dynamic connectivity and Kruskal | Deletions or path queries are central |
| Breadth-first search | O(V + E) | O(V) | Unweighted shortest paths | Edge weights differ |
| Dijkstra | O((V + E) log V) | O(V) | Non-negative weighted shortest paths | Any edge may have negative weight |
| Topological sort | O(V + E) | O(V) | Dependency ordering | The graph contains a cycle |
| Kruskal MST | O(E log E) | O(V) | Sparse weighted graphs and forests | You need a directed spanning structure |

## How to reason about complexity

### Input size must be explicit

For arrays and strings, `n` usually means the number of elements or characters. For graphs, use both vertices `V` and edges `E`. For knapsack, capacity `C` is part of the cost. For edit distance, both sequence lengths `n` and `m` matter.

### Worst case is not the whole story

Big-O is an upper-bound growth model. Two O(n log n) implementations can have very different runtimes because of allocation, interpreter overhead, cache behaviour, and input distribution.

### Space complexity matters in production

An algorithm with lower runtime can be inappropriate if it duplicates a very large input. The repository documents auxiliary space separately where practical.

## Baseline versus optimised implementation

A baseline is valuable when it is easier to verify and explain. An optimised version is valuable when input scale makes the baseline impractical.

The longest-increasing-subsequence pair demonstrates this pattern:

- Dynamic programming: transparent O(n²) state transitions.
- Patience sorting: O(n log n) through binary search over candidate tails.

Use the baseline to understand and cross-check correctness. Use the optimised implementation for larger inputs.

## Graph selection rules

- Use BFS when every edge has equal cost.
- Use Dijkstra when weights are finite and non-negative.
- Do not silently use Dijkstra for negative weights.
- Use topological sort only for directed acyclic dependency graphs.
- Use Kruskal when the objective is minimum total undirected connection cost.

## Measurement guidance

For trustworthy comparisons:

1. Compare implementations solving the same problem on identical inputs.
2. Warm up the interpreter and imports.
3. Run multiple repetitions.
4. Prefer median over a single measurement.
5. Record Python version and platform.
6. Treat very small timings cautiously because timer noise dominates.
7. Keep correctness tests separate from performance benchmarks.

See the [benchmark leaderboard](benchmark_leaderboard.md) for the repository's reproducible methodology.