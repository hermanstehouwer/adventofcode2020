from pytest import fixture

from core.boating import manhattan, get_coordinates, action_to_direction, get_coordinates2


@fixture
def example_boating():
    a = """F10
N3
F7
R90
F11"""
    return a.split("\n")


def test_part1(example_boating):
    *_, last = get_coordinates(action_to_direction(example_boating))
    assert manhattan(0, 0, last[0], last[1]) == 25


def test_part2(example_boating):
    *_, last = get_coordinates2(example_boating)
    assert manhattan(0, 0, last[0], last[1]) == 286
