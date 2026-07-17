"""Additional graph algorithms for dependency and network problems."""

from __future__ import annotations

from collections import deque
from collections.abc import Hashable, Iterable, Mapping, Sequence
from typing import TypeVar

from .data_structures import DisjointSet

Node = TypeVar("Node", bound=Hashable)


def topological_sort(graph: Mapping[Node, Iterable[Node]]) -> list[Node]:
    """Return a deterministic topological ordering using Kahn's algorithm.

    Raises ``ValueError`` when the directed graph contains a cycle. Nodes that
    only appear as neighbours are included automatically.
    """
    adjacency = {node: list(neighbours) for node, neighbours in graph.items()}
    indegree: dict[Node, int] = {node: 0 for node in adjacency}
    for neighbours in adjacency.values():
        for neighbour in neighbours:
            indegree.setdefault(neighbour, 0)
            adjacency.setdefault(neighbour, [])
            indegree[neighbour] += 1

    queue = deque(node for node, degree in indegree.items() if degree == 0)
    ordering: list[Node] = []
    while queue:
        node = queue.popleft()
        ordering.append(node)
        for neighbour in adjacency[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    if len(ordering) != len(indegree):
        raise ValueError("graph contains a cycle")
    return ordering


def kruskal_minimum_spanning_forest(
    nodes: Iterable[Node], edges: Sequence[tuple[float, Node, Node]]
) -> tuple[float, list[tuple[Node, Node, float]]]:
    """Return the minimum spanning forest using Kruskal's algorithm.

    The result supports disconnected undirected graphs. Time complexity is
    O(E log E), dominated by sorting the edges.
    """
    node_list = list(dict.fromkeys(nodes))
    disjoint_set = DisjointSet(node_list)
    selected: list[tuple[Node, Node, float]] = []
    total_weight = 0.0

    for weight, first, second in sorted(edges, key=lambda edge: edge[0]):
        if first not in disjoint_set._parent or second not in disjoint_set._parent:
            raise ValueError("every edge endpoint must appear in nodes")
        if disjoint_set.union(first, second):
            selected.append((first, second, float(weight)))
            total_weight += float(weight)

    return total_weight, selected
