import aoc2015.day21 as d21

d21_s00_raw = [
    "Hit Points: 104",
    "Damage: 8",
    "Armor: 1"
]

d21_s00 = d21.Stats(hit_points=104, damage=8, armor=1)


def test_parse():
    assert d21_s00 == d21.parse(d21_s00_raw)
