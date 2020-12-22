import pytest
from pytest import fixture

from core.spacecards import CardGame


@fixture
def cards_description():
    a = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""
    yield a.split("\n\n")


@fixture
def cardgame(cards_description) -> CardGame:
    yield CardGame(cards_description)


def test_part1(cardgame: CardGame):
    cardgame.play()
    assert cardgame.get_winning_score() == 306


def test_part2(cardgame: CardGame):
    cardgame.play_recursive()
    assert cardgame.get_winning_score() == 291
