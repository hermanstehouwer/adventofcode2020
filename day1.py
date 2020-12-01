#!/usr/bin/env python3.8

from readers.read_lists import read_list_ints
from core.findsum import find_inputs_that_sumto
import math


def part1():
    with read_list_ints("data/day1_input.txt") as intlist:
        sumto = find_inputs_that_sumto(intlist, 2020)
        print("Day1_Part1: found tuple: {} that multiplies to: {}".format(sumto, sumto[0]*sumto[1]))


def part2():
    with read_list_ints("data/day1_input.txt") as intlist:
        sumto = find_inputs_that_sumto(intlist, 2020, 3)
        print("Day1_Part1: found tuple: {} that multiplies to: {}".format(sumto, math.prod(sumto)))


if __name__ == "__main__":
    part1()
    part2()
