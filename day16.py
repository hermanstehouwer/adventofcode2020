#!/usr/bin/env python3.8
import timeit

from core.bitmask import BitMaskProcessor
from core.traintickets import TicketControl
from readers.generic import read_and_rstrip


def part1() -> int:
    control = TicketControl(read_and_rstrip("data/day16_input.txt"))
    return control.calc_ser()


def part2() -> int:
    control = TicketControl(read_and_rstrip("data/day16_input.txt"))
    return control.calc_departure_value()

if __name__ == "__main__":
    print("Day16_Part1: found count: {}".format(part1()))

    print("Day16_Part2: found count: {}".format(part2()))
