import aoc2015.day19 as d19
import utils.core as u

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


def test_match_ranges():
    assert [(0, 2), (2, 4), (4, 6)] == list(d19.match_ranges("HOHOHO", "HO"))
    assert [(1, 3), (3, 5)] == list(d19.match_ranges("HOHOHO", "OH"))
    assert [] == list(d19.match_ranges("HOHOHO", "e"))
    assert [(1, 4), (3, 6)] == list(d19.match_ranges("HOHOHO", "OHO"))


def test_single_replacements():
    assert ["HOOH", "HOHO"] == \
        list(d19.single_replacements(["H", "HO"], "HOH"))
    assert ["OHOH", "HOOH"] == \
        list(d19.single_replacements(["H", "OH"], "HOH"))
    assert ["HHHH"] == list(d19.single_replacements(["O", "HH"], "HOH"))


def test_distinct_molecules():
    assert 4 == len(d19.distinct_molecules(*d19_s00))
    assert 7 == len(d19.distinct_molecules(*d19_s01))


def test_fabrication_steps():
    assert 3 == len(d19.fabrication_steps(d19_s00))
    assert 6 == len(d19.fabrication_steps(d19_s01))


day19_input = d19.parse(u.standard_puzzle_input(year=2015, day=19))


def test_part1():
    assert 518 == d19.part1(day19_input)


def test_part2():
    assert 200 == d19.part2(day19_input)
