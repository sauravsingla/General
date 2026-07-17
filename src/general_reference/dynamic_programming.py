"""Dynamic programming reference implementations.

Each function favours explicit state transitions and reconstructable results so the
module can be used for teaching, testing, and production prototypes.
"""

from __future__ import annotations

from collections.abc import Sequence


def zero_one_knapsack(
    weights: Sequence[int], values: Sequence[float], capacity: int
) -> tuple[float, list[int]]:
    """Return the maximum value and selected item indices for 0/1 knapsack.

    Time complexity is O(n * capacity); space complexity is O(n * capacity).
    """
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    if capacity < 0:
        raise ValueError("capacity must be non-negative")
    if any(weight <= 0 for weight in weights):
        raise ValueError("weights must be positive integers")

    item_count = len(weights)
    table = [[0.0] * (capacity + 1) for _ in range(item_count + 1)]

    for item in range(1, item_count + 1):
        weight = weights[item - 1]
        value = float(values[item - 1])
        for current_capacity in range(capacity + 1):
            table[item][current_capacity] = table[item - 1][current_capacity]
            if weight <= current_capacity:
                candidate = table[item - 1][current_capacity - weight] + value
                table[item][current_capacity] = max(
                    table[item][current_capacity], candidate
                )

    selected: list[int] = []
    remaining = capacity
    for item in range(item_count, 0, -1):
        if table[item][remaining] != table[item - 1][remaining]:
            selected.append(item - 1)
            remaining -= weights[item - 1]
    selected.reverse()
    return table[item_count][capacity], selected


def edit_distance(source: str, target: str) -> int:
    """Return the Levenshtein distance between two strings.

    Time complexity is O(len(source) * len(target)); space complexity is
    O(min(len(source), len(target))).
    """
    if len(source) < len(target):
        source, target = target, source

    previous = list(range(len(target) + 1))
    for source_index, source_character in enumerate(source, start=1):
        current = [source_index]
        for target_index, target_character in enumerate(target, start=1):
            insertion = current[target_index - 1] + 1
            deletion = previous[target_index] + 1
            substitution = previous[target_index - 1] + (
                source_character != target_character
            )
            current.append(min(insertion, deletion, substitution))
        previous = current
    return previous[-1]


def matrix_chain_order(dimensions: Sequence[int]) -> tuple[int, str]:
    """Return minimum scalar multiplications and an optimal parenthesization.

    ``dimensions`` of length n + 1 describes n matrices, where matrix i has
    shape dimensions[i] x dimensions[i + 1].
    """
    if len(dimensions) < 2:
        raise ValueError("at least two dimensions are required")
    if any(dimension <= 0 for dimension in dimensions):
        raise ValueError("dimensions must be positive integers")

    matrix_count = len(dimensions) - 1
    costs = [[0] * matrix_count for _ in range(matrix_count)]
    splits = [[0] * matrix_count for _ in range(matrix_count)]

    for chain_length in range(2, matrix_count + 1):
        for start in range(matrix_count - chain_length + 1):
            end = start + chain_length - 1
            best_cost: int | None = None
            for split in range(start, end):
                candidate = (
                    costs[start][split]
                    + costs[split + 1][end]
                    + dimensions[start]
                    * dimensions[split + 1]
                    * dimensions[end + 1]
                )
                if best_cost is None or candidate < best_cost:
                    best_cost = candidate
                    splits[start][end] = split
            costs[start][end] = 0 if best_cost is None else best_cost

    def build(start: int, end: int) -> str:
        if start == end:
            return f"A{start + 1}"
        split = splits[start][end]
        return f"({build(start, split)} × {build(split + 1, end)})"

    return costs[0][matrix_count - 1], build(0, matrix_count - 1)
