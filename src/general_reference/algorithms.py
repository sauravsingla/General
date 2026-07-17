"""Reference implementations of frequently used algorithms.

Each function favours explicit behaviour, useful type hints and documented complexity.
Where helpful, both a traditional baseline and an optimised implementation are provided.
"""

from __future__ import annotations

from bisect import bisect_left
from collections.abc import Iterable, Sequence
from typing import TypeVar

T = TypeVar("T")


def binary_search(values: Sequence[T], target: T) -> int:
    """Return the index of *target* in a sorted sequence, or ``-1``.

    The implementation uses the standard library's well-tested bisection primitive.
    Time complexity is O(log n); space complexity is O(1).
    """
    index = bisect_left(values, target)
    return index if index < len(values) and values[index] == target else -1


def merge_sort(values: Iterable[T]) -> list[T]:
    """Return a stable sorted list without modifying the input.

    This explicit divide-and-conquer implementation is useful for learning and for
    objects whose ordering must remain stable. Time complexity is O(n log n) and
    auxiliary space complexity is O(n).
    """
    items = list(values)
    if len(items) < 2:
        return items

    midpoint = len(items) // 2
    left = merge_sort(items[:midpoint])
    right = merge_sort(items[midpoint:])
    merged: list[T] = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def longest_increasing_subsequence_dp(values: Sequence[T]) -> tuple[int, list[T]]:
    """Return one longest strictly increasing subsequence using classic DP.

    This transparent baseline compares each item with every earlier item. It is useful
    for teaching and for validating faster implementations. Time complexity is O(n²)
    and space complexity is O(n).
    """
    if not values:
        return 0, []

    lengths = [1] * len(values)
    predecessors = [-1] * len(values)

    for current in range(len(values)):
        for previous in range(current):
            if values[previous] < values[current] and lengths[previous] + 1 > lengths[current]:
                lengths[current] = lengths[previous] + 1
                predecessors[current] = previous

    current = max(range(len(values)), key=lengths.__getitem__)
    sequence: list[T] = []
    while current != -1:
        sequence.append(values[current])
        current = predecessors[current]
    sequence.reverse()
    return len(sequence), sequence


def longest_increasing_subsequence(values: Sequence[T]) -> tuple[int, list[T]]:
    """Return the length and one strictly increasing subsequence.

    Uses the modern patience-sorting approach with predecessor reconstruction.
    Time complexity is O(n log n), improving on the traditional O(n²) dynamic
    programming solution, while retaining O(n) space complexity.
    """
    if not values:
        return 0, []

    tail_indices: list[int] = []
    predecessors = [-1] * len(values)

    for index, value in enumerate(values):
        low, high = 0, len(tail_indices)
        while low < high:
            middle = (low + high) // 2
            if values[tail_indices[middle]] < value:
                low = middle + 1
            else:
                high = middle

        position = low
        if position > 0:
            predecessors[index] = tail_indices[position - 1]

        if position == len(tail_indices):
            tail_indices.append(index)
        else:
            tail_indices[position] = index

    sequence: list[T] = []
    current = tail_indices[-1]
    while current != -1:
        sequence.append(values[current])
        current = predecessors[current]
    sequence.reverse()

    return len(sequence), sequence
