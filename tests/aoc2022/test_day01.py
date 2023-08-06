# from aoc2022.day01 import parse, day01_part1_soln, day01_part2_soln, split_at_blanklines
from aoc2022.day01 import parse, top_n_capacity_sum, puzzle_input

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


filename = "/Users/klsmith/Documents/projects/2scientists/aoc-clj/resources/2022/day01-input.txt"
d01_input = list(parse(puzzle_input(filename)))


def test_top_n_capacity_sum():
    assert 24000 == top_n_capacity_sum(1, d01_s01)
    assert 45000 == top_n_capacity_sum(3, d01_s01)


def test_day01_part1_soln():
    assert 70116 == top_n_capacity_sum(1, d01_input)


def test_day01_part2_soln():
    assert 206582 == top_n_capacity_sum(3, d01_input)
