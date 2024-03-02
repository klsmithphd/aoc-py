import aoc2015.day25 as d25

d25_s00_raw = ["...Enter the code at row 2981, column 3075."]
d25_s00 = [2981, 3075]


def test_parse():
    assert d25_s00 == d25.parse(d25_s00_raw)
