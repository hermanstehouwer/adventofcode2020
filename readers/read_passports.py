from typing import Iterable

from core.passport import PassPort


def passport_from_line(line: str) -> PassPort:
    passport = PassPort()
    passport.fields = {}
    for item in line.split(" "):
        key, value = item.split(":")
        passport.fields[key] = value
    return passport


def make_passports(filename: str) -> Iterable[PassPort]:
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
