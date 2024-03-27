"""Solution to https://adventofcode.com/2015/day/4"""
import itertools as it
import functools as ft
import more_itertools as mit
import utils.digest as dig


# Input parsing
parse = mit.first


# Puzzle logic
def first_int(pred, secret: str):
    """Find the first integer that satisfies the predicate `pred` on the MD5
    digest"""
    return mit.first(i for i in it.count(1)
                     if pred(dig.md5_digest(f"{secret}{i}")))


first_fivezeros_int = ft.partial(first_int, dig.isfivezerostart)
first_sixzeros_int = ft.partial(first_int, dig.issixzerostart)


# Puzzle solutions
def part1(input):
    "Finds the first integer where the MD5 hash starts with five zeros in hex"
    return first_fivezeros_int(input)


def part2(input):
    "Finds the first integer where the MD5 hash starts with six zeros in hex"
    return first_sixzeros_int(input)
