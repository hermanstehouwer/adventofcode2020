#!/usr/bin/env python3.8
from core.crabcups import CrabCups


def part1() -> int:
    cups = [7,8,4,2,3,5,9,1,6]
    cc = CrabCups(cups)
    cc.game(moves=100)
    return cc.get_label()


def part2() -> int:
    cups = [7,8,4,2,3,5,9,1,6]
    cc = CrabCups(cups, expand=True)
    cc.game(moves=10000000)
    return cc.mult_next_to_one()

if __name__ == "__main__":
    print("Day23_Part1: found count: {}".format(part1()))

    # performance_result_ms=25675.129059600004ms
    print("Day23_Part2: found count: {}".format(part2()))