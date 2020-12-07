#!/usr/bin/env python3.8
from core.bagtree import BagTree
from readers.generic import read_and_rstrip


def get_bagtree() -> BagTree:
    bt = BagTree()
    for line in read_and_rstrip("data/day7_input.txt"):
        bt.add_bags_from_line(line)
    return bt


def part1() -> int:
    bt = get_bagtree()
    parents = bt.get_list_of_parents("shiny gold")
    return len(parents)


def part2() -> int:
    bt = get_bagtree()
    return bt.count_number_of_children("shiny gold")


if __name__ == "__main__":
    result = part1()
    print("Day7_Part1: found count: {}".format(result))

    result = part2()
    print("Day7_Part2: found count: {}".format(result))
