import aoc2015.day03 as d03
import utils.core as u


d03_s00 = ">"
d03_s01 = "^>v<"
d03_s02 = "^v^v^v^v^v"


def test_houses_visited():
    assert [(0, 0), (1, 0)] == list(d03.houses_visited(d03_s00))
    assert [(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)] == \
        list(d03.houses_visited(d03_s01))
    assert [(0, 0), (0, 1), (0, 0), (0, 1), (0, 0), (0, 1), (0, 0),
            (0, 1), (0, 0), (0, 1), (0, 0)] == \
        list(d03.houses_visited(d03_s02))


def distinct_houses_visited():
    assert 2 == d03.distinct_houses_visited(d03_s00)
    assert 4 == d03.distinct_houses_visited(d03_s01)
    assert 2 == d03.distinct_houses_visited(d03_s02)


day03_input = d03.parse(u.standard_puzzle_input(year=2015, day=3))


def test_part1():
    assert 2081 == d03.part1(day03_input)
