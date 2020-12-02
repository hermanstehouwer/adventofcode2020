#!/usr/bin/env python3.8
from typing import List

from readers.read_lists import read_policystring_password
from core.passwords_and_policy import SledRentalPolicy, OfficialTobogganPolicy, PasswordPolicy


def generate_for_passwordpolicy(policy: PasswordPolicy.__class__) -> List[bool]:
    for (policy_str, password_str) in read_policystring_password("data/day2_input.txt"):
        yield policy(policy_str).check_password_against_policy(password_str)


def part1():
    return sum(generate_for_passwordpolicy(SledRentalPolicy))


def part2():
    return sum(generate_for_passwordpolicy(OfficialTobogganPolicy))


if __name__ == "__main__":
    result = part1()
    print("Day2_Part1: found count: {}".format(result))

    result = part2()
    print("Day2_Part2: found count: {}".format(result))
