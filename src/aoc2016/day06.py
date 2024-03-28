"""Solution to https://adventofcode.com/2016/day/6"""
import functools as ft
import pipe as p
from collections import Counter

# Input parsing
parse = list


# Puzzle logic
def max_key(c: Counter):
    """Returns the character with the greatest frequency of occurrence"""
    return c.most_common()[0][0]


def min_key(c: Counter):
    """Returns the character with the least frequency of occurrence"""
    return c.most_common()[-1][0]


def frequent_chars(minmax_fn, codes):
    """A string of the most or least frequent characters in each column of
    the code strings"""
    return "".join(
        zip(*codes)
        | p.map(Counter)
        | p.map(minmax_fn)
    )


most_frequent_chars = ft.partial(frequent_chars, max_key)
least_frequent_chars = ft.partial(frequent_chars, min_key)


# Puzzle solutions
def part1(input):
    "The string composed of the most frequent character in each column"
    return most_frequent_chars(input)


def part2(input):
    "The string composed of the least frequent character in each column"
    return least_frequent_chars(input)
