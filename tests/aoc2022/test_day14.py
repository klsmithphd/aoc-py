from aoc2022.day14 import parse, rocks
from utils.core import standard_puzzle_input

d14_s0_raw = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()

d14_s0 = [[(498, 4), (498, 6), (496, 6)],
          [(503, 4), (502, 4), (502, 9), (494, 9)]]


def test_parse():
    assert d14_s0 == parse(d14_s0_raw)


def test_rocks():
    assert {(498, 4),
            (498, 5),
            (498, 6),
            (497, 6),
            (496, 6),
            (503, 4),
            (502, 4),
            (502, 5),
            (502, 6),
            (502, 7),
            (502, 8),
            (502, 9),
            (501, 9),
            (500, 9),
            (499, 9),
            (498, 9),
            (497, 9),
            (496, 9),
            (495, 9),
            (494, 9)} == rocks(d14_s0)

# d14_input = standard_puzzle_input(year=2022, day=14)


# def test_day14_part1_soln():
#     assert 1 == day14_soln.part1(d14_input)


# def test_day14_part2_soln():
#     assert 1 == day14_soln.part2(d14_input)
