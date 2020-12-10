from pytest import fixture

from core.jolts import get_jolt_differences, get_number_of_arrangements


@fixture
def example_jolts1():
    a = """16
10
15
5
1
11
7
19
6
12
4"""
    return [int(x) for x in a.split("\n")]


@fixture
def example_jolts2():
    a = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
    return [int(x) for x in a.split("\n")]


def test_differences1(example_jolts1):
    counts = get_jolt_differences(example_jolts1)
    assert counts.get(1, 0) == 7
    assert counts.get(3, 0) == 5


def test_differences2(example_jolts2):
    counts = get_jolt_differences(example_jolts2)
    assert counts.get(1, 0) == 22
    assert counts.get(3, 0) == 10


def test_arrangements(example_jolts1, example_jolts2):
    assert get_number_of_arrangements(example_jolts1) == 8
    assert get_number_of_arrangements(example_jolts2) == 19208
