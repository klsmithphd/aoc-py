import aoc2016.day02 as d02
import utils.core as u


d02_s00 = ["ULL",
           "RRDDD",
           "LURDL",
           "UUUUD"]


def test_all_digits_pos():
    assert [(0, 0), (-1, 1), (1, -1), (0, -1), (0, 0)] == \
        list(d02.all_digits_pos(d02.SQUARE_KEYPAD, d02_s00))


def test_bathroom_code():
    assert "1985" == d02.square_bathroom_code(d02_s00)


day02_input = d02.parse(u.standard_puzzle_input(year=2016, day=2))


def test_part1():
    assert "18843" == d02.part1(day02_input)
