#!/usr/bin/env python3.8
from typing import List

from core.airplaine_seats import Seat
from readers.generic import read_and_rstrip


def get_seat_IDs() -> List[int]:
    return [Seat(boarding_pass).ID
                for boarding_pass in read_and_rstrip("data/day5_input.txt")]


def part1() -> int:
    return max(get_seat_IDs())


def part2():
    seats = get_seat_IDs()
    return [seat_id
            for seat_id in range(min(seats), max(seats))
            if seat_id not in seats
            ].pop()


if __name__ == "__main__":
    result = part1()
    print("Day5_Part1: found count: {}".format(result))

    result = part2()
    print("Day5_Part2: found count: {}".format(result))