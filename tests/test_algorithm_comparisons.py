from general_reference.algorithms import (
    longest_increasing_subsequence,
    longest_increasing_subsequence_dp,
)


def _is_strictly_increasing(values: list[int]) -> bool:
    return all(left < right for left, right in zip(values, values[1:]))


def _is_subsequence(candidate: list[int], values: list[int]) -> bool:
    iterator = iter(values)
    return all(any(item == expected for item in iterator) for expected in candidate)


def test_lis_implementations_agree_on_optimal_length() -> None:
    examples = [
        [],
        [5],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [3, 1, 5, 2, 6, 4, 9],
        [2, 2, 2, 2],
        [10, 9, 2, 5, 3, 7, 101, 18],
    ]

    for values in examples:
        baseline_length, baseline = longest_increasing_subsequence_dp(values)
        optimised_length, optimised = longest_increasing_subsequence(values)

        assert baseline_length == optimised_length
        assert len(baseline) == baseline_length
        assert len(optimised) == optimised_length
        assert _is_strictly_increasing(baseline)
        assert _is_strictly_increasing(optimised)
        assert _is_subsequence(baseline, values)
        assert _is_subsequence(optimised, values)
