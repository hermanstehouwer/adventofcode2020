#!/usr/bin/env python3.8
from core.encryption import get_loop_size, get_encryption_key


def part1() -> int:
    loop_size = get_loop_size(9093927)
    encryption_key = get_encryption_key(11001876, loop_size)
    return encryption_key


if __name__ == "__main__":
    print("Day25_Part1: found count: {}".format(part1()))
