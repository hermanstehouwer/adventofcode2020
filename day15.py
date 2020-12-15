#!/usr/bin/env python3.8
from core.memory_game import take_turns


def part1() -> int:
    return next(x for i, x in enumerate(take_turns([11,18,0,20,1,7,16])) if i==2019)


def part2() -> int:
    return next(x for i, x in enumerate(take_turns([11,18,0,20,1,7,16])) if i==(30000000-1))



if __name__ == "__main__":
    print("Day15_Part1: found count: {}".format(part1()))

    print("Day15_Part2: found count: {}".format(part2()))
