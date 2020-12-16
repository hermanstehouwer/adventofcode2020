from typing import List, Iterable, Dict


class Ticket:
    fields: List[int]

    def __init__(self, ticket: str):
        # 40,4,50
        self.fields = [int(x) for x in ticket.split(",")]


class TicketRule:
    label: str
    values: List[int]

    def __init__(self, rule: str):
        #class: 1-3 or 5-7
        self.label, vals = rule.split(": ")
        self.values = []
        for val in vals.split(" or "):
            f, t = val.split("-")
            self.values.extend(range(int(f), int(t)+1))


class TicketControl:
    tickets: List[Ticket]
    rules: List[TicketRule]
    own_ticket: Ticket

    def __init__(self, desc: Iterable[str]):
        self.tickets = []
        self.rules = []
        while (curr := next(desc)) != "":
            self.rules.append(TicketRule(curr))
        next(desc) #your ticket:
        self.own_ticket = Ticket(next(desc))

        next(desc)
        next(desc) # Nearby tickets
        for curr in desc:
            self.tickets.append(Ticket(curr))

    def calc_ser(self) -> int:
        totalcheck = []
        for rule in self.rules:
            totalcheck.extend(rule.values)
        totalcheck = set(totalcheck)
        sum = 0
        for ticket in self.tickets:
            for field in ticket.fields:
                if field not in totalcheck:
                    sum += field
        return sum

    def calc_departure_value(self) -> int:
        self.filter_tickets()
        self.order_rules()
        return self.multiply_departure()

    def filter_tickets(self):
        totalcheck = []
        for rule in self.rules:
            totalcheck.extend(rule.values)
        totalcheck = set(totalcheck)
        i = 0
        d = 0
        to_discard = []
        for ticket in self.tickets:
            i += 1
            for field in ticket.fields:
                if field not in totalcheck:
                    to_discard.append(ticket)
                    d += 1
        for ticket in to_discard:
            self.tickets.remove(ticket)

    def order_rules(self):
        new_rules_candidates: List[List[TicketRule]] = []
        for pos in range(len(self.own_ticket.fields)):
            new_rules_candidates.append([])
            for rule in self.rules:
                if all(t.fields[pos] in rule.values for t in self.tickets):
                    new_rules_candidates[pos].append(rule)
        new_rules: Dict[int, TicketRule] = {}
        while len(new_rules.keys()) < len(self.rules):
            # find rule
            pos = 0
            for i in range(len(new_rules_candidates)):
                if len(new_rules_candidates[i]) == 1:
                    pos = i
                    break
            new_rules[pos] = new_rules_candidates[pos][0]
            to_remove = new_rules[pos]
            # remove from all candidates
            for i in range(len(new_rules_candidates)):
                if to_remove in new_rules_candidates[i]:
                    new_rules_candidates[i].remove(to_remove)
        self.rules = []
        for i in range(len(new_rules.keys())):
            self.rules.append(new_rules[i])

    def multiply_departure(self) -> int:
        mult = 1
        for i in range(len(self.rules)):
            if self.rules[i].label.startswith("departure"):
                mult *= self.own_ticket.fields[i]
        return mult

