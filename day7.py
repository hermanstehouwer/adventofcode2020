#!/usr/bin/env python3.8
from core.bagtree import BagTree
from readers.generic import yield_blocks, yield_rstripped_and_joined_blocks, read_and_rstrip


def part1() -> int:
    bt = BagTree()
    for line in read_and_rstrip("data/day7_input.txt"):
        bt.add_bags_from_line(line)
    parents = bt.get_list_of_parents("shiny gold")
    return len(parents)


def part2() -> int:
    bt = BagTree()
    for rule in read_and_rstrip("data/day7_input.txt"):
        bt.add_bags_from_line(rule)
    return bt.count_number_of_children("shiny gold") - 1

if __name__ == "__main__":
    result = part1()
    print("Day6_Part1: found count: {}".format(result))

    result = part2()
    print("Day6_Part2: found count: {}".format(result))
