#!/usr/bin/env python3.8

from readers.read_lists import read_policystring_password
from core.passwords_and_policy import SledRentalPolicy, OfficialTobogganPolicy


def part1():
    counter = 0
    for (policy_str, password_str) in read_policystring_password("data/day2_input.txt"):
        if SledRentalPolicy(policy_str).check_password_against_policy(password_str):
            counter += 1
    return counter


def part2():
    counter = 0
    for (policy_str, password_str) in read_policystring_password("data/day2_input.txt"):
        if OfficialTobogganPolicy(policy_str).check_password_against_policy(password_str):
            counter += 1
    return counter


if __name__ == "__main__":
    result = part1()
    print("Day2_Part1: found count: {}".format(result))

    result = part2()
    print("Day2_Part2: found count: {}".format(result))
