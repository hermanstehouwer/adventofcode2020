from pytest import fixture

from core.jigsaw import Tile, JigSaw
from readers.generic import yield_blocks


@fixture
def tiles():
    tiles = []
    for tile_desc in yield_blocks("test/data/day20_test.txt"):
        tiles.append(Tile(tile_desc))
    yield tiles


def test_part1(tiles):
    assert len(tiles) == 9
    jigsaw = JigSaw(tiles)
    assert jigsaw.mult_corners() == 20899048083289
    jigsaw.puzzles()
    assert jigsaw.number_of_monsters() == 2
    assert jigsaw.leftover_hash() == 273