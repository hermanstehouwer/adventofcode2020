from abc import ABC, abstractmethod
from enum import IntEnum

from typing import Dict, NamedTuple, Optional, Iterable


class GridItem(IntEnum):
    EMPTY = 0
    TREE = 1


class Coordinate(NamedTuple):
    x: int
    y: int


class Grid(ABC):
    @abstractmethod
    def get_at_coordinate(self, coord: Coordinate) -> GridItem:
        pass

    @abstractmethod
    def set_coordinate(self, coord: Coordinate, item: GridItem):
        pass

    @abstractmethod
    def get_largest_coordinate(self) -> Coordinate:
        pass


class DictGrid(Grid, ABC):
    grid: Dict[Coordinate, GridItem] = {}

    def get_at_coordinate(self, coord: Coordinate) -> GridItem:
        return self.grid.get(coord, GridItem.EMPTY)

    def set_coordinate(self, coord: Coordinate, item: GridItem):
        self.grid[coord] = item

    def get_largest_coordinate(self) -> Coordinate:
        return max(self.grid.keys())


def next_coord(start_coord: Coordinate, delta: Coordinate, maximum: Coordinate) -> Optional[Coordinate]:
    new_coord = Coordinate(
        start_coord.x + delta.x,
        (start_coord.y + delta.y) % (maximum.y + 1)
    )
    if new_coord > maximum:
        return None
    return new_coord


def generate_coords(start_coord: Coordinate, delta: Coordinate, maximum: Coordinate) -> Iterable[Coordinate]:
    """
    Generates coordinates that wrap around horizontally.
    """
    if delta.x == 0:
        raise ValueError("With a vertical delta of 0 the function wouldn't terminate")
    while start_coord := next_coord(start_coord, delta, maximum):
        yield start_coord
