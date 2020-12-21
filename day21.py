#!/usr/bin/env python3.8
from typing import Tuple, Iterable

from core.allergens import find_ingredients_without_allergens, find_dangerous_ingredients
from readers.generic import read_and_rstrip


def part1() -> int:
    return len(find_ingredients_without_allergens(read_and_rstrip("data/day21_input.txt")))


def part2() -> str:
    todo = find_dangerous_ingredients(read_and_rstrip("data/day21_input.txt"))
    return ','.join(todo)


if __name__ == "__main__":
    print("Day21_Part1: found count: {}".format(part1()))

    print("Day21_Part2: found count: {}".format(part2()))
