""" Solution to https://adventofcode.com/2023/day/1 """
from re import findall
from utils.core import AoCSolution

# Input parsing


def parse(x):
    return x

# Puzzle logic


def digits(s):
    return [int(x) for x in findall(r'\d', s)]


def calibration_value(s):
    digs = digits(s)
    return digs[0]*10 + digs[-1]


def calibration_value_sum(input):
    return sum(calibration_value(x) for x in input)

# Puzzle solutions


def part1(input):
    return calibration_value_sum(input)


def part2(input):
    pass


day01_soln = AoCSolution(parse, part1, part2)
