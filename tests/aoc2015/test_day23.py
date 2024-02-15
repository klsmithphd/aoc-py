import aoc2015.day23 as d23

d23_s00_raw = [
    "inc a",
    "jio a, +2",
    "tpl a",
    "inc a"
]

d23_s00 = [
    d23.Instruction("inc", "a"),
    d23.Instruction("jio", "a", 2),
    d23.Instruction("tpl", "a"),
    d23.Instruction("inc", "a")
]


def test_parse():
    assert d23_s00 == d23.parse(d23_s00_raw)
