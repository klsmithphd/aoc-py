"""Solution to https://adventofcode.com/2015/day/14"""
import re

# Constants
MAX_TEASPOONS = 100
CALORIE_LIMIT = 500


# Input parsing
def parse_line(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


def parse(input):
    return [parse_line(line) for line in input]


# Puzzle logic


# Puzzle solutions
