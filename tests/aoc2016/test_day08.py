import aoc2016.day08 as d08

d08_s00_raw = [
    "rect 3x2",
    "rotate column x=1 by 1",
    "rotate row y=0 by 4",
    "rotate column x=1 by 1"
]

d08_s00 = [
    {"cmd": "rect", "width": 3, "height": 2},
    {"cmd": "rotate", "dim": "column", "pos": 1, "amount": 1},
    {"cmd": "rotate", "dim": "row", "pos": 0, "amount": 4},
    {"cmd": "rotate", "dim": "column", "pos": 1, "amount": 1}
]


def test_parse():
    assert d08_s00 == d08.parse(d08_s00_raw)
