from pytest import fixture

from core import findsum

@fixture
def short_test_list():
    l = [1721,979,366,299,675,1456]
    yield l


def test_day1_part1(short_test_list):
    to_verify = findsum.find_inputs_that_sumto(short_test_list, 2020)
    assert 1721 in to_verify
    assert 299 in to_verify


def test_day1_part2(short_test_list):
    to_verify = findsum.find_inputs_that_sumto(short_test_list, 2020, 3)
    assert 979 in to_verify
    assert 366 in to_verify
    assert 675 in to_verify

