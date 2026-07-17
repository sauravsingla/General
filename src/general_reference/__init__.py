"""Reusable reference implementations for common technical problems."""

from .algorithms import (
    binary_search,
    longest_increasing_subsequence,
    longest_increasing_subsequence_dp,
    merge_sort,
)
from .graphs import breadth_first_path, dijkstra_shortest_path
from .statistics import RunningStatistics, online_mean_variance

__all__ = [
    "RunningStatistics",
    "binary_search",
    "breadth_first_path",
    "dijkstra_shortest_path",
    "longest_increasing_subsequence",
    "longest_increasing_subsequence_dp",
    "merge_sort",
    "online_mean_variance",
]
