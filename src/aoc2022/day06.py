"""Solution to https://adventofcode.com/2022/day/6"""
from toolz import sliding_window, isdistinct, first
from utils.core import AoCSolution

# Input parsing


def parse(input):
    return first(input)


# Puzzle logic


def chars_to_distinct_run(len, s):
    """
    Returns the number of characters that need to be examined before 
    finding a run of `len` distinct characters in the string `s`
    """
    windows = enumerate(sliding_window(len, s))
    return len + first(x[0] for x in windows if isdistinct(x[1]))


# Puzzle solutions


def part1(input):
    """
    How many characters need to be processed before the first 
    start-of-packet marker is detected?
    """
    return chars_to_distinct_run(4, input)


def part2(input):
    """
    How many characters need to be processed before the first 
    start-of-message marker is detected?
    """
    return chars_to_distinct_run(14, input)


day06_soln = AoCSolution(parse, part1, part2)
