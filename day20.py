#!/usr/bin/env python3.8
from typing import Tuple, Iterable

from core.jigsaw import Tile, JigSaw
from readers.generic import yield_blocks


def part1() -> int:
    tiles = []
    for tile_desc in yield_blocks("data/day20_input.txt"):
        tiles.append(Tile(tile_desc))
    jigsaw = JigSaw(tiles)
    return jigsaw.mult_corners()


def part2() -> int:
    tiles = []
    for tile_desc in yield_blocks("data/day20_input.txt"):
        tiles.append(Tile(tile_desc))
    jigsaw = JigSaw(tiles)
    jigsaw.mult_corners()
    jigsaw.puzzles()
    return jigsaw.leftover_hash()


if __name__ == "__main__":
    print("Day20_Part1: found count: {}".format(part1()))

    print("Day20_Part2: found count: {}".format(part2()))
