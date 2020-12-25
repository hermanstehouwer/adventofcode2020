from typing import List

import pytest
from pytest import fixture

from core.hexalobby import HexaLobby


@fixture
def tile_routes():
    a = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""
    yield a.split("\n")

@fixture
def lobby():
    yield HexaLobby()


def test_part1(lobby: HexaLobby, tile_routes: List[str]):
    assert lobby.count_black_tiles() == 0
    lobby.flip_tiles(tile_routes)
    assert lobby.count_black_tiles() == 10


def test_part2(lobby: HexaLobby, tile_routes: List[str]):
    lobby.flip_tiles(tile_routes)
    lobby.gol(times=100)
    assert lobby.count_black_tiles() == 2208
