from typing import List, Dict, Iterable
import itertools

import networkx as nx


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def get_jolt_differences(jolts: List[int]) -> Dict[int, int]:
    jolts.append(0)
    jolts.append(max(jolts) + 3)
    return get_difference_counts(jolts)


def get_difference_counts(jolts: List[int]) -> Dict[int, int]:
    jolts.sort()
    out = {}
    for a, b in pairwise(jolts):
        difference = b - a
        out[difference] = out.get(difference, 0) + 1
    return out


def jolts_to_graph(jolts: List[int]) -> nx.DiGraph:
    G = nx.DiGraph()
    for n in jolts:
        G.add_node(n)
    for index_a in range(len(jolts)-1):
        for index_b in range(index_a+1, len(jolts)):
            if jolts[index_b] - jolts[index_a] <= 3:
                G.add_edge(jolts[index_a], jolts[index_b])
            else:
                break
    return G


def splitjolts(jolts: List[int]) -> Iterable[List[int]]:
    to_yield = []
    while jolts:
        to_yield.append(jolts.pop(0))
        if not jolts or jolts[0] - to_yield[-1] == 3:
            yield to_yield
            to_yield = []


def get_number_of_arrangements(jolts: List[int]) -> int:
    jolts.append(0)
    jolts.append(max(jolts) + 3)
    jolts.sort()
    total = 1
    for subjolts in splitjolts(jolts):
        G = jolts_to_graph(subjolts)
        summed = sum(1 for x in nx.all_simple_paths(G, min(subjolts), max(subjolts)))
        if summed == 0:
            summed = 1
        total *= summed
    return total
