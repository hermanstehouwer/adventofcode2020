import pytest
from pytest import fixture
from core.passport import *
from readers.read_passports import passport_from_line


@fixture
def passports():
    def ret():
        yield passport_from_line("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm")
        yield passport_from_line("iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929")
        yield passport_from_line("hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm")
        yield passport_from_line("hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in")
    yield ret


@fixture
def invalid_passports():
    def ret():
        yield passport_from_line("eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926")
        yield passport_from_line("iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946")
        yield passport_from_line("hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277")
        yield passport_from_line("hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007")
    yield ret


@fixture
def valid_passports():
    def ret():
        yield passport_from_line("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f")
        yield passport_from_line("eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm")
        yield passport_from_line("hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022")
        yield passport_from_line("iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719")
        yield passport_from_line('pid:760899887 eyr:2023 hcl:#866857 hgt:185cm iyr:2017 byr:1976 ecl:gry')
    yield ret


@fixture
def one_valid_passport() -> Passport:
    yield passport_from_line("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f")


def test_passport_validity(passports):
    counter = sum([x.validate() for x in passports()])
    assert counter == 1


def test_passport_validity_ignore_cid(passports):
    counter = sum([x.validate(ignore="cid") for x in passports()])
    assert counter == 2


def test_invalid_passports(invalid_passports):
    for passport in invalid_passports():
        assert not passport.validate(ignore="cid", validate_values=True)


def test_valid_passports(valid_passports):
    for passport in valid_passports():
        assert passport.validate(ignore="cid", validate_values=True)


def test_one_valid(one_valid_passport):
    assert one_valid_passport.validate(ignore="cid", validate_values=True)


@pytest.mark.parametrize("function, field_value, expected", [
    # Birthyear
    pytest.param("byr", "2002", True),
    pytest.param("byr", "2003", False),
    pytest.param("byr", "1976", True),
    # Height
    pytest.param("hgt", "60in", True),
    pytest.param("hgt", "190cm", True),
    pytest.param("hgt", "190in", False),
    pytest.param("hgt", "190", False),
    pytest.param("hgt", "185cm", True),
    # Hair Colour
    pytest.param("hcl", "#123abc", True),
    pytest.param("hcl", "#123abz", False),
    pytest.param("hcl", "123abc", False),
    pytest.param("hcl", "#866857", True),
    # Eye Colour
    pytest.param("ecl", "brn", True),
    pytest.param("ecl", "wat", False),
    pytest.param("ecl", "gry", True),
    # PID
    pytest.param("pid", "000000001", True),
    pytest.param("pid", "0123456789", False),
    pytest.param("pid", "760899887", True)
])
def test_validators(function, field_value, expected):
    assert getattr(PassportValidator, function)(field_value) == expected
