import aoc2015.day19 as d19

d19_s00_raw = [
    "e => H",
    "e => O",
    "H => HO",
    "H => OH",
    "O => HH",
    "",
    "HOH"
]

d19_s01_raw = [
    "e => H",
    "e => O",
    "H => HO",
    "H => OH",
    "O => HH",
    "",
    "HOHOHO"
]

d19_s00 = (
    [["e", "H"],
     ["e", "O"],
     ["H", "HO"],
     ["H", "OH"],
     ["O", "HH"]],
    "HOH"
)

d19_s01 = (
    [["e", "H"],
     ["e", "O"],
     ["H", "HO"],
     ["H", "OH"],
     ["O", "HH"]],
    "HOHOHO"
)


def test_parse():
    assert d19_s00 == d19.parse(d19_s00_raw)
