"""Reusable data structures with explicit complexity guarantees."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Generic, TypeVar

T = TypeVar("T", bound=object)


class DisjointSet(Generic[T]):
    """Union-find with path compression and union by rank."""

    def __init__(self, items: Iterable[T] = ()) -> None:
        self._parent: dict[T, T] = {}
        self._rank: dict[T, int] = {}
        for item in items:
            self.add(item)

    def add(self, item: T) -> None:
        """Add an item as a singleton set in amortized O(1) time."""
        if item not in self._parent:
            self._parent[item] = item
            self._rank[item] = 0

    def find(self, item: T) -> T:
        """Return the representative for ``item`` with path compression."""
        if item not in self._parent:
            raise KeyError(item)
        parent = self._parent[item]
        if parent != item:
            self._parent[item] = self.find(parent)
        return self._parent[item]

    def union(self, first: T, second: T) -> bool:
        """Merge two sets and return whether a merge occurred."""
        first_root = self.find(first)
        second_root = self.find(second)
        if first_root == second_root:
            return False
        if self._rank[first_root] < self._rank[second_root]:
            first_root, second_root = second_root, first_root
        self._parent[second_root] = first_root
        if self._rank[first_root] == self._rank[second_root]:
            self._rank[first_root] += 1
        return True

    def connected(self, first: T, second: T) -> bool:
        """Return whether two items belong to the same set."""
        return self.find(first) == self.find(second)


class FenwickTree:
    """Fenwick tree supporting point updates and prefix/range sums."""

    def __init__(self, values: Iterable[float] = ()) -> None:
        materialized = list(values)
        self._tree = [0.0] * (len(materialized) + 1)
        for index, value in enumerate(materialized):
            self.add(index, value)

    def __len__(self) -> int:
        return len(self._tree) - 1

    def add(self, index: int, delta: float) -> None:
        """Add ``delta`` at a zero-based index in O(log n) time."""
        if index < 0 or index >= len(self):
            raise IndexError("index out of range")
        internal = index + 1
        while internal < len(self._tree):
            self._tree[internal] += delta
            internal += internal & -internal

    def prefix_sum(self, end: int) -> float:
        """Return sum of values in the half-open range [0, end)."""
        if end < 0 or end > len(self):
            raise IndexError("end out of range")
        total = 0.0
        while end:
            total += self._tree[end]
            end -= end & -end
        return total

    def range_sum(self, start: int, end: int) -> float:
        """Return sum of values in the half-open range [start, end)."""
        if start < 0 or start > end or end > len(self):
            raise IndexError("invalid range")
        return self.prefix_sum(end) - self.prefix_sum(start)
