import aoc2016.day01 as d01


d01_s00_raw = ["R2, L3"]
d01_s00 = [("right", 2), ("left", 3)]


def test_parse():
    assert d01_s00 == d01.parse(d01_s00_raw)
