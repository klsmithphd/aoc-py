""" Solution to https://adventofcode.com/2022/day/1 """
from functools import partial
from pipe import Pipe, map, sort, take
from utils.core import AoCSolution, split_at_blanklines

# Input parsing


def parse_chunk(chunk):
    return [int(x) for x in chunk]


def parse(input):
    return input | split_at_blanklines | map(parse_chunk)

# Puzzle logic


@Pipe
def sorted_totals(calories):
    """
    Return a collection of all the `calorie` totals, sorted in descending order
    """
    return calories | map(sum) | sort(reverse=True)


def top_n_capacity_sum(calories, n):
    """
    Return the sum of the top `n` totals
    """
    return sum(calories | sorted_totals | take(n))

# Puzzle solutions


day01_soln = \
    AoCSolution(
        parse,
        # Find the Elf carrying the most Calories.
        # How many total Calories is that Elf carrying?
        p1=partial(top_n_capacity_sum, n=1),
        # Find the top three Elves carrying the most Calories.
        # How many Calories are those Elves carrying in total?
        p2=partial(top_n_capacity_sum, n=3))
