from typing import Iterable

from pytest import fixture

from core.bitmask import BitMaskProcessor, BitMask


@fixture
def simple_program() -> Iterable[str]:
    a = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
    yield a.split("\n")

@fixture
def mode2_program() -> Iterable[str]:
    a = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
    yield a.split("\n")

@fixture
def processor() -> BitMaskProcessor:
    yield BitMaskProcessor()


def test_bitmask():
    bm1 = BitMask("XXXXXXXX")
    assert bm1.mask(0) == 0
    assert bm1.mask(12) == 12

    bm2 = BitMask("11111111")
    assert bm2.mask(0) == 255

    bm3 = BitMask("00000000")
    assert bm3.mask(123) == 0


def test_part1(simple_program: Iterable[str], processor: BitMaskProcessor):
    for line in simple_program:
        processor.process_step(line)
    assert processor.sum_of_values() == 165


def test_part2(mode2_program: Iterable[str], processor: BitMaskProcessor):
    for line in mode2_program:
        processor.process_step(line, mode2=True)
    assert processor.sum_of_values() == 208