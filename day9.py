#!/usr/bin/env python3.8
import timeit

from core.XMASencoding import find_first_number_not_summed_from_preamble, find_contiguous_set_for_sum
from readers.generic import read_and_rstrip


def part1() -> int:
    data = [int(x) for x in read_and_rstrip("data/day9_input.txt")]
    return find_first_number_not_summed_from_preamble(data, preamble_size=25)


def part2() -> int:
    data = [int(x) for x in read_and_rstrip("data/day9_input.txt")]
    answer = find_contiguous_set_for_sum(data, find_first_number_not_summed_from_preamble(data, preamble_size=25))
    return min(answer) + max(answer)


if __name__ == "__main__":
    print("Day9_Part1: found count: {}".format(part1()))

    print("Day9_Part2: found count: {}".format(part2()))

    #data = [int(x) for x in read_and_rstrip("data/day9_input.txt")]
    #iterations = 100
    #t = timeit.Timer(stmt='find_first_number_not_summed_from_preamble(data, preamble_size=25)', globals=globals())
    #performance_result_ms = t.timeit(number=iterations) / iterations * 1000
    #print(f'{performance_result_ms=}ms')
    #
    #t = timeit.Timer(stmt='find_contiguous_set_for_sum(data, 1721308972)', globals=globals())
    #performance_result_ms = t.timeit(number=iterations) / iterations * 1000
    #print(f'{performance_result_ms=}ms')
