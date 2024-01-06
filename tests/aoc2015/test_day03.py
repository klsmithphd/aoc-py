import aoc2015.day03 as d03
import utils.core as u


d03_s00 = ">"
d03_s01 = "^>v<"
d03_s02 = "^v^v^v^v^v"
d03_s03 = "^v"


def test_houses_visited():
    assert [(0, 0), (1, 0)] == list(d03.visits(d03_s00))
    assert [(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)] == \
        list(d03.visits(d03_s01))
    assert [(0, 0), (0, 1), (0, 0), (0, 1), (0, 0), (0, 1), (0, 0),
            (0, 1), (0, 0), (0, 1), (0, 0)] == \
        list(d03.visits(d03_s02))


def test_split_houses_visited():
    assert [(0, 0), (0, 1), (0, 0), (0, -1)] == \
        list(d03.split_visits(d03_s03))
    assert [(0, 0), (0, 1), (0, 0),
            (0, 0), (1, 0), (0, 0)] == \
        list(d03.split_visits(d03_s01))
    assert [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
            (0, 0), (0, -1), (0, -2), (0, -3), (0, -4), (0, -5)] == \
        list(d03.split_visits(d03_s02))


def test_distinct_houses_visited():
    assert 2 == d03.distinct_visits(d03_s00, d03.visits)
    assert 4 == d03.distinct_visits(d03_s01, d03.visits)
    assert 2 == d03.distinct_visits(d03_s02, d03.visits)
    assert 3 == d03.distinct_visits(d03_s03, d03.split_visits)
    assert 3 == d03.distinct_visits(d03_s01, d03.split_visits)
    assert 11 == d03.distinct_visits(d03_s02, d03.split_visits)


day03_input = d03.parse(u.standard_puzzle_input(year=2015, day=3))


def test_part1():
    assert 2081 == d03.part1(day03_input)


def test_part2():
    assert 2341 == d03.part2(day03_input)
