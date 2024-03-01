import aoc2015.day24 as d24


d24_s00_raw = ["1", "2", "3", "4", "5",
               "7", "8", "9", "10", "11"]

d24_s00 = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]


def test_parse():
    assert d24_s00 == d24.parse(d24_s00_raw)
