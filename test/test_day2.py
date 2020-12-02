import pytest
from core.passwords_and_policy import SledRentalPolicy, OfficialTobogganPolicy


@pytest.mark.parametrize("password_line, expected_outcome, PolicyClass", [
    pytest.param("1-3 a: abcde", True, SledRentalPolicy),
    pytest.param("1-3 b: cdefg", False, SledRentalPolicy),
    pytest.param("2-9 c: ccccccccc", True, SledRentalPolicy),
    pytest.param("1-3 a: abcde", True, OfficialTobogganPolicy),
    pytest.param("1-3 b: cdefg", False, OfficialTobogganPolicy),
    pytest.param("2-9 c: ccccccccc", False, OfficialTobogganPolicy)
])
def test_password_lines(password_line, expected_outcome, PolicyClass):
    policy_str, password = password_line.split(": ")
    p = PolicyClass(policy_str)
    assert p.check_password_against_policy(password) == expected_outcome
