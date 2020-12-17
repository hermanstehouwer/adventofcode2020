from typing import Tuple, Set, Iterable, Dict, Iterator


class GoL:
    # 3D/4D GoL
    active_cubes: Set[Tuple[int,int,int,int]]
    extra_dim: bool

    def __init__(self, start_state: Iterable[str], extra_dim: bool = False):
        self.extra_dim = extra_dim
        self.active_cubes = set()
        for y, line in enumerate(start_state):
            for x, char in enumerate(line):
                if char == "#":
                    self.active_cubes.add((x, y, 0, 0))

    def cycle(self) -> None:
        counter: Dict[Tuple[int,int,int,int],int] = {}
        for coord in self.active_cubes:
            for c in self.neighbours_of_coordinate(coord):
                counter[c] = counter.get(c, 0) + 1
        new_coords: Set[Tuple[int, int, int, int]] = set()
        for coord in self.active_cubes:
            if 3 <= counter[coord] <= 4:
                new_coords.add(coord)
        for coord in counter.keys() - self.active_cubes:
            if counter[coord] == 3:
                new_coords.add(coord)
        self.active_cubes = new_coords

    def boot(self) -> None:
        for _ in range(6):
            self.cycle()

    def count_active(self) -> int:
        return len(self.active_cubes)

    def neighbours_of_coordinate(self, coord: Tuple[int, int, int, int]) -> Iterator[Tuple[int, int, int, int]]:
        x, y, z, w = coord
        w_mods = [0]
        if self.extra_dim:
            w_mods = [-1, 0, 1]
        for x_mod in [-1, 0, 1]:
            for y_mod in [-1, 0, 1]:
                for z_mod in [-1, 0, 1]:
                    for w_mod in w_mods:
                        yield x + x_mod, y + y_mod, z + z_mod, w + w_mod
