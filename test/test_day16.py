from pytest import fixture

from core.traintickets import TicketControl


@fixture
def ticket():
    a = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
    yield a.split("\n")


def test_error_rate(ticket):
    control = TicketControl(iter(ticket))
    assert control.calc_ser() == 71
