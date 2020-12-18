import math
import re
from typing import List

MATCH_PARENTHESES = re.compile(r".*(?P<in_paren>\(.*?\)).*")


def process_operator_precedence_lr(tomath: str) -> int:
    while m := MATCH_PARENTHESES.match(tomath):
        s, e = m.span('in_paren')
        toprocess = m.group('in_paren')[1:-1]
        tomath = tomath[:s] + str(process_operator_precedence_lr(toprocess)) + tomath[e:]

    to_calc: List[str] = tomath.split(" ")
    while len(to_calc) > 1:
        a = int(to_calc.pop(0))
        op = to_calc.pop(0)
        b = int(to_calc.pop(0))
        result = a + b
        if op == "*":
            result = a * b
        to_calc.insert(0, str(result))

    return int(to_calc[0])


def process_operator_precedence_add_first(tomath: str) -> int:
    while m := MATCH_PARENTHESES.match(tomath):
        s, e = m.span('in_paren')
        toprocess = m.group('in_paren')[1:-1]
        tomath = tomath[:s] + str(process_operator_precedence_add_first(toprocess)) + tomath[e:]

    split_sum = tomath.split(" * ")
    if len(split_sum) > 1:
        return math.prod(process_operator_precedence_add_first(x) for x in split_sum)

    split_add = split_sum[0].split(" + ")
    if len(split_add) > 1:
        return sum(process_operator_precedence_add_first(x) for x in split_add)

    return int(split_add[0])
