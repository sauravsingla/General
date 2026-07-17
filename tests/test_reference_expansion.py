import pytest

from general_reference.advanced_graphs import (
    kruskal_minimum_spanning_forest,
    topological_sort,
)
from general_reference.data_structures import DisjointSet, FenwickTree
from general_reference.dynamic_programming import (
    edit_distance,
    matrix_chain_order,
    zero_one_knapsack,
)
from general_reference.string_algorithms import kmp_search, prefix_function, z_function


def test_zero_one_knapsack_reconstructs_selected_items() -> None:
    value, selected = zero_one_knapsack([2, 3, 4, 5], [3, 4, 5, 8], 5)
    assert value == 8
    assert selected == [3]


def test_zero_one_knapsack_validates_inputs() -> None:
    with pytest.raises(ValueError):
        zero_one_knapsack([1], [1, 2], 3)
    with pytest.raises(ValueError):
        zero_one_knapsack([0], [1], 3)


def test_edit_distance_handles_standard_and_empty_cases() -> None:
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("", "abc") == 3
    assert edit_distance("same", "same") == 0


def test_matrix_chain_order_returns_optimal_cost() -> None:
    cost, parenthesization = matrix_chain_order([30, 35, 15, 5, 10, 20, 25])
    assert cost == 15125
    assert parenthesization.count("A") == 6


def test_string_algorithms_support_overlapping_matches() -> None:
    assert prefix_function("ababaca") == [0, 0, 1, 2, 3, 0, 1]
    assert kmp_search("aaaa", "aa") == [0, 1, 2]
    assert kmp_search("abc", "") == [0, 1, 2, 3]
    assert z_function("aaaaa") == [0, 4, 3, 2, 1]


def test_disjoint_set_merges_components() -> None:
    groups = DisjointSet(["a", "b", "c"])
    assert groups.union("a", "b") is True
    assert groups.union("a", "b") is False
    assert groups.connected("a", "b") is True
    assert groups.connected("a", "c") is False
    with pytest.raises(KeyError):
        groups.find("missing")


def test_fenwick_tree_supports_updates_and_ranges() -> None:
    tree = FenwickTree([1, 2, 3, 4])
    assert tree.prefix_sum(3) == 6
    assert tree.range_sum(1, 4) == 9
    tree.add(2, 5)
    assert tree.range_sum(2, 3) == 8
    with pytest.raises(IndexError):
        tree.add(4, 1)


def test_topological_sort_orders_dependencies_and_rejects_cycles() -> None:
    ordering = topological_sort({"plan": ["build"], "build": ["test"], "test": []})
    assert ordering.index("plan") < ordering.index("build") < ordering.index("test")
    with pytest.raises(ValueError, match="cycle"):
        topological_sort({"a": ["b"], "b": ["a"]})


def test_kruskal_returns_minimum_spanning_forest() -> None:
    total, edges = kruskal_minimum_spanning_forest(
        ["a", "b", "c", "d"],
        [(1, "a", "b"), (4, "a", "c"), (2, "b", "c"), (3, "c", "d")],
    )
    assert total == 6
    assert len(edges) == 3
    with pytest.raises(ValueError):
        kruskal_minimum_spanning_forest(["a"], [(1, "a", "b")])
