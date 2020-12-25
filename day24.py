#!/usr/bin/env python3.8
from core.hexalobby import HexaLobby
from readers.generic import read_and_rstrip


def part1() -> int:
    lobby = HexaLobby()
    tile_routes = read_and_rstrip("data/day24_input.txt")
    lobby.flip_tiles(tile_routes)
    return lobby.count_black_tiles()


def part2() -> int:
    lobby = HexaLobby()
    tile_routes = read_and_rstrip("data/day24_input.txt")
    lobby.flip_tiles(tile_routes)
    lobby.gol(times=100)
    return lobby.count_black_tiles()


if __name__ == "__main__":
    print("Day24_Part1: found count: {}".format(part1()))

    print("Day24_Part2: found count: {}".format(part2()))
