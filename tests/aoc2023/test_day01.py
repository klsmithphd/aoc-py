from aoc2023.day01 import parse, part1, part2, digits, calibration_value, \
    calibration_value_sum
from utils.core import standard_puzzle_input

d01_s01 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()

d01_s02 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()


def test_parse():
    assert d01_s01 == parse(d01_s01)


def test_digits():
    assert [1, 2] == digits(d01_s01[0])
    assert [3, 8] == digits(d01_s01[1])
    assert [1, 2, 3, 4, 5] == digits(d01_s01[2])
    assert [7] == digits(d01_s01[3])

    assert [2, 1, 9] == digits(d01_s02[0], spelled=True)
    assert [8, 2, 3] == digits(d01_s02[1], spelled=True)
    assert [1, 2, 3] == digits(d01_s02[2], spelled=True)
    assert [2, 1, 3, 4] == digits(d01_s02[3], spelled=True)
    assert [4, 9, 8, 7, 2] == digits(d01_s02[4], spelled=True)
    assert [1, 8, 2, 3, 4] == digits(d01_s02[5], spelled=True)
    assert [7, 6] == digits(d01_s02[6], spelled=True)


def test_calibration_value():
    assert [12, 38, 15, 77] == [calibration_value(x) for x in d01_s01]
    assert [29, 83, 13, 24, 42, 14, 76] == \
        [calibration_value(x, spelled=True) for x in d01_s02]


def test_calibration_value_sum():
    assert 142 == calibration_value_sum(d01_s01)
    assert 281 == calibration_value_sum(d01_s02, spelled=True)


d01_input = parse(standard_puzzle_input(year=2023, day=1))


def test_day01_part1_soln():
    assert 55172 == part1(d01_input)


def test_day01_part2_soln():
    assert 54925 == part2(d01_input)
