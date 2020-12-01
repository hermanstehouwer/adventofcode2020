#!/usr/bin/env python3.8
import timeit

from readers.read_lists import read_list_ints
from core.findsum import find_inputs_that_sumto
import math


def both(number_of_inputs:int = 2):
    with read_list_ints("data/day1_input.txt") as intlist:
        result = find_inputs_that_sumto(intlist, 2020, number_of_inputs)
        return result, math.prod(result)


def part1():
    return both(2)


def part2():
    return both(3)


if __name__ == "__main__":
    result = part1()
    print("Day1_Part1: found tuple: {} that multiplies to: {}".format(result[0], result[1]))
    result = part2()
    print("Day1_Part2: found tuple: {} that multiplies to: {}".format(result[0], result[1]))

    # timing part2 without IO
    with read_list_ints("data/day1_input.txt") as intlist:
        t = timeit.Timer('find_inputs_that_sumto(intlist, 2020, 3)', globals=globals())
        n = 100
        print(sum(t.repeat(repeat=n, number=1)) / n)
