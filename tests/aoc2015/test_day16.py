import aoc2015.day16 as d16
import utils.core as u

d16_s00_raw = [
    "Sue 1: children: 1, cars: 8, vizslas: 7",
    "Sue 2: akitas: 10, perfumes: 10, children: 5",
    "Sue 3: cars: 5, pomeranians: 4, vizslas: 1",
    "Sue 4: goldfish: 5, children: 8, perfumes: 3",
    "Sue 5: vizslas: 2, akitas: 7, perfumes: 6"
]

d16_s00 = {
    1: {"children": 1, "cars": 8, "vizslas": 7},
    2: {"akitas": 10,  "perfumes": 10, "children": 5},
    3: {"cars": 5, "pomeranians": 4, "vizslas": 1},
    4: {"goldfish": 5, "children": 8, "perfumes": 3},
    5: {"vizslas": 2, "akitas": 7, "perfumes": 6}
}


def test_parse():
    assert d16_s00 == d16.parse(d16_s00_raw)


day16_input = d16.parse(u.standard_puzzle_input(year=2015, day=16))


def test_part1():
    assert 213 == d16.part1(day16_input)


def test_part2():
    assert 323 == d16.part2(day16_input)
