from pytest import fixture

from core.console import Console


@fixture
def example_program():
    a = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    yield a.split("\n")


def test_part1(example_program):
    console = Console(example_program)
    console.run_until_repeat_instruction()
    assert console.current_value() == 5


def test_part2(example_program):
    console = Console(example_program)
    console.try_jmpnoppatching_until_terminates_normally()
    assert console.current_value() == 8
