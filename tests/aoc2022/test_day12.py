from aoc2022.day12 import parse, \
    find_matches, transitions, shortest_path_from_start
from utils.core import standard_puzzle_input
from utils.grid.listgrid2d import ListGrid2D

d12_s0_raw = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()

d12_s0 = ListGrid2D([[-1, 0, 1, 16, 15, 14, 13, 12],
                     [0,  1, 2, 17, 24, 23, 23, 11],
                     [0,  2, 2, 18, 25, 26, 23, 10],
                     [0,  2, 2, 19, 20, 21, 22,  9],
                     [0,  1, 3,  4,  5,  6,  7,  8]])


def test_parse():
    assert d12_s0 == parse(d12_s0_raw)


def test_find_matches():
    assert {(0, 0)} == set(find_matches(d12_s0, -1))
    assert {(1, 0), (0, 1), (0, 2), (0, 3), (0, 4)} == \
        set(find_matches(d12_s0, 0))


def test_transitions():
    assert ((0, 0), {(1, 0): 1, (0, 1): 1}) == transitions(d12_s0, (0, 0))
    assert ((0, 1), {(0, 2): 1, (1, 1): 1, (0, 0): 1}) == \
        transitions(d12_s0, (0, 1))


def test_shortest_path_length():
    assert 31 == shortest_path_from_start(d12_s0)
# d12_input = standard_puzzle_input(year=2022, day=12)


# def test_day12_part1_soln():
#     assert 1 == day12_soln.part1(d12_input)


# def test_day12_part2_soln():
#     assert 1 == day12_soln.part2(d12_input)
