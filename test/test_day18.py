import pytest

from core.mathing import process_operator_precedence_lr, process_operator_precedence_add_first


@pytest.mark.parametrize("expression, expected", [
    pytest.param("1 + (2 * 3) + (4 * (5 + 6))", 51),
    pytest.param("2 * 3 + (4 * 5)", 26),
    pytest.param("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
    pytest.param("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
    pytest.param("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632)
])
def test_part1(expression, expected):
    assert process_operator_precedence_lr(expression) == expected

@pytest.mark.parametrize("expression, expected", [
    pytest.param("1 + (2 * 3) + (4 * (5 + 6))", 51),
    pytest.param("2 * 3 + (4 * 5)", 46),
    pytest.param("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
    pytest.param("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
    pytest.param("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340)
])
def test_part2(expression, expected):
    assert process_operator_precedence_add_first(expression) == expected
