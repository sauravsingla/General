from math import inf

import pytest

from general_reference.graphs import breadth_first_path, dijkstra_shortest_path


def test_breadth_first_path_returns_shortest_unweighted_route() -> None:
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": ["E"]}

    assert breadth_first_path(graph, "A", "E") == ["A", "C", "E"]


def test_breadth_first_path_handles_identity_and_unreachable_goal() -> None:
    assert breadth_first_path({}, "A", "A") == ["A"]
    assert breadth_first_path({"A": ["B"]}, "A", "Z") == []


def test_dijkstra_returns_minimum_cost_path() -> None:
    graph = {
        "A": [("B", 4), ("C", 1)],
        "C": [("B", 2), ("D", 5)],
        "B": [("D", 1)],
    }

    assert dijkstra_shortest_path(graph, "A", "D") == (4.0, ["A", "C", "B", "D"])


def test_dijkstra_supports_non_orderable_nodes_with_equal_costs() -> None:
    left, right, goal = object(), object(), object()
    graph = {"start": [(left, 1), (right, 1)], left: [(goal, 1)], right: [(goal, 1)]}

    cost, path = dijkstra_shortest_path(graph, "start", goal)

    assert cost == 2.0
    assert path[0] == "start"
    assert path[-1] is goal


def test_dijkstra_reports_unreachable_goal() -> None:
    assert dijkstra_shortest_path({"A": [("B", 1)]}, "A", "Z") == (inf, [])


@pytest.mark.parametrize("weight", [-1, float("nan"), float("inf")])
def test_dijkstra_rejects_invalid_weights(weight: float) -> None:
    with pytest.raises(ValueError, match="finite, non-negative"):
        dijkstra_shortest_path({"A": [("B", weight)]}, "A", "B")
