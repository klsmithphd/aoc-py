import aoc2015.day02 as d02
import utils.core as u

d02_s00_raw = ["2x3x4",
               "1x1x10"]

d02_s00 = [(2, 3, 4), (1, 1, 10)]


def test_parse():
    assert d02_s00 == d02.parse(d02_s00_raw)


def test_wrapping_paper_area():
    assert 58 == d02.wrapping_paper_area(d02_s00[0])
    assert 43 == d02.wrapping_paper_area(d02_s00[1])


day02_input = d02.parse(u.standard_puzzle_input(year=2015, day=2))


def test_part1():
    assert 1598415 == d02.part1(day02_input)
