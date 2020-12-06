from readers.generic import *


def test_part1():
    a = [
        len(set(x)) for x in yield_rstripped_and_joined_blocks("data/day6_test.txt")
    ]
    print(a)
    assert sum(a) == 11


def test_part2():
    sum = 0
    for group in yield_blocks("data/day6_test.txt"):
        sets = [set(x) for x in group.split("\n")]
        sum += len(sets[0].intersection(*sets))
    assert sum == 6