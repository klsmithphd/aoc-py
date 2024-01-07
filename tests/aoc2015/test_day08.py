import aoc2015.day08 as d08
import utils.core as u

d08_s00 = [
    r'""',
    r'"abc"',
    r'"aaa\"aaa"',
    r'"\x27"'
]


def test_code_chars():
    assert [2, 5, 10, 6] == [d08.code_chars(x) for x in d08_s00]


def test_string_chars():
    assert [0, 3, 7, 1] == [d08.string_chars(x) for x in d08_s00]


def test_unescaped_diff():
    assert 12 == d08.unescaped_diff(d08_s00)


day08_input = d08.parse(u.standard_puzzle_input(year=2015, day=8))


def test_part1():
    assert 1371 == d08.part1(day08_input)
