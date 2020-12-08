#!/usr/bin/env python3.8
from core.console import Console
from readers.generic import read_and_rstrip


def part1() -> int:
    console = Console(read_and_rstrip("data/day8_input.txt"))
    console.run_until_repeat_instruction()
    return console.current_value()


def part2() -> int:
    console = Console(read_and_rstrip("data/day8_input.txt"))
    console.try_jmpnoppatching_until_terminates_normally()
    return console.current_value()


if __name__ == "__main__":
    result = part1()
    print("Day8_Part1: found count: {}".format(result))

    result = part2()
    print("Day8_Part2: found count: {}".format(result))
