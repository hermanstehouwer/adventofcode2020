from typing import Tuple, List
import itertools


def find_inputs_that_sumto(input: List[int], target_sum: int = 2020, number_of_inputs:int = 2) -> List[int]:
    for p in itertools.permutations(input, number_of_inputs):
        if sum(p) == target_sum:
            return [x for x in p]
    raise ValueError(f"Cannot find two elements in the list that sum to {target_sum}")
