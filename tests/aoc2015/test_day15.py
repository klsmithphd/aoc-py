import aoc2015.day15 as d15
import utils.core as u

d15_s00_raw = [
    "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
    "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"
]

d15_s00 = [[-1, -2, 6, 3, 8],
           [2, 3, -2, -1, 3]]


def test_parse():
    """Correctly parses the input"""
    assert d15_s00 == d15.parse(d15_s00_raw)
