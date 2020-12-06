#!/usr/bin/env python3.8
from readers.generic import yield_blocks, yield_rstripped_and_joined_blocks


def part1() -> int:
    return sum([
        len(set(x)) for x in yield_rstripped_and_joined_blocks("data/day6_input.txt")
    ])


def part2() -> int:
    return sum([len(set.intersection(*[set(x) for x in group.split("\n")]))
                for group in yield_blocks("data/day6_input.txt")
                ])


if __name__ == "__main__":
    result = part1()
    print("Day6_Part1: found count: {}".format(result))

    result = part2()
    print("Day6_Part2: found count: {}".format(result))
