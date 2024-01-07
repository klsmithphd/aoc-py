import aoc2015.day08 as d08
import utils.core as u

d08_s00 = [
    r'""',
    r'"abc"',
    r'"aaa\"aaa"',
    r'"\x27"'
]

d08_s00_unescaped = [
    "",
    "abc",
    "aaa\"aaa",
    "\x27"
]

d08_s08_escaped = [
    r'"\"\""',
    r'"\"abc\""',
    r'"\"aaa\\\"aaa\""',
    r'"\"\\x27\""'
]


def test_unescape():
    assert d08_s00_unescaped == [d08.unescape(x) for x in d08_s00]


def test_escape():
    assert d08_s08_escaped == [d08.escape(x) for x in d08_s00]


def test_code_count():
    assert [2, 5, 10, 6] == [len(x) for x in d08_s00]


def test_unescaped_count():
    assert [0, 3, 7, 1] == [len(d08.unescape(x)) for x in d08_s00]


def test_escaped_count():
    assert [6, 9, 16, 11] == [len(d08.escape(x)) for x in d08_s00]


def test_unescaped_diff():
    assert 12 == d08.unescaped_diff(d08_s00)


def test_escaped_diff():
    assert 19 == d08.escaped_diff(d08_s00)


day08_input = d08.parse(u.standard_puzzle_input(year=2015, day=8))


def test_part1():
    assert 1371 == d08.part1(day08_input)


def test_part2():
    assert 2117 == d08.part2(day08_input)
