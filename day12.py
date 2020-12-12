#!/usr/bin/env python3.8
import timeit

from core.boating import get_coordinates, action_to_direction, manhattan, get_coordinates2
from readers.generic import read_and_rstrip

def part1() -> int:
    *_, last = get_coordinates(action_to_direction(read_and_rstrip("data/day12_input.txt")))
    return manhattan(0, 0, last[0], last[1])


def part2() -> int:
    *_, last = get_coordinates2(read_and_rstrip("data/day12_input.txt"))
    return manhattan(0, 0, last[0], last[1])

if __name__ == "__main__":
    print("Day12_Part1: found count: {}".format(part1()))

    print("Day12_Part2: found count: {}".format(part2()))

    #data = [int(x) for x in read_and_rstrip("data/day9_input.txt")]
    #iterations = 100
    #t = timeit.Timer(stmt='find_first_number_not_summed_from_preamble(data, preamble_size=25)', globals=globals())
    #performance_result_ms = t.timeit(number=iterations) / iterations * 1000
    #print(f'{performance_result_ms=}ms')
    #
    #t = timeit.Timer(stmt='find_contiguous_set_for_sum(data, 1721308972)', globals=globals())
    #performance_result_ms = t.timeit(number=iterations) / iterations * 1000
    #print(f'{performance_result_ms=}ms')
