import copy
from abc import ABC, abstractmethod
from enum import IntEnum

from typing import Dict, NamedTuple, Optional, Iterable, List


class GridItem(IntEnum):
    EMPTY = 0
    TREE = 1
    OCCUPIED = 2
    SEAT = 3


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

    @abstractmethod
    def get_coords(self) -> Iterable[Coordinate]:
        pass

    @abstractmethod
    def get_values(self) -> Iterable[GridItem]:
        pass


class DictGrid(Grid, ABC):
    grid: Dict[Coordinate, GridItem] = {}

    def get_at_coordinate(self, coord: Coordinate) -> GridItem:
        return self.grid.get(coord, None)

    def set_coordinate(self, coord: Coordinate, item: GridItem):
        self.grid[coord] = item

    def get_largest_coordinate(self) -> Coordinate:
        return max(self.grid.keys())

    def get_coords(self) -> Iterable[Coordinate]:
        return self.grid.keys()

    def get_values(self) -> Iterable[GridItem]:
        return self.grid.values()


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


def generate_all_coords(maximum: Coordinate):
    for x in range(maximum.x + 1):
        for y in range(maximum.y + 1):
            yield Coordinate(x, y)


def seatcount(grid: Grid) -> int:
    return sum(1 for x in grid.get_values() if x == GridItem.OCCUPIED)


def new_mods(x_mod, y_mod):
    if x_mod > 0:
        x_mod += 1
    if x_mod < 0:
        x_mod -= 1
    if y_mod > 0:
        y_mod += 1
    if y_mod < 0:
        y_mod -= 1
    return x_mod, y_mod


def get_adjecent_coords(grid: Grid, position: Coordinate, lookfurther: bool, printit=False) -> Iterable[Coordinate]:
    max = grid.get_largest_coordinate()
    x_base = position.x
    y_base = position.y
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            x_mod, y_mod = x, y
            if x_mod == 0 and y_mod == 0:
                continue
            if lookfurther:
                while grid.get_at_coordinate(Coordinate(x_base + x_mod, y_base + y_mod)) == GridItem.EMPTY:
                    x_mod, y_mod = new_mods(x_mod, y_mod)
            if grid.get_at_coordinate(Coordinate(x_base + x_mod, y_base + y_mod)) is None:
                continue
            yield Coordinate(x_base + x_mod, y_base + y_mod)


def should_change(grid: Grid, position: Coordinate, lookfurther: bool = False) -> bool:
    current_value = grid.get_at_coordinate(position)
    if current_value == GridItem.EMPTY:
        return False
    if current_value == GridItem.SEAT:
        num_occupied = sum(1 for x in get_adjecent_coords(grid, position, lookfurther) if
                           grid.get_at_coordinate(x) == GridItem.OCCUPIED)
        if num_occupied == 0:
            return True
        return False
    # else: GridItem.OCCUPIED
    num_occupied = sum(
        1 for x in get_adjecent_coords(grid, position, lookfurther) if grid.get_at_coordinate(x) == GridItem.OCCUPIED)
    if (not lookfurther and num_occupied >= 4) or (lookfurther and num_occupied >= 5):
        return True
    return False


def change(grid, position):
    current_value = grid.get_at_coordinate(position)
    if current_value == GridItem.EMPTY:
        return
    if current_value == GridItem.SEAT:
        grid.set_coordinate(position, GridItem.OCCUPIED)
        return
    # else: GridItem.OCCUPIED
    grid.set_coordinate(position, GridItem.SEAT)


def seating_step(grid: Grid, lookfurther: bool = False):
    tochange = []
    for position in generate_all_coords(grid.get_largest_coordinate()):
        if should_change(grid, position, lookfurther=lookfurther):
            tochange.append(position)
    for position in tochange:
        change(grid, position)


def to_char(item: GridItem):
    if item == GridItem.EMPTY:
        return "."
    if item == GridItem.SEAT:
        return "L"
    if item == GridItem.OCCUPIED:
        return "#"


def printgrid(grid: Grid):
    print()
    print()
    maximum = grid.get_largest_coordinate()
    for x in range(maximum.x + 1):
        line = "".join(to_char(grid.get_at_coordinate(Coordinate(x, y))) for y in range(maximum.y + 1))
        print(line)


def simulate_seating_until_done(grid: Grid, lookfurther: bool = False) -> int:
    previous_seatcount = -1
    printgrid(grid)
    while seatcount(grid) != previous_seatcount:
        previous_seatcount = seatcount(grid)
        seating_step(grid, lookfurther)
    toret = seatcount(grid)
    return toret
