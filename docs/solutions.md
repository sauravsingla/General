# Solution catalogue

This catalogue connects each problem to a transparent baseline and, where useful, a more scalable implementation.

## Core algorithms

| Problem | Reference | Approach | Time | Space | Best use |
|---|---|---|---:|---:|---|
| Search sorted data | `binary_search` | Standard-library bisection | O(log n) | O(1) | Fast lookup when the input is already sorted |
| Stable sorting | `merge_sort` | Divide and conquer | O(n log n) | O(n) | Learning stable sorting and handling generic iterables |
| Longest increasing subsequence | `longest_increasing_subsequence_dp` | Traditional dynamic programming | O(n²) | O(n) | Teaching, small inputs and correctness comparison |
| Longest increasing subsequence | `longest_increasing_subsequence` | Patience sorting with reconstruction | O(n log n) | O(n) | Larger sequences and production-style use |

## Dynamic programming

| Problem | Reference | Approach | Time | Space | Output |
|---|---|---|---:|---:|---|
| 0/1 knapsack | `zero_one_knapsack` | Capacity-indexed dynamic programming | O(nC) | O(nC) | Optimal value and selected item indices |
| Edit distance | `edit_distance` | Space-optimised Levenshtein recurrence | O(nm) | O(min(n, m)) | Minimum insertion, deletion and substitution count |
| Matrix-chain multiplication | `matrix_chain_order` | Interval dynamic programming | O(n³) | O(n²) | Minimum scalar operations and parenthesization |

## Graphs

| Problem | Reference | Approach | Time | Space | Assumptions |
|---|---|---|---:|---:|---|
| Shortest unweighted path | `breadth_first_path` | Breadth-first search | O(V + E) | O(V) | All edges have equal cost |
| Shortest weighted path | `dijkstra_shortest_path` | Heap-based Dijkstra | O((V + E) log V) | O(V) | Edge weights are finite and non-negative |
| Dependency ordering | `topological_sort` | Kahn's algorithm | O(V + E) | O(V) | Directed graph must be acyclic |
| Minimum spanning forest | `kruskal_minimum_spanning_forest` | Kruskal plus union-find | O(E log E) | O(V) | Undirected weighted graph |

## String processing

| Problem | Reference | Approach | Time | Space | Notes |
|---|---|---|---:|---:|---|
| Prefix-border analysis | `prefix_function` | KMP prefix table | O(n) | O(n) | Building block for efficient matching |
| Exact substring matching | `kmp_search` | Knuth-Morris-Pratt | O(n + m) | O(m) | Includes overlapping matches |
| Prefix matching at every position | `z_function` | Z algorithm | O(n) | O(n) | Useful for pattern matching and periodicity |

## Data structures

| Problem | Reference | Operations | Time | Space | Best use |
|---|---|---|---:|---:|---|
| Dynamic connectivity | `DisjointSet` | add, find, union, connected | Amortized O(α(n)) | O(n) | Components, Kruskal and clustering |
| Prefix and range sums | `FenwickTree` | point add, prefix sum, range sum | O(log n) | O(n) | Frequently updated numeric sequences |

## Streaming statistics

| Problem | Reference | Approach | Time | Space | Advantage |
|---|---|---|---:|---:|---|
| Mean and variance | `online_mean_variance` | Welford's online algorithm | O(n) | O(1) | Stable for large values and streaming inputs |

## Choosing baseline or optimised code

Use a baseline implementation when explanation, auditing and comparison matter more than throughput. Use an optimised implementation when input size makes the baseline cost material. For important work, cross-check an optimised solution against the baseline on representative small inputs before relying on performance results.

## Notebook quality expectations

Historical notebooks remain available, but new or revised notebooks should:

1. state the problem and assumptions at the top;
2. use a local random generator such as `numpy.random.default_rng(seed)`;
3. avoid hidden downloads, credentials and machine-specific paths;
4. separate data generation, computation and visualisation;
5. report input size, complexity and runtime context;
6. clear unnecessarily large outputs before committing;
7. link reusable logic back to `src/general_reference/` instead of duplicating it.
