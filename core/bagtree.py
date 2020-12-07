import re
from typing import List, Dict, Iterable, Tuple


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
        if p not in self.parents:
            self.parents.append(p)

    def hasChildren(self):
        return len(self.children) > 0


class BagTree:
    bags = Dict[str, Bag]
    EXTRACT_REGEX = re.compile("^(\d+) (.*) bags?\.?$")

    def __init__(self):
        self.bags = {}

    def get_or_create(self, name: str) -> Bag:
        if name not in self.bags:
            self.bags[name] = Bag(name)
        return self.bags[name]

    def get_or_create_children(self, desc: str) -> Iterable[Tuple[int, Bag]]:
        if desc == "no other bags.":
            return
        for c in desc.split(", "):
            m = self.EXTRACT_REGEX.match(c)
            count = m.group(1)
            name = m.group(2)
            yield int(count), self.get_or_create(name)

    def add_bags_from_line(self, line: str) -> None:
        parent, children = line.split(" bags contain ")
        p = self.get_or_create(parent)
        for count, c in self.get_or_create_children(children):
            p.addChild(c, count)
            c.addParent(p)

    def get_list_of_parents(self, name: str) -> Iterable[str]:
        todo = [self.bags[name]]
        parents = []
        # Apparently the graph is a-cyclic. So not keeping track of visited nodes.
        while todo:
            current = todo.pop()
            for new_p in current.parents:
                if new_p not in parents:
                    parents.append(new_p)
                todo.append(new_p)
        return [x.colour for x in parents]

    def count_number_of_children(self, name: str, add: int = 0) -> int:
        cb = self.bags[name]
        if cb.hasChildren():
            return add + sum([a[0]*self.count_number_of_children(a[1].colour, add=1) for a in zip(cb.counts, cb.children)])
        return add
