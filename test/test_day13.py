import pytest
from pytest import fixture

from core.busservice import BusService, Bus


@fixture
def time_and_busservice():
    a = 939
    b = "7,13,x,x,59,x,31,19"
    yield a, BusService(b)


def test_earliest_departure(time_and_busservice):
    time, busservice = time_and_busservice
    bus = busservice.firstBusAfter(time)
    assert bus.ID == 59
    assert bus.WaitTime(time) == 5


@pytest.mark.parametrize("busservice, expected",[
    pytest.param(BusService("7,13,x,x,59,x,31,19"), 1068781),
    pytest.param(BusService("17,x,13,19"), 3417),
    pytest.param(BusService("67,7,59,61"), 754018),
    pytest.param(BusService("67,x,7,59,61"), 779210),
    pytest.param(BusService("67,7,x,59,61"), 1261476),
    pytest.param(BusService("1789,37,47,1889"), 1202161486)
])
def test_find_special_time(busservice: BusService, expected: int):
    assert busservice.specialtime() == expected
