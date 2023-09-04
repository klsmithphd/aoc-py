from aoc2022.day08 import parse, part1, \
    trees_visible_from_left, trees_visible_in_row, trees_visible_count
from utils.core import standard_puzzle_input

d08_s01_raw = """30373
25512
65332
33549
35390""".splitlines()

d08_s01 = [[3, 0, 3, 7, 3],
           [2, 5, 5, 1, 2],
           [6, 5, 3, 3, 2],
           [3, 3, 5, 4, 9],
           [3, 5, 3, 9, 0]]


def test_parse():
    assert d08_s01 == parse(d08_s01_raw)


def test_trees_visible_from_left():
    assert [1, 0, 0, 1, 0] == trees_visible_from_left(d08_s01[0])
    assert [1, 1, 0, 0, 0] == trees_visible_from_left(d08_s01[1])
    assert [1, 0, 0, 0, 0] == trees_visible_from_left(d08_s01[2])
    assert [1, 0, 1, 0, 1] == trees_visible_from_left(d08_s01[3])
    assert [1, 1, 0, 1, 0] == trees_visible_from_left(d08_s01[4])


def test_trees_visible_in_row():
    assert [1, 0, 0, 1, 1] == trees_visible_in_row(d08_s01[0])
    assert [1, 1, 1, 0, 1] == trees_visible_in_row(d08_s01[1])
    assert [1, 1, 0, 1, 1] == trees_visible_in_row(d08_s01[2])
    assert [1, 0, 1, 0, 1] == trees_visible_in_row(d08_s01[3])
    assert [1, 1, 0, 1, 1] == trees_visible_in_row(d08_s01[4])


def test_trees_visible_count():
    assert 21 == trees_visible_count(d08_s01)


d08_input = parse(standard_puzzle_input(year=2022, day=8))


def test_day08_part1_soln():
    assert 1538 == part1(d08_input)


# def test_day08_part2_soln():
#     assert 1 == day08_soln.part2(d08_input)
