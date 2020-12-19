import pytest
from typing import Iterable
from pytest import fixture
from core.message_validator import RuleSet


@fixture
def rule_set() -> RuleSet:
    a = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"'''
    yield RuleSet(a.split("\n"))


@fixture
def to_validate() -> Iterable[str]:
    a = """ababbb
bababa
abbbab
aaabbb
aaaabbb"""
    yield a.split("\n")


@fixture
def rule_set2():
    a = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1'''
    yield RuleSet(a.split("\n"))


@fixture
def rule_set2_patched():
    a = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1'''
    yield RuleSet(a.split("\n"), patch=True)

@fixture
def to_validate2():
    a = '''abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''
    yield a.split("\n")


def test_part1(rule_set: RuleSet, to_validate: Iterable[str]):
    assert sum(rule_set.validate(x) for x in to_validate) == 2


@pytest.mark.parametrize("to_validate",[
    pytest.param("bbabbbbaabaabba"),
    pytest.param("babbbbaabbbbbabbbbbbaabaaabaaa"),
    pytest.param("aaabbbbbbaaaabaababaabababbabaaabbababababaaa"),
    pytest.param("bbbbbbbaaaabbbbaaabbabaaa"),
    pytest.param("bbbababbbbaaaaaaaabbababaaababaabab"),
    pytest.param("ababaaaaaabaaab"),
    pytest.param("ababaaaaabbbaba"),
    pytest.param("baabbaaaabbaaaababbaababb"),
    pytest.param("abbbbabbbbaaaababbbbbbaaaababb"),
    pytest.param("aaaaabbaabaaaaababaa"),
    pytest.param("aaaabbaabbaaaaaaabbbabbbaaabbaabaaa"),
    pytest.param("aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba")
])
def test_specific_validation(to_validate, rule_set2_patched: RuleSet):
    assert rule_set2_patched.validate(to_validate)


def test_part2(rule_set2: RuleSet, rule_set2_patched: RuleSet, to_validate2: Iterable[str]):
    assert sum(rule_set2.validate(x) for x in to_validate2) == 3
    assert sum(rule_set2_patched.validate(x) for x in to_validate2) == 12
