#!/usr/bin/env python3.8
from typing import Iterable
from core.gol import GoL


def initial_state() -> Iterable[str]:
    a = """..#..#.#
##.#..#.
#....#..
.#..####
.....#..
...##...
.#.##..#
.#.#.#.#"""
    return a.split("\n")


def get_GoL(extra_dim: bool = False) -> GoL:
    return GoL(initial_state(), extra_dim=extra_dim)


def part1() -> int:
    gol = get_GoL()
    gol.boot()
    return gol.count_active()


def part2() -> int:
    gol = get_GoL(extra_dim=True)
    gol.boot()
    return gol.count_active()


if __name__ == "__main__":
    print("Day17_Part1: found count: {}".format(part1()))

    print("Day17_Part2: found count: {}".format(part2()))
