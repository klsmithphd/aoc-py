"""Solution to https://adventofcode.com/2015/day/1"""
import cardinality
import itertools as it
import toolz

# Input parsing
mapping = {'(': 1, ')': -1}


def parse(input):
    return [mapping[x] for x in toolz.first(input)]


# Puzzle logic
def final_floor(input):
    """Compute the final floor as the sum of all the up and down moves."""
    return sum(input)


def first_time_in_basement(input):
    """Determine the first time the elevator reaches the basement by counting
    how many moves it takes until the sum becomes -1."""
    floors_until_neg = it.takewhile(lambda x: x != -1, it.accumulate(input))
    return cardinality.count(floors_until_neg) + 1


# Puzzle logic
def part1(input):
    """Given a list of `1`s and `-1`s, each representing an elevator moving
    up or down one floor, return the floor reached at the end of the moves."""
    return final_floor(input)


def part2(input):
    """Given the same list of `1`s and `-1`s, each representing an elevator 
    moving up or down one floor, return the position of the first move in the
    sequence where the elevator reaches the basement (at -1)."""
    return first_time_in_basement(input)
