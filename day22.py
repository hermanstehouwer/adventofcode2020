#!/usr/bin/env python3.8

from core.spacecards import CardGame
from readers.generic import yield_blocks


def part1() -> int:
    game = CardGame(yield_blocks("data/day22_input.txt"))
    game.play()
    return game.get_winning_score()


def part2() -> int:
    game = CardGame(yield_blocks("data/day22_input.txt"))
    game.play_recursive()
    return game.get_winning_score()

if __name__ == "__main__":
    print("Day22_Part1: found count: {}".format(part1()))

    print("Day22_Part2: found count: {}".format(part2()))
