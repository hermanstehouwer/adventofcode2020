#!/usr/bin/env python3.8
import timeit

from core.jolts import get_jolt_differences, get_number_of_arrangements
from readers.generic import read_and_rstrip
from readers.read_grid import create_grid, simulate_seating_until_done


def part1() -> int:
    grid = create_grid(read_and_rstrip("data/day11_input.txt"))
    return simulate_seating_until_done(grid)


def part2() -> int:
    grid = create_grid(read_and_rstrip("data/day11_input.txt"))
    return simulate_seating_until_done(grid, lookfurther=True)

if __name__ == "__main__":
    #print("Day11_Part1: found count: {}".format(part1()))

    print("Day11_Part2: found count: {}".format(part2()))

    #data = [int(x) for x in read_and_rstrip("data/day9_input.txt")]
    #iterations = 100
    #t = timeit.Timer(stmt='find_first_number_not_summed_from_preamble(data, preamble_size=25)', globals=globals())
    #performance_result_ms = t.timeit(number=iterations) / iterations * 1000
    #print(f'{performance_result_ms=}ms')
    #
    #t = timeit.Timer(stmt='find_contiguous_set_for_sum(data, 1721308972)', globals=globals())
    #performance_result_ms = t.timeit(number=iterations) / iterations * 1000
    #print(f'{performance_result_ms=}ms')
