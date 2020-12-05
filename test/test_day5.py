import pytest
from core.airplaine_seats import *


@pytest.mark.parametrize("boardingpass, expected", [
    pytest.param("BFFFBBFRRR", 567),
    pytest.param("FFFBBBFRRR", 119),
    pytest.param("BBFFBBFRLL", 820),
])
def test_validators(boardingpass, expected):
    assert Seat(boardingpass).get_ID() == expected
