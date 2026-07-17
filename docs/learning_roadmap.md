# Learning roadmap

The repository supports two complementary paths: learning the fundamentals and selecting reliable techniques for practical work.

## Path 1: Foundations

1. **Searching and sorting**
   - Understand ordered data, comparison-based sorting, and binary search.
   - Start with `merge_sort` and `binary_search`.

2. **Streaming statistics**
   - Learn why numerical stability matters.
   - Use `online_mean_variance` to process values in one pass and constant extra space.

3. **Dynamic programming**
   - Learn how overlapping subproblems become reusable state.
   - Compare the O(n²) longest-increasing-subsequence baseline with the O(n log n) implementation.
   - Continue with 0/1 knapsack and matrix-chain multiplication.

4. **String processing**
   - Move beyond repeated slicing and naive matching.
   - Study prefix tables through KMP, then compare with the Z-function.
   - Use edit distance for sequence similarity.

5. **Data structures**
   - Use Union-Find for connectivity and Kruskal's algorithm.
   - Use a Fenwick Tree for efficient prefix and range sums.

6. **Graph algorithms**
   - Begin with breadth-first search for unweighted paths.
   - Use Dijkstra for non-negative weighted paths.
   - Study topological ordering for dependency graphs.
   - Use Kruskal for minimum spanning forests.

7. **Engineering and reproducibility**
   - Run tests, dataset validation, and benchmarks.
   - Inspect assumptions, failure modes, and complexity before choosing an implementation.

## Path 2: Choose by problem

| Problem | Recommended starting point | Important constraint |
|---|---|---|
| Find an item in sorted data | Binary search | Input must be ordered |
| Sort generic comparable values | Merge sort | Requires O(n) auxiliary space |
| Compute mean/variance from a stream | Welford online statistics | Reject non-finite inputs |
| Find a shortest path in an unweighted graph | Breadth-first search | O(V + E) traversal |
| Find a shortest path with non-negative weights | Dijkstra | Negative edges are invalid |
| Order tasks with dependencies | Topological sort | Graph must be acyclic |
| Connect components at minimum total cost | Kruskal + Union-Find | Returns a forest for disconnected graphs |
| Repeated prefix/range sums with updates | Fenwick Tree | Best for associative prefix sums |
| Find all exact pattern matches | KMP | Linear in text + pattern length |
| Measure insertion/deletion/substitution distance | Edit distance | O(nm) dynamic programming |
| Select items under a capacity limit | 0/1 knapsack | Pseudo-polynomial in capacity |
| Find an increasing subsequence | Patience-sorting LIS | O(n log n), use DP baseline to learn |

## Suggested study routine

For each topic:

1. Read the public function's docstring.
2. Work through one small example manually.
3. Read the corresponding tests to see boundary conditions.
4. Run the implementation on a modified input.
5. Compare the documented complexity with benchmark behaviour.
6. Explain when the algorithm should not be used.

## Reproduction commands

```bash
python -m pip install -e ".[datasets,dev]"
pytest --cov=general_reference --cov-report=term-missing
python examples/open_dataset_validation.py
python benchmarks/run_benchmarks.py --repeats 15
```

The goal is not to memorise code. It is to understand the assumptions that make each solution correct and the trade-offs that make it appropriate.