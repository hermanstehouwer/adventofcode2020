import re
from typing import List, Dict


class Bag:
    colour: str
    children: List
    counts: List
    parents: List

    def __init__(self, name:str):
        self.colour = name
        self.children = []
        self.counts = []
        self.parents = []

    def addChild(self, c, count):
        if c not in self.children:
            self.children.append(c)
            self.counts.append(count)

    def addParent(self, p):
        print(f"adding parent [{p.colour}] to [{self.colour}]")
        if p not in self.parents:
            self.parents.append(p)

    def hasChildren(self):
        return len(self.children) > 0


class BagTree:
    bags = Dict[str, Bag]
    EXTRACT_REGEX = re.compile("^(\d+) (.*) bags?\.?$")

    def __init__(self):
        self.bags = {}

    def get_or_create(self, name:str):
        if name not in self.bags:
            newbag = Bag(name)
            self.bags[name] = newbag
        return self.bags[name]

    def get_or_create_children(self, desc:str):
        if desc == "no other bags.":
            return
        for c in desc.split(", "):
            m = self.EXTRACT_REGEX.match(c)
            count = m.group(1)
            name = m.group(2)
            yield int(count), self.get_or_create(name)

    def add_bags_from_line(self, line:str):
        parent, children = line.split(" bags contain ")
        p = self.get_or_create(parent)
        for count, c in self.get_or_create_children(children):
            p.addChild(c, count)
            c.addParent(p)

    def get_list_of_parents(self, name:str):
        todo = [self.bags[name]]
        done = []
        parents = []
        while todo:
            current = todo.pop()
            for new_p in current.parents:
                if new_p not in parents:
                    parents.append(new_p)
                if new_p not in done:
                    todo.append(new_p)
            done.append(current)
        return [x.colour for x in parents]

    def count_number_of_children(self, name: str) -> int:
        cb = self.bags[name]
        if cb.hasChildren():
            ret = 1+ sum([a[0]*self.count_number_of_children(a[1].colour) for a in zip(cb.counts, cb.children)])
            print(f"{cb.colour} has {cb.counts} children for value: {ret}")
            return ret
        return 1
