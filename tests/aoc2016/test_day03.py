import aoc2016.day03 as d03
import utils.core as u

d03_s00_raw = [
    "101 301 501",
    "102 302 502",
    "103 303 503",
    "201 401 601",
    "202 402 602",
    "203 403 603"
]

d03_s00 = [
    (101, 301, 501),
    (102, 302, 502),
    (103, 303, 503),
    (201, 401, 601),
    (202, 402, 602),
    (203, 403, 603)
]


def test_parse():
    assert d03_s00 == d03.parse(d03_s00_raw)


day03_input = d03.parse(u.standard_puzzle_input(year=2016, day=3))


def test_part1():
    assert 869 == d03.part1(day03_input)
