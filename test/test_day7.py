from pytest import fixture

from core.bagtree import BagTree, BagTree2


@fixture
def example_rules():
    a = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
    yield a.split("\n")

@fixture
def example_rules2():
    a = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
    yield a.split("\n")


def test_part1(example_rules):
    bt = BagTree()
    for rule in example_rules:
        bt.add_bags_from_line(rule)
    sires = bt.get_list_of_parents("shiny gold")
    assert len(sires) == 4
    bt = BagTree2()
    for rule in example_rules:
        bt.add_bags_from_line(rule)
    sires = bt.get_list_of_parents("shiny gold")
    print(sires)
    assert len(sires) == 4


def test_part2(example_rules2):
    bt = BagTree()
    for rule in example_rules2:
        bt.add_bags_from_line(rule)
    assert bt.count_number_of_children("shiny gold") == 126
    bt = BagTree2()
    for rule in example_rules2:
        bt.add_bags_from_line(rule)
    print(bt.G.nodes)
    print(bt.G.edges)
    assert bt.count_number_of_children("shiny gold") == 126