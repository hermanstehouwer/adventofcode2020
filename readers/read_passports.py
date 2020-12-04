from typing import Iterable

from core.passport import Passport


def passport_from_line(line: str) -> Passport:
    passport = Passport()
    passport.fields = dict([field.split(":") for field in line.split()])
    return passport


def make_passports(filename: str) -> Iterable[Passport]:
    with open(filename) as f:
        for passport in f.read().split("\n\n"):
            yield passport_from_line(" ".join(passport.split("\n")))
