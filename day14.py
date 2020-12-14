#!/usr/bin/env python3.8
import timeit

from core.bitmask import BitMaskProcessor
from readers.generic import read_and_rstrip


def part1() -> int:
    processor = BitMaskProcessor()
    for line in read_and_rstrip("data/day14_input.txt"):
        processor.process_step(line)
    return processor.sum_of_values()


def part2() -> int:
    processor = BitMaskProcessor()
    for line in read_and_rstrip("data/day14_input.txt"):
        processor.process_step(line, mode2=True)
    return processor.sum_of_values()


if __name__ == "__main__":
    print("Day14_Part1: found count: {}".format(part1()))

    print("Day14_Part2: found count: {}".format(part2()))
