import pytest
from pytest import fixture

from core import findsum

@fixture
def short_test_list():
    l = [1721,979,366,299,675,1456]
    yield l

@pytest.mark.parametrize("num_to_find, expected", [
    pytest.param(2, [1721, 299]),
    pytest.param(3, [979, 366, 675])
])
def test_day1_positive(short_test_list, num_to_find, expected):
    to_verify = findsum.find_inputs_that_sumto(short_test_list, 2020, num_to_find)
    for ev in expected:
        assert ev in to_verify


def test_day1_valueerror(short_test_list):
    with pytest.raises(ValueError):
        findsum.find_inputs_that_sumto(short_test_list, 0)
