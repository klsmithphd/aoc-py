from aoc2022.day09 import parse, part1, part2, \
    step, all_moves, unique_tail_positions, unique_tail_pos_count
from toolz import last
from utils.core import standard_puzzle_input

d09_s01_raw = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()

d09_s02_raw = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".splitlines()

d09_s01 = ['R', 'R', 'R', 'R',
           'U', 'U', 'U', 'U',
           'L', 'L', 'L',
           'D',
           'R', 'R', 'R', 'R',
           'D',
           'L', 'L', 'L', 'L', 'L',
           'R', 'R']

d09_s02 = list(parse(d09_s02_raw))


def test_parse():
    assert d09_s01 == list(parse(d09_s01_raw))


def test_step():
    assert [(1, 0), (0, 0)] == step([(0, 0), (0, 0)], 'R')
    assert [(2, 0), (1, 0)] == step([(1, 0), (0, 0)], 'R')
    assert [(3, 0), (2, 0)] == step([(2, 0), (1, 0)], 'R')
    assert [(4, 0), (3, 0)] == step([(3, 0), (2, 0)], 'R')
    assert [(4, 1), (3, 0)] == step([(4, 0), (3, 0)], 'U')
    assert [(4, 2), (4, 1)] == step([(4, 1), (3, 0)], 'U')
    assert [(4, 3), (4, 2)] == step([(4, 2), (4, 1)], 'U')
    assert [(4, 4), (4, 3)] == step([(4, 3), (4, 2)], 'U')
    assert [(3, 4), (4, 3)] == step([(4, 4), (4, 3)], 'L')
    assert [(2, 4), (3, 4)] == step([(3, 4), (4, 3)], 'L')
    assert [(1, 4), (2, 4)] == step([(2, 4), (3, 4)], 'L')
    assert [(1, 3), (2, 4)] == step([(1, 4), (2, 4)], 'D')
    assert [(2, 3), (2, 4)] == step([(1, 3), (2, 4)], 'R')
    assert [(3, 3), (2, 4)] == step([(2, 3), (2, 4)], 'R')
    assert [(4, 3), (3, 3)] == step([(3, 3), (2, 4)], 'R')
    assert [(5, 3), (4, 3)] == step([(4, 3), (3, 3)], 'R')
    assert [(5, 2), (4, 3)] == step([(5, 3), (4, 3)], 'D')
    assert [(4, 2), (4, 3)] == step([(5, 2), (4, 3)], 'L')
    assert [(3, 2), (4, 3)] == step([(4, 2), (4, 3)], 'L')
    assert [(2, 2), (3, 2)] == step([(3, 2), (4, 3)], 'L')
    assert [(1, 2), (2, 2)] == step([(2, 2), (3, 2)], 'L')
    assert [(0, 2), (1, 2)] == step([(1, 2), (2, 2)], 'L')
    assert [(1, 2), (1, 2)] == step([(0, 2), (1, 2)], 'R')
    assert [(2, 2), (1, 2)] == step([(1, 2), (1, 2)], 'R')


def test_all_moves():
    assert [(2, 2), (1, 2)] == last(all_moves(d09_s01, 2))
    assert [(2, 2), (1, 2), (2, 2), (3, 2), (2, 2),
            (1, 1), (0, 0), (0, 0), (0, 0), (0, 0)] == \
        last(all_moves(d09_s01, 10))
    assert [(-11, 15), (-11, 14), (-11, 13), (-11, 12), (-11, 11),
            (-11, 10), (-11, 9), (-11, 8), (-11, 7), (-11, 6)] == \
        last(all_moves(d09_s02, 10))


def test_unique_tail_positions():
    assert {(0, 0), (1, 0), (2, 0), (3, 0), (4, 1),
            (4, 2), (4, 3), (3, 4), (2, 4), (3, 3),
            (3, 2), (2, 2), (1, 2)} == unique_tail_positions(d09_s01, 2)
    assert {(0, 0)} == unique_tail_positions(d09_s01, 10)
    assert {(0, 0), (1, 1), (2, 2), (1, 3), (2, 4), (3, 5),
            (4, 5), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1),
            (10, 0), (9, -1), (8, -2), (7, -3), (6, -4),
            (5, -5), (4, -5), (3, -5), (2, -5), (1, -5),
            (0, -5), (-1, -5), (-2, -5), (-3, -4), (-4, -3),
            (-5, -2), (-6, -1), (-7, 0), (-8, 1), (-9, 2),
            (-10, 3), (-11, 4), (-11, 5), (-11, 6)} == \
        unique_tail_positions(d09_s02, 10)


def test_unique_tail_pos_count():
    assert 13 == unique_tail_pos_count(d09_s01, 2)
    assert 1 == unique_tail_pos_count(d09_s01, 10)
    assert 36 == unique_tail_pos_count(d09_s02, 10)


d09_input = list(parse(standard_puzzle_input(year=2022, day=9)))


def test_day08_part1_soln():
    assert 5874 == part1(d09_input)


def test_day09_part2_soln():
    assert 2467 == part2(d09_input)
