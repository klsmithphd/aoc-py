import aoc2015.day22 as d22


d22_s00_raw = [
    "Hit Points: 58",
    "Damage: 9"
]

d22_s00 = d22.Stats(hit_points=58, damage=9)


def test_parse():
    assert d22_s00 == d22.parse(d22_s00_raw)
