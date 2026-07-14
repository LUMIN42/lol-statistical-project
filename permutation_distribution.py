import random
from typing import Callable
import numpy as np

random.seed(75511435)


# while grossly underoptimized, it should suffice
# could be optimized by taking into account that the data is just a pool of boolean values

def permutation_distribution(pool: list,
                             relevant_statistic: Callable[[list, list], float],
                             subset_size: int, sample_count: int = 10 ** 5):
  pool_copy = pool.copy()

  result = []

  for _ in range(sample_count):
    random.shuffle(pool_copy)
    marked = pool_copy[:subset_size]
    rest = pool_copy[subset_size:]

    stat = relevant_statistic(marked, rest)

    result.append(stat)

  result.sort()
  return result


def significant_value(distribution_values, top_percentile: float | None = None,
                      bottom_percentile: float | None = None):
  if top_percentile is None and bottom_percentile is None:
    raise Exception("can't have both top and bottom percentile be None")

  if top_percentile is not None:
    top_value = float(np.percentile(distribution_values, top_percentile))

  if bottom_percentile is not None:
    bottom_value = float(np.percentile(distribution_values, bottom_percentile))

  if top_percentile is None:
    return bottom_value

  if bottom_percentile is None:
    return top_value

  return [bottom_value, top_value]
