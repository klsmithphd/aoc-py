"""Solution to https://adventofcode.com/2016/day/14"""
import re
import more_itertools as mit
import utils.digest as dig


# Input parsing
parse = mit.first


# Puzzle logic
def hastriplechars(s: str):
    return re.match(r"(.)\1{2}", s)

