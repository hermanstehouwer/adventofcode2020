import pytest

from core.memory_game import take_turns


@pytest.mark.parametrize("start_sequence, expected", [
    pytest.param([1,3,2], 1),
    pytest.param([2,1,3], 10),
    pytest.param([1,2,3], 27),
    pytest.param([2,3,1], 78),
    pytest.param([3,2,1], 438),
    pytest.param([3,1,2], 1836),
])
def test_part1(start_sequence, expected):
    assert next(x for i,x in enumerate(take_turns(start_sequence)) if i==2019) == expected
