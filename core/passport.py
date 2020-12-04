import re
from typing import Dict


class PassPort:
    REQUIRED_FIELDS = {}

    fields: Dict[str, str]
    valid: bool = True

    @staticmethod
    def _validate_height(field) -> bool:
        if not re.match("^[0-9]+(cm|in)$", field):
            return False
        ln = int(field[0:-2])
        unit = field[-2:]
        return 150 <= ln <= 193 if unit == "cm" \
            else 59 <= ln <= 76

    def _validate_fields(self) -> bool:
        for (k, v) in self.fields.items():
            if not self.REQUIRED_FIELDS[k](v):
                return False
        return True

    def validate(self, ignore="None", validate_values=False) -> bool:
        for field in self.REQUIRED_FIELDS.keys():
            if field not in self.fields and field != ignore:
                return False
        if validate_values:
            return self._validate_fields()
        return True


PassPort.REQUIRED_FIELDS = {
    "byr": lambda k: 1920 <= int(k) <= 2002,
    "iyr": lambda k: 2010 <= int(k) <= 2020,
    "eyr": lambda k: 2020 <= int(k) <= 2030,
    "hgt": PassPort._validate_height,
    "hcl": lambda k: re.match("^#[0-9a-f]{6}$", k) != None,
    "ecl": lambda k: k in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda k: k.isnumeric() and len(k) == 9,
    "cid": lambda k: True
}
