#!/usr/bin/env python3.8
from core.airplaine_seats import Seat
from readers.generic import read_and_rstrip


def part1():
    return max([Seat(boarding_pass).get_ID()
                for boarding_pass in read_and_rstrip("data/day5_input.txt")])


def part2():
    l = [Seat(boarding_pass).get_ID()
                for boarding_pass in read_and_rstrip("data/day5_input.txt")]
    l.sort()
    return list(set(range(min(l), max(l))).difference(l))[0]


if __name__ == "__main__":
    result = part1()
    print("Day5_Part1: found count: {}".format(result))

    result = part2()
    print("Day5_Part2: found count: {}".format(result))