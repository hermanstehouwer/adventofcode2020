import itertools
from typing import List


def find_first_number_not_summed_from_preamble(data: List[int], preamble_size=25) -> int:
    for index in range(preamble_size, len(data)):
        preamble = data[index-preamble_size: index]
        found = False
        for combo in itertools.combinations(preamble, 2):
            if sum(combo) == data[index]:
                found = True
                break
        if not found:
            return data[index]
    return -1


def find_contiguous_set_for_sum(data: List[int], target_number: int) -> List[int]:
    from_idx = 0
    to_idx = 2
    current_sum = sum(data[from_idx: to_idx])
    while current_sum != target_number:
        if current_sum > target_number:
            current_sum -= data[from_idx]
            from_idx += 1
        else:
            current_sum += data[to_idx]
            to_idx += 1
    return data[from_idx: to_idx]
