import copy
from typing import Dict, Iterable, List, Tuple, Set
from pyformlang.cfg import Production, Variable, Terminal, CFG, Epsilon


class RuleSet:
    rules: CFG

    def __init__(self, rules: Iterable[str], patch: bool = False):
        start_var: Variable
        vars: set[Variable] = set()
        terminals: Set[Terminal] = set()
        productions: Set[Production] = set()

        for rule in rules:
            i, r = rule.split(": ")
            var = Variable(i)
            if i == "0":
                start_var = var
            if r[0] == '"':
                ter = Terminal(r[1])
                terminals.add(ter)
                productions.add(Production(var, [ter]))
                continue
            if patch:
                if i == "8":
                    r = "42 | 42 8"
                if i == "11":
                    r = "42 31 | 42 11 31"
            rr = r.split(" | ")
            for r in rr:
                productions.add(Production(var, [Variable(x) for x in r.split(" ")]))

        self.CFG = CFG(vars, terminals, start_var, productions)

    def validate(self, to_validate: str) -> bool:
        return self.CFG.contains(to_validate)
