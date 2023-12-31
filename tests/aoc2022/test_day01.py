from aoc2022.day01 import parse, part1, part2, top_n_capacity_sum
from utils.core import standard_puzzle_input

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

d01_s01 = parse(d01_s01_raw)
d01_input = parse(standard_puzzle_input(year=2022, day=1))


def test_parse():
    assert d01_s01 == [[1000, 2000, 3000],
                       [4000],
                       [5000, 6000],
                       [7000, 8000, 9000],
                       [10000]]


def test_top_n_capacity_sum():
    assert 24000 == top_n_capacity_sum(d01_s01, 1)
    assert 45000 == top_n_capacity_sum(d01_s01, 3)


def test_day01_part1_soln():
    assert 70116 == part1(d01_input)


def test_day01_part2_soln():
    assert 206582 == part2(d01_input)
