import math

import pytest

from general_reference.algorithms import (
    binary_search,
    longest_increasing_subsequence,
    merge_sort,
)
from general_reference.statistics import online_mean_variance


def test_binary_search_handles_present_and_missing_values() -> None:
    values = [1, 4, 7, 10, 15]
    assert binary_search(values, 7) == 2
    assert binary_search(values, 8) == -1
    assert binary_search([], 1) == -1


def test_merge_sort_is_stable_and_does_not_mutate_input() -> None:
    values = [5, 1, 4, 1, 3]
    assert merge_sort(values) == [1, 1, 3, 4, 5]
    assert values == [5, 1, 4, 1, 3]


def test_longest_increasing_subsequence_returns_valid_solution() -> None:
    values = [3, 1, 5, 2, 6, 4, 9]
    length, sequence = longest_increasing_subsequence(values)
    assert length == 4
    assert len(sequence) == length
    assert all(left < right for left, right in zip(sequence, sequence[1:]))


def test_online_statistics_match_known_example() -> None:
    summary = online_mean_variance([2, 4, 4, 4, 5, 5, 7, 9])
    assert summary.count == 8
    assert summary.mean == pytest.approx(5.0)
    assert summary.population_variance == pytest.approx(4.0)
    assert summary.population_standard_deviation == pytest.approx(2.0)


def test_online_statistics_remain_stable_for_large_offsets() -> None:
    summary = online_mean_variance([1_000_000_001, 1_000_000_002, 1_000_000_003])
    assert summary.mean == pytest.approx(1_000_000_002)
    assert summary.sample_variance == pytest.approx(1.0)


def test_online_statistics_reject_invalid_input() -> None:
    with pytest.raises(ValueError, match="at least one"):
        online_mean_variance([])
    with pytest.raises(ValueError, match="finite"):
        online_mean_variance([1.0, math.inf])
