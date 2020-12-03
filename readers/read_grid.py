from contextlib import contextmanager
from typing import Iterable

from core.Grid import *


def getGridItem(c: str) -> GridItem:
    if c == ".":
        return GridItem.EMPTY
    return GridItem.TREE


def create_grid(lines: Iterable[str]) -> Grid:
    grid = DictGrid()
    x = 0
    for line in lines:
        y = 0
        for c in line:
            item = getGridItem(c)
            coord = Coordinate(x, y)
            grid.set_coordinate(coord, item)
            y += 1
        x += 1
    return grid
