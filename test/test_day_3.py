import pytest
from pytest import fixture
from readers.read_grid import create_grid
from core.Grid import *


@fixture
def test_grid():
    with open("test/data/day3_test.txt") as f:
        yield create_grid(f)


@pytest.mark.parametrize("coordinate, expected_griditem", [
    pytest.param(Coordinate(0, 0), GridItem.EMPTY),
    pytest.param(Coordinate(1, 3), GridItem.EMPTY),
    pytest.param(Coordinate(2, 6), GridItem.TREE)
])
def test_read_grid(test_grid: Grid, coordinate, expected_griditem):
    assert test_grid.get_at_coordinate(coordinate) == expected_griditem


@pytest.mark.parametrize("delta, expected_sum", [
    pytest.param(Coordinate(1, 1), 2),
    pytest.param(Coordinate(1, 3), 7),
    pytest.param(Coordinate(1, 5), 3),
    pytest.param(Coordinate(1, 7), 4),
    pytest.param(Coordinate(2, 1), 2),
])
def test_sum_part1(test_grid: Grid, delta, expected_sum):
    start = Coordinate(0, 0)
    maximum = test_grid.get_largest_coordinate()
    assert sum([test_grid.get_at_coordinate(c) for c in generate_coords(start, delta, maximum)]) == expected_sum
