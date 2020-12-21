#!/usr/bin/env python3.8
from typing import Tuple, Iterable

from core.message_validator import RuleSet
from readers.generic import yield_blocks
import regex


def get_stuff(patch: bool = False) -> Tuple[RuleSet, Iterable[str]]:
    a, b = yield_blocks("data/day19_input.txt")
    rs = RuleSet(a.split("\n"), patch=patch)
    to_v = b.split("\n")
    return rs, to_v


def part1() -> int:
    rule_set, to_validate = get_stuff()
    return sum(rule_set.validate(x) for x in to_validate)


def part2() -> int:
    rule_set, to_validate = get_stuff(patch=True)
    return sum(rule_set.validate(x) for x in to_validate)


if __name__ == "__main__":
    print("Day19_Part1: found count: {}".format(part1()))

    print("Day19_Part2: found count: {}".format(part2()))