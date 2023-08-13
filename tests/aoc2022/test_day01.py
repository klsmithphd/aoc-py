from utils.core import standard_puzzle_input
from aoc2022.day01 import parse, top_n_capacity_sum, day01_part1, day01_part2

d01_s01_raw = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".splitlines()

d01_s01 = list(parse(d01_s01_raw))


def test_parse():
    assert d01_s01 == [[1000, 2000, 3000],
                       [4000],
                       [5000, 6000],
                       [7000, 8000, 9000],
                       [10000]]


def test_top_n_capacity_sum():
    assert 24000 == top_n_capacity_sum(d01_s01, 1)
    assert 45000 == top_n_capacity_sum(d01_s01, 3)


d01_input = standard_puzzle_input(year=2022, day=1)


def test_day01_part1_soln():
    assert 70116 == day01_part1(d01_input)


def test_day01_part2_soln():
    assert 206582 == day01_part2(d01_input)
