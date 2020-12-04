from typing import Iterable

from core.passport import Passport


def passport_from_line(line: str) -> Passport:
    passport = Passport()
    passport.fields = dict([field.split(":") for field in line.split()])
    return passport


def make_passports(filename: str) -> Iterable[Passport]:
    passports = []
    passport_lines = []
    with open(filename) as f:
        while line := f.readline():
            line = line.rstrip()
            if line == "":
                yield passport_from_line(" ".join(passport_lines))
                passport_lines = []
            else:
                passport_lines.append(line)
    # last line of the file is not empty
    yield passport_from_line(" ".join(passport_lines))
