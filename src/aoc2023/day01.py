""" Solution to https://adventofcode.com/2023/day/1 """
from re import findall
from utils.core import AoCSolution

# Input parsing


def parse(x):
    return list(x)

# Puzzle logic


def asint(x):
    match x:
        case 'one': return 1
        case 'two': return 2
        case 'three': return 3
        case 'four': return 4
        case 'five': return 5
        case 'six': return 6
        case 'seven': return 7
        case 'eight': return 8
        case 'nine': return 9
        case _: return int(x)


def digits(s, spelled=False):
    if not spelled:
        return [int(x) for x in findall(r'\d', s)]
    else:
        return [asint(x) for x in
                findall('(?=(\d|one|two|three|four|five|six|seven|eight|nine))', s)]


def calibration_value(s, spelled=False):
    digs = digits(s, spelled)
    return digs[0]*10 + digs[-1]


def calibration_value_sum(input, spelled=False):
    return sum(calibration_value(x, spelled) for x in input)

# Puzzle solutions


def part1(input):
    return calibration_value_sum(input)


def part2(input):
    return calibration_value_sum(input, spelled=True)


day01_soln = AoCSolution(parse, part1, part2)
