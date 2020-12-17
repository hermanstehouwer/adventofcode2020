from typing import Iterable
from pytest import fixture

from core.gol import GoL


@fixture
def initial_state() -> Iterable[str]:
    a = """.#.
..#
###"""
    yield a.split("\n")

@fixture
def initial_gol(initial_state: Iterable[str]) -> GoL:
    yield GoL(initial_state)


def test_part1(initial_gol: GoL):
    initial_gol.boot()
    assert initial_gol.count_active() == 112


def test_part2(initial_gol: GoL):
    initial_gol.extra_dim = True
    initial_gol.boot()
    assert initial_gol.count_active() == 848
