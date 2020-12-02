import pytest

from core.passwords_and_policy import SledRentalPolicy, OfficialTobogganPolicy, PasswordPolicy


@pytest.mark.parametrize("password_line, expected_outcome_sled, expected_outcome_toboggan", [
    pytest.param("1-3 a: abcde", True, True),
    pytest.param("1-3 b: cdefg", False, False),
    pytest.param("2-9 c: ccccccccc", True, False)
])
def test_password_lines(password_line, expected_outcome_sled, expected_outcome_toboggan):
    policy_str, password = password_line.split(": ")
    assert SledRentalPolicy(policy_str).check_password_against_policy(password) == expected_outcome_sled
    assert OfficialTobogganPolicy(policy_str).check_password_against_policy(password) == expected_outcome_toboggan
