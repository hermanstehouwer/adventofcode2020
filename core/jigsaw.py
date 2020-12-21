import math
from collections import defaultdict
from typing import Dict, List, Union

MONSTER = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split("\n")


def num_hash(lines: List[str]) -> int:
    total = 0
    for line in lines:
        total += len([x for x in line if x == "#"])
    return total


def normalize_edge(edge: str) -> str:
    i = 0
    j = len(edge) - 1
    while edge[i] == edge[j]:
        i += 1
        j -= 1
    return edge if edge[i] == "#" else ''.join(reversed(edge))


class Tile:
    id: int
    image: List[str]
    rows: int
    cols: int
    edges_normalized: List[str]
    edges: List[str]

    def reset_edges(self):
        self.edges_normalized = [normalize_edge(edge) for edge in [
            self.image[0],
            ''.join([line[-1] for line in self.image]),
            self.image[-1],
            ''.join([line[0] for line in self.image])
        ]]
        self.edges = [
            self.image[0],
            ''.join([line[-1] for line in self.image]),
            self.image[-1],
            ''.join([line[0] for line in self.image])
        ]

    def __init__(self, desc: str):
        lines = desc.split("\n")
        first_line = lines.pop(0)
        self.id = int(first_line[-5:-1])
        self.image = lines
        self.rows = len(self.image)
        self.cols = len(self.image[0])
        self.reset_edges()

    def __str__(self):
        return f"Tile {self.id}:\n" + "\n".join([' '.join(row) for row in self.image])

    def __repr__(self):
        return f"Tile: {self.id}"

    def orientations(self):
        for _ in self.mirrors():
            for _ in self.rotations():
                yield

    def mirror(self):
        self.image = self.image[::-1]
        self.reset_edges()

    def flip(self):
        self.image = [row[::-1] for row in self.image]
        self.reset_edges()

    def rotate(self):
        new_image = []
        for min_col in range(self.cols):
            line = []
            for new_row in range(self.rows):
                line.append(self.image[new_row][-1-min_col])
            new_image.append(''.join(line))
        self.image = new_image
        self.reset_edges()

    def pretty(self):
        print()
        print(f"Pretty: Tile: {self.id}")
        for row in self.image:
            print(row)
        print()

    def rotations(self):
        for _ in range(5):
            yield
            self.rotate()

    def mirrors(self):
        self.mirror()
        yield
        self.mirror()
        self.flip()
        yield
        self.flip()
        yield

    def find_max_monsters(self) -> int:
        return max([self.count_monsters() for _ in self.orientations()])

    def count_monsters(self) -> int:
        count = 0
        for col in range(self.cols-(len(MONSTER[0]) -1)):
            for row in range(self.rows - (len(MONSTER)-1)):
                if self.has_monster_at_position(row, col):
                    count += 1
        return count

    def has_monster_at_position(self, row: int, col: int) -> bool:
        for c_mod in range(len(MONSTER[0])):
            for r_mod in range(len(MONSTER)):
                if MONSTER[r_mod][c_mod] == "#" and self.image[row+r_mod][col+c_mod] != "#":
                    return False
        return True

    def number_of_hashes(self):
        return num_hash(self.image)

class JigSaw:
    tiles: List[Tile]
    edge_to_tiles: Dict[str, List[Tile]]
    corners: List[Tile]
    size: int
    puzzle: List[List[Union[Tile,None]]]
    big_tile: Tile

    def __init__(self, tiles: List[Tile]):
        self.tiles = tiles
        self.edge_to_tiles = defaultdict(list)
        self.corners = []
        self.size = int(math.sqrt(len(self.tiles)))
        self.puzzle = [[None]*self.size for _ in range(self.size)]

    def mult_corners(self) -> int:
        self.find_corners()
        return math.prod([x.id for x in self.corners])

    def find_corners(self) -> None:
        for tile in self.tiles:
            for edge in tile.edges_normalized:
                self.edge_to_tiles[edge].append(tile)
        tile_nonmatching_edges = defaultdict(int)
        counter = defaultdict(int)
        for edge, tiles in self.edge_to_tiles.items():
            counter[len(tiles)] += 1
            if len(tiles) == 1:
                tile_nonmatching_edges[tiles[0]] += 1
        for tile in tile_nonmatching_edges.keys():
            if tile_nonmatching_edges[tile] == 2:
                self.corners.append(tile)

    def puzzles(self):
        unplaced = list(self.tiles)
        for row in range(self.size):
            for column in range(self.size):
                if row == column == 0:
                    self.puzzle[row][column] = self.corners[0]
                    unplaced.remove(self.corners[0])
                    self.make_top_left(self.corners[0])
                elif column == 0:
                    # only connect the top
                    top_edge = self.puzzle[row - 1][column].edges_normalized[2]
                    for candidate in self.edge_to_tiles[top_edge]:
                        if candidate not in unplaced:
                            continue
                        self.puzzle[row][column] = candidate
                        unplaced.remove(candidate)
                        top_edge = self.puzzle[row - 1][column].edges[2]
                        self.make_left(candidate, top_edge)
                elif row == 0:
                    left_edge = self.puzzle[row][column - 1].edges_normalized[1]
                    for candidate in self.edge_to_tiles[left_edge]:
                        if candidate not in unplaced:
                            continue
                        self.puzzle[row][column] = candidate
                        unplaced.remove(candidate)
                        left_edge = self.puzzle[row][column - 1].edges[1]
                        self.make_top(candidate, left_edge)
                else:
                    top_edge = self.puzzle[row - 1][column].edges_normalized[2]
                    left_edge = self.puzzle[row][column - 1].edges_normalized[1]
                    candidates_1 = self.edge_to_tiles[left_edge]
                    candidates_2 = self.edge_to_tiles[top_edge]
                    for candidate in list(set(candidates_1) & set(candidates_2)):
                        if candidate not in unplaced:
                            continue
                        top_edge = self.puzzle[row - 1][column].edges[2]
                        left_edge = self.puzzle[row][column - 1].edges[1]
                        self.puzzle[row][column] = candidate
                        unplaced.remove(candidate)
                        self.make_normal(candidate, top_edge, left_edge)

        lines = ["Tile 9999:"]
        for row in range(self.size):
            for row2 in range(1, self.puzzle[row][0].rows-1):
                lines.append(''.join([''.join(self.puzzle[row][col].image[row2][1:-1]) for col in range(self.size)]))
        self.big_tile = Tile("\n".join(lines))

    def number_of_monsters(self):
        return self.big_tile.find_max_monsters()

    def leftover_hash(self):
        num_monsters = self.number_of_monsters()
        return self.big_tile.number_of_hashes() - (num_monsters * num_hash(MONSTER))

    def make_top_left(self, tile: Tile):
        for _ in tile.orientations():
            if len(self.edge_to_tiles[tile.edges_normalized[0]]) == 1 and \
                    len(self.edge_to_tiles[tile.edges_normalized[3]]) == 1:
                return
        print(f"DANGER tl")


    def make_left(self, tile: Tile, top_edge):
        for _ in tile.orientations():
            if len(self.edge_to_tiles[tile.edges_normalized[3]]) == 1 and \
                    tile.edges[0] == top_edge:
                return
        print(f"DANGER l")


    def make_top(self, tile: Tile, left_edge):
        for _ in tile.orientations():
            if len(self.edge_to_tiles[tile.edges_normalized[0]]) == 1 and \
                    tile.edges[3] == left_edge:
                return
        print(f"DANGER t")


    def make_normal(self, tile: Tile, top_edge, left_edge):
        for _ in tile.orientations():
            if tile.edges[0] == top_edge and \
                    tile.edges[3] == left_edge:
                return
        print(f"DANGER n")

    def make_bottom_right(self, tile: Tile):
        for _ in tile.orientations():
            if len(self.edge_to_tiles[tile.edges_normalized[1]]) == 1 and \
                    len(self.edge_to_tiles[tile.edges_normalized[2]]) == 1:
                return
        print(f"DANGER br")

