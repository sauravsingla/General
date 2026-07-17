"""Reusable reference implementations for common technical problems."""

from .advanced_graphs import kruskal_minimum_spanning_forest, topological_sort
from .algorithms import (
    binary_search,
    longest_increasing_subsequence,
    longest_increasing_subsequence_dp,
    merge_sort,
)
from .data_structures import DisjointSet, FenwickTree
from .dynamic_programming import edit_distance, matrix_chain_order, zero_one_knapsack
from .graphs import breadth_first_path, dijkstra_shortest_path
from .statistics import RunningStatistics, online_mean_variance
from .string_algorithms import kmp_search, prefix_function, z_function

__all__ = [
    "DisjointSet",
    "FenwickTree",
    "RunningStatistics",
    "binary_search",
    "breadth_first_path",
    "dijkstra_shortest_path",
    "edit_distance",
    "kmp_search",
    "kruskal_minimum_spanning_forest",
    "longest_increasing_subsequence",
    "longest_increasing_subsequence_dp",
    "matrix_chain_order",
    "merge_sort",
    "online_mean_variance",
    "prefix_function",
    "topological_sort",
    "zero_one_knapsack",
    "z_function",
]
