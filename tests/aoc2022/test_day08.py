from aoc2022.day08 import parse, part1, part2, \
    trees_visible_from_left, trees_visible_in_row, trees_visible_count, \
    tree_distance, scenic_scores, max_scenic_score
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


def test_tree_distance():
    assert (0, 2) == tree_distance(d08_s01[0], 0)
    assert (1, 1) == tree_distance(d08_s01[0], 1)
    assert (2, 1) == tree_distance(d08_s01[0], 2)
    assert (3, 1) == tree_distance(d08_s01[0], 3)
    assert (1, 0) == tree_distance(d08_s01[0], 4)

    assert (0, 1) == tree_distance(d08_s01[1], 0)
    assert (1, 1) == tree_distance(d08_s01[1], 1)
    assert (1, 2) == tree_distance(d08_s01[1], 2)
    assert (1, 1) == tree_distance(d08_s01[1], 3)
    assert (2, 0) == tree_distance(d08_s01[1], 4)


def test_scenic_scores():
    assert [0, 0, 0, 0, 0,
            0, 1, 4, 1, 0,
            0, 6, 1, 2, 0,
            0, 1, 8, 3, 0,
            0, 0, 0, 0, 0] == list(scenic_scores(d08_s01))


def test_max_scenic_score():
    assert 8 == max_scenic_score(d08_s01)


d08_input = parse(standard_puzzle_input(year=2022, day=8))


def test_day08_part1_soln():
    assert 1538 == part1(d08_input)


def test_day08_part2_soln():
    assert 496125 == part2(d08_input)
