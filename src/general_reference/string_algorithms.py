"""Efficient string-processing algorithms."""

from __future__ import annotations


def prefix_function(pattern: str) -> list[int]:
    """Return the KMP prefix table for ``pattern`` in O(n) time."""
    table = [0] * len(pattern)
    matched = 0
    for index in range(1, len(pattern)):
        while matched and pattern[index] != pattern[matched]:
            matched = table[matched - 1]
        if pattern[index] == pattern[matched]:
            matched += 1
        table[index] = matched
    return table


def kmp_search(text: str, pattern: str) -> list[int]:
    """Return all starting indices where ``pattern`` occurs in ``text``.

    Overlapping matches are included. Time complexity is O(len(text) +
    len(pattern)).
    """
    if pattern == "":
        return list(range(len(text) + 1))

    table = prefix_function(pattern)
    matches: list[int] = []
    matched = 0
    for index, character in enumerate(text):
        while matched and character != pattern[matched]:
            matched = table[matched - 1]
        if character == pattern[matched]:
            matched += 1
        if matched == len(pattern):
            matches.append(index - len(pattern) + 1)
            matched = table[matched - 1]
    return matches


def z_function(value: str) -> list[int]:
    """Return Z-values, where z[i] is the prefix match length at position i."""
    z_values = [0] * len(value)
    left = right = 0
    for index in range(1, len(value)):
        if index <= right:
            z_values[index] = min(right - index + 1, z_values[index - left])
        while (
            index + z_values[index] < len(value)
            and value[z_values[index]] == value[index + z_values[index]]
        ):
            z_values[index] += 1
        if index + z_values[index] - 1 > right:
            left = index
            right = index + z_values[index] - 1
    return z_values
