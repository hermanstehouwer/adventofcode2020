import re
from typing import List, Dict, Iterable, Tuple
import networkx as nx


class Bag:
    colour: str
    children: List
    counts: List
    parents: List

    def __init__(self, name: str):
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
            return add + sum(
                [a[0] * self.count_number_of_children(a[1].colour, add=1) for a in zip(cb.counts, cb.children)])
        return add


class BagTree2():
    G: nx.DiGraph
    EXTRACT_REGEX = re.compile("^(\d+) (.*) bags?\.?$")
    def __init__(self):
        self.G = nx.DiGraph()

    def create_node_if_needed(self, name: str):
        if name not in self.G.nodes:
            self.G.add_node(name)

    def parse_children(self, desc: str) -> Iterable[Tuple[int, Bag]]:
        if desc == "no other bags.":
            return
        for c in desc.split(", "):
            m = self.EXTRACT_REGEX.match(c)
            count = m.group(1)
            name = m.group(2)
            yield int(count), name

    def add_bags_from_line(self, line: str) -> None:
        parent, children = line.split(" bags contain ")
        self.create_node_if_needed(parent)
        for count, child_name in self.parse_children(children):
            self.create_node_if_needed(child_name)
            self.G.add_weighted_edges_from([(parent, child_name, count)])

    def get_list_of_parents(self, name: str) -> Iterable[str]:
        todo = [name]
        parents = []
        # Apparently the graph is a-cyclic. So not keeping track of visited nodes.
        while todo:
            current = todo.pop()
            for new_p in self.G.predecessors(current):
                if new_p not in parents:
                    parents.append(new_p)
                todo.append(new_p)
        return parents

    def count_number_of_children(self, name: str, add: int = 0) -> int:
        successors = self.G[name].keys()
        if len(list(successors)) > 0:
            ret = add + sum([self.G[name][child_name]['weight'] *
                              self.count_number_of_children(child_name, add=1)
                              for child_name in successors])
            return ret
        return add
