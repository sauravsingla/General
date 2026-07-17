"""Dependency-free graph algorithms with explicit validation and complexity notes."""

from __future__ import annotations

from collections import deque
from collections.abc import Hashable, Mapping, Sequence
from heapq import heappop, heappush
from math import isfinite
from typing import TypeVar

Node = TypeVar("Node", bound=Hashable)


def breadth_first_path(graph: Mapping[Node, Sequence[Node]], start: Node, goal: Node) -> list[Node]:
    """Return a shortest unweighted path from ``start`` to ``goal``.

    Returns an empty list when the goal is unreachable. The graph may omit leaf nodes.
    Time complexity is O(V + E), and auxiliary space complexity is O(V).
    """
    if start == goal:
        return [start]

    queue = deque([start])
    predecessor: dict[Node, Node | None] = {start: None}

    while queue:
        node = queue.popleft()
        for neighbour in graph.get(node, ()):
            if neighbour in predecessor:
                continue
            predecessor[neighbour] = node
            if neighbour == goal:
                return _reconstruct_path(predecessor, goal)
            queue.append(neighbour)

    return []


def dijkstra_shortest_path(
    graph: Mapping[Node, Sequence[tuple[Node, float]]], start: Node, goal: Node
) -> tuple[float, list[Node]]:
    """Return the minimum non-negative path cost and corresponding node sequence.

    Raises ``ValueError`` for negative or non-finite weights because Dijkstra's
    assumptions would otherwise be violated. An unreachable goal returns
    ``(float("inf"), [])``. Complexity is O((V + E) log V) with a binary heap.
    """
    distances: dict[Node, float] = {start: 0.0}
    predecessor: dict[Node, Node | None] = {start: None}
    heap: list[tuple[float, Node]] = [(0.0, start)]

    while heap:
        distance, node = heappop(heap)
        if distance != distances.get(node):
            continue
        if node == goal:
            return distance, _reconstruct_path(predecessor, goal)

        for neighbour, weight in graph.get(node, ()):
            numeric_weight = float(weight)
            if not isfinite(numeric_weight) or numeric_weight < 0:
                raise ValueError("Dijkstra requires finite, non-negative edge weights")

            candidate = distance + numeric_weight
            if candidate < distances.get(neighbour, float("inf")):
                distances[neighbour] = candidate
                predecessor[neighbour] = node
                heappush(heap, (candidate, neighbour))

    return float("inf"), []


def _reconstruct_path(predecessor: Mapping[Node, Node | None], goal: Node) -> list[Node]:
    path: list[Node] = []
    current: Node | None = goal
    while current is not None:
        path.append(current)
        current = predecessor[current]
    path.reverse()
    return path
