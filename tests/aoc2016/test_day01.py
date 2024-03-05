import aoc2016.day01 as d01


d01_s00_raw = ["R2, L3"]
d01_s00 = [("right", 2), ("left", 3)]


def test_parse():
    assert d01_s00 == d01.parse(d01_s00_raw)


d01_s01 = d01.parse(["R2, R2, R2"])
d01_s02 = d01.parse(["R5, L5, R5, R3"])
d01_s03 = d01.parse(["R8, R4, R4, R8"])


def test_move():
    assert (2, 3) == d01.move(d01_s00)['pos']
    assert (0, -2) == d01.move(d01_s01)['pos']
    assert (10, 2) == d01.move(d01_s02)['pos']
