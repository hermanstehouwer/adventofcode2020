#!/usr/bin/env python3.8

from core.mathing import process_operator_precedence_lr, process_operator_precedence_add_first
from readers.generic import read_and_rstrip


def part1() -> int:
    return sum(process_operator_precedence_lr(line) for line in read_and_rstrip("data/day18_input.txt"))


def part2() -> int:
    return sum(process_operator_precedence_add_first(line) for line in read_and_rstrip("data/day18_input.txt"))


if __name__ == "__main__":
    print("Day18_Part1: found count: {}".format(part1()))

    print("Day18_Part2: found count: {}".format(part2()))
