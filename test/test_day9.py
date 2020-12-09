from pytest import fixture
import numpy as np
from core.XMASencoding import find_first_number_not_summed_from_preamble, find_contiguous_set_for_sum

@fixture
def test_data():
    a = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
    yield [int(x) for x in a.split("\n")]


def test_part1(test_data):
    assert find_first_number_not_summed_from_preamble(test_data, preamble_size=5) == 127


def test_part2(test_data):
    answer = find_contiguous_set_for_sum(test_data, 127)
    print(answer)
    assert (min(answer) + max(answer)) == 62
