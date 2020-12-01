#!/usr/bin/env python3.8
import timeit

from readers.read_lists import read_list_ints
from core.findsum import find_inputs_that_sumto
import math

def both(number_of_inputs:int = 2):
    with read_list_ints("data/day1_input.txt") as intlist:
        sumto = find_inputs_that_sumto(intlist, 2020, number_of_inputs)
        return sumto, math.prod(sumto)


def part1():
    return both(2)


def part2():
    return both(3)


def totime():
    part1()
    part2()


if __name__ == "__main__":
    result = part1()
    print("Day1_Part1: found tuple: {} that multiplies to: {}".format(result[0], result[1]))
    result = part2()
    print("Day1_Part2: found tuple: {} that multiplies to: {}".format(result[0], result[1]))

    # t = timeit.Timer(totime)
    # print(t.timeit(number=100)/100)
    # Note: produces a value of 0.194.... on my machine for day1 and day2 together.
