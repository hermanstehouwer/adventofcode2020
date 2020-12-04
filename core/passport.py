import re
from typing import Dict, Iterator


class PassportValidator:
    @staticmethod
    def byr(field_value: str) -> bool:
        return 1920 <= int(field_value) <= 2002

    @staticmethod
    def iyr(field_value: str) -> bool:
        return 2010 <= int(field_value) <= 2020

    @staticmethod
    def eyr(field_value: str) -> bool:
        return 2020 <= int(field_value) <= 2030

    @staticmethod
    def hgt(field_value: str) -> bool:
        if not re.match("^[0-9]+(cm|in)$", field_value):
            return False
        ln = int(field_value[0:-2])
        unit = field_value[-2:]
        return (150 <= ln <= 193 and unit == "cm") ^ \
               (59 <= ln <= 76 and unit == "in")

    @staticmethod
    def hcl(field_value: str) -> bool:
        return re.match("^#[0-9a-f]{6}$", field_value) is not None

    @staticmethod
    def ecl(field_value: str) -> bool:
        return field_value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    @staticmethod
    def pid(field_value: str) -> bool:
        return field_value.isnumeric() and len(field_value) == 9

    @staticmethod
    def cid(field_value: str) -> bool:
        return True

    @staticmethod
    def _get_fields() -> Iterator[str]:
        return [x for x in dir(PassportValidator) if not x.startswith("_")]


class Passport:
    fields: Dict[str, str]

    def _validate_fields(self) -> bool:
        for (k, v) in self.fields.items():
            if not getattr(PassportValidator, k)(v):
                return False
        return True

    def validate(self, ignore="None", validate_values=False) -> bool:
        for field in PassportValidator._get_fields():
            if field not in self.fields and field != ignore:
                return False
        if validate_values and not self._validate_fields():
            return False
        return True
