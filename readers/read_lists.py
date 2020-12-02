from contextlib import contextmanager
from typing import Tuple


@contextmanager
def read_list_ints_sorted(filename: str):
    with open(filename) as f:
        data = f.readlines()
    data = [int(x) for x in data]
    data.sort()
    yield data


def read_policystring_password(filename: str) -> Tuple[str, str]:
    with open(filename) as f:
        for line in f:
            policy_str, password = line.split(": ")
            yield policy_str, password
