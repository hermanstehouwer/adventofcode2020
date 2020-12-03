#!/usr/bin/env python3.8
import math
from typing import Iterable
from readers.read_grid import create_grid
from core.Grid import Coordinate, Grid, generate_coords


def part1():
    with open("data/day3_input.txt") as f:
        grid = create_grid(f)
    start = Coordinate(0, 0)
    delta = Coordinate(1, 3)
    maximum = grid.get_largest_coordinate()
    return sum([grid.get_at_coordinate(c) for c in generate_coords(start, delta, maximum)])


def deltas() -> Iterable[Coordinate]:
    yield Coordinate(1, 1)
    yield Coordinate(1, 3)
    yield Coordinate(1, 5)
    yield Coordinate(1, 7)
    yield Coordinate(2, 1)


def part2():
    with open("data/day3_input.txt") as f:
        grid = create_grid(f)
    start = Coordinate(0, 0)
    maximum = grid.get_largest_coordinate()
    return math.prod([
            sum([
                    grid.get_at_coordinate(c) for c in generate_coords(start, delta, maximum)
                ]) for delta in deltas()
        ])


if __name__ == "__main__":
    result = part1()
    print("Day3_Part1: found count: {}".format(result))

    result = part2()
    print("Day3_Part2: found count: {}".format(result))
