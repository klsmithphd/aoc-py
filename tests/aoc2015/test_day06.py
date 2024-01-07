import aoc2015.day06 as d06
import utils.core as u

d06_s00_raw = ["turn on 0,0 through 999,999",
               "toggle 0,0 through 999,0",
               "turn off 499,499 through 500,500"]

d06_s00 = [d06.Instruction("turn on",  (0, 0),     (999, 999)),
           d06.Instruction("toggle",   (0, 0),     (999, 0)),
           d06.Instruction("turn off", (499, 499), (500, 500))]


def test_parse():
    assert d06_s00 == d06.parse(d06_s00_raw)


def test_brightness():
    assert 1000000 == d06.part1(d06_s00[:1])
    assert 999000 == d06.part1(d06_s00[:2])
    assert 998996 == d06.part1(d06_s00)


day06_input = d06.parse(u.standard_puzzle_input(year=2015, day=6))


def test_part1():
    assert 377891 == d06.part1(day06_input)


def test_part2():
    assert 14110788 == d06.part2(day06_input)
