"""Numerically stable statistical utilities."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
import math


@dataclass(frozen=True, slots=True)
class RunningStatistics:
    """Summary produced by a single-pass streaming calculation."""

    count: int
    mean: float
    sample_variance: float
    population_variance: float

    @property
    def sample_standard_deviation(self) -> float:
        return math.sqrt(self.sample_variance)

    @property
    def population_standard_deviation(self) -> float:
        return math.sqrt(self.population_variance)


def online_mean_variance(values: Iterable[float]) -> RunningStatistics:
    """Calculate mean and variance with Welford's stable online algorithm.

    Unlike a naive two-pass formula, this method supports streams and avoids large
    cancellation errors when observations have a large offset but small variance.
    It runs in O(n) time and O(1) additional space.

    Raises:
        ValueError: If the iterable is empty or contains a non-finite value.
    """
    count = 0
    mean = 0.0
    sum_squared_deviations = 0.0

    for raw_value in values:
        value = float(raw_value)
        if not math.isfinite(value):
            raise ValueError("values must contain only finite numbers")

        count += 1
        delta = value - mean
        mean += delta / count
        delta_after_update = value - mean
        sum_squared_deviations += delta * delta_after_update

    if count == 0:
        raise ValueError("at least one value is required")

    population_variance = sum_squared_deviations / count
    sample_variance = sum_squared_deviations / (count - 1) if count > 1 else 0.0
    return RunningStatistics(
        count=count,
        mean=mean,
        sample_variance=sample_variance,
        population_variance=population_variance,
    )
