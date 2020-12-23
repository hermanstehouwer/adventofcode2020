from typing import List, Dict


class CrabCups:
    cups: Dict[int, int]
    current_cup: int
    min_val: int
    max_val: int

    def __init__(self, cups: List[int], expand=False):
        self.cups = dict(zip(cups, cups[1:] + cups[:1]))
        self.current_cup = cups[0]
        self.min_val = min(cups)
        self.max_val = max(cups)
        if expand:
            self.expand(cups)

    def game(self, moves: int = 100):
        for _ in range(moves):
            self.move()

    def move(self):
        take = self.take(3)
        destination = self.find_destination_cup(take)
        self.place(destination, take)
        self.current_cup = self.cups[self.current_cup]

    def get_label(self) -> str:
        idx = self.cups[1]
        ret = []
        for _ in range(len(self.cups)-1):
            ret.append(str(idx))
            idx = self.cups[idx]
        return ''.join(ret)

    def take(self, number: int) -> List[int]:
        idx = self.cups[self.current_cup]
        ret = []
        for _ in range(number):
            ret.append(idx)
            idx = self.cups[idx]
        self.cups[self.current_cup] = self.cups[ret[-1]]
        return ret

    def find_destination_cup(self, take) -> int:
        to_find = self.current_cup
        if (to_find := to_find - 1) < self.min_val:
            to_find = self.max_val
        while to_find in take:
            if (to_find := to_find - 1) < self.min_val:
                to_find = self.max_val
        return to_find

    def place(self, destination: int, take: List[int]):
        self.cups[take[-1]] = self.cups[destination]
        self.cups[destination] = take[0]

    def mult_next_to_one(self, number: int = 2) -> int:
        ret = 1
        idx = 1
        for _ in range(number):
            idx = self.cups[idx]
            ret *= idx
        return ret

    def expand(self, cups: List[int]):
        old = self.cups
        self.cups = dict(zip(range(1000001), list(range(1, 1000001))+[1]))
        self.max_val = 1000000
        for k,v in old.items():
            self.cups[k] = v
        self.cups[cups[-1]] = 10
        self.cups[1000000] = cups[0]
