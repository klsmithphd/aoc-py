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


def test_groupby_columns():
    assert set([(101, 102, 103),
                (201, 202, 203),
                (301, 302, 303),
                (401, 402, 403),
                (501, 502, 503),
                (601, 602, 603)]) == set(d03.groupby_columns(d03_s00))


day03_input = d03.parse(u.standard_puzzle_input(year=2016, day=3))


def test_part1():
    assert 869 == d03.part1(day03_input)


def test_part2():
    assert 1544 == d03.part2(day03_input)
