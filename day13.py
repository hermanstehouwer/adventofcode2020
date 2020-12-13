#!/usr/bin/env python3.8
import timeit

from core.busservice import BusService
from readers.generic import read_and_rstrip


def part1() -> int:
    a, b = read_and_rstrip("data/day13_input.txt")
    time = int(a)
    busservice = BusService(b)
    bus = busservice.firstBusAfter(time)
    return bus.ID * bus.WaitTime(time)


def part2() -> int:
    a, b = read_and_rstrip("data/day13_input.txt")
    busservice = BusService(b)
    return busservice.specialtime()


if __name__ == "__main__":
    print("Day13_Part1: found count: {}".format(part1()))

    print("Day13_Part2: found count: {}".format(part2()))
