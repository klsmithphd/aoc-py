import aoc2016.day01 as d01
import utils.core as u


d01_s00_raw = ["R2, L3"]
d01_s00 = [("right", 2), ("left", 3)]


def test_parse():
    assert d01_s00 == d01.parse(d01_s00_raw)


d01_s01 = d01.parse(["R2, R2, R2"])
d01_s02 = d01.parse(["R5, L5, R5, R3"])
d01_s03 = d01.parse(["R8, R4, R4, R8"])


def test_move():
    assert (2, 3) == d01.move(d01_s00)['pos']
    assert (0, -2) == d01.move(d01_s01)['pos']
    assert (10, 2) == d01.move(d01_s02)['pos']


def test_distance():
    assert 5 == d01.distance(d01_s00)
    assert 2 == d01.distance(d01_s01)
    assert 12 == d01.distance(d01_s02)


def test_all_points():
    assert [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)] == \
        list(d01.all_points(d01_s00))


def test_first_duplicate():
    assert (4, 0) == d01.first_duplicate(d01.all_points(d01_s03))


def test_distance_to_first_duplicate():
    assert 4 == d01.distance_to_first_duplicate(d01_s03)


day01_input = d01.parse(u.standard_puzzle_input(year=2016, day=1))


def test_part1():
    assert 241 == d01.part1(day01_input)


def test_part2():
    assert 116 == d01.part2(day01_input)
