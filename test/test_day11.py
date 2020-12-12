from pytest import fixture

from readers.read_grid import create_grid, simulate_seating_until_done


@fixture
def seatgrid():
    layout = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    yield create_grid(layout.split("\n"))

def test_test(seatgrid):
    assert simulate_seating_until_done(seatgrid) == 37


def test_part2(seatgrid):
    assert simulate_seating_until_done(seatgrid, lookfurther=True) == 26
