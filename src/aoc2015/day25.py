"""Solution to https://adventofcode.com/2015/day/25"""
import re
import toolz


# Constants
FIRST_CODE = 20151125
MODULUS = 33554393
MULTIPLER = 252533


# Input parsing
def parse(input):
    return [int(x) for x in re.findall(r"\d+", toolz.first(input))]
