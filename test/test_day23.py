import pytest

from core.crabcups import CrabCups


@pytest.mark.parametrize("moves, expected",[
    pytest.param(10, "92658374"),
    pytest.param(100, "67384529")
])
def test_part1(moves, expected):
    cups = [3,8,9,1,2,5,4,6,7]
    cc = CrabCups(cups)
    cc.game(moves=moves)
    assert cc.get_label() == expected


@pytest.mark.skip(reason="takes several seconds to run, so slows down test suite.")
def test_part2():
    cups = [3,8,9,1,2,5,4,6,7]
    cc = CrabCups(cups, expand=True)
    cc.game(moves=10000000)
    assert cc.mult_next_to_one() == 149245887792
