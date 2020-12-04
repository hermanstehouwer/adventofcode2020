#!/usr/bin/env python3.8
from readers.read_passports import make_passports


def part1():
    return sum([p.validate(ignore="cid") for p in make_passports("data/day4_input.txt")])


def part2():
    return sum([p.validate(ignore="cid", validate_values=True) for p in make_passports("data/day4_input.txt")])


if __name__ == "__main__":
    result = part1()
    print("Day4_Part1: found count: {}".format(result))

    result = part2()
    print("Day4_Part2: found count: {}".format(result))
