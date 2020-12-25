from collections import defaultdict
from enum import IntEnum
from typing import NamedTuple, Dict, List
import re


class Colour(IntEnum):
    WHITE = 0
    BLACK = 1


class HexaLobby:
    tiles: Dict
    steps = {
        'e': (1, -1, 0),
        'w': (-1, 1, 0),
        'se': (0, -1, 1),
        'sw': (-1, 0, 1),
        'nw': (0, 1, -1),
        'ne': (1, 0, -1),
    }

    message: int

    def __init__(self):
        self.tiles = defaultdict(int)
        self.message = ""

    def flip_tile(self, route_from_0: str):
        c = (0,0,0)
        pattern = re.compile(r'(e|s[ew]|w|n[ew])')
        moves = pattern.findall(route_from_0)
        for move in moves:
            x,y,z = self.steps[move]
            c = (c[0] + x, c[1] + y, c[2] + z)
        self.tiles[c] = (self.tiles[c] + 1) % 2
        if self.tiles[c] == Colour.WHITE:
            # No need to track white tiles
            self.tiles.pop(c)


    def flip_tiles(self, routes: List[str]):
        for route in routes:
            self.flip_tile(route)
        print(self.message)

    def count_black_tiles(self):
        return sum(self.tiles.values())

    def gol(self, times):
        for _ in range(times):
            self.gol_step()

    def gol_step(self):
        counts = defaultdict(int)
        for c in self.tiles.keys():
            for s in self.steps.values():
                counts[(c[0]+s[0], c[1]+s[1], c[2]+s[2])] += 1
        for c, v in counts.items():
            if v == 2 and c not in self.tiles:
                self.tiles[c] = 1
        topop = []
        for c in self.tiles.keys():
            if counts[c] == 0 or counts[c] > 2:
                topop.append(c)
        [self.tiles.pop(c) for c in topop]



