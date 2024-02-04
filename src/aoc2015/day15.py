"""Solution to https://adventofcode.com/2015/day/14"""
import itertools as it
import functools as ft
import operator as op
import re
import utils.vectors as v

# Constants
MAX_TEASPOONS = 100
CALORIE_LIMIT = 500


# Input parsing
def parse_line(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


def parse(input):
    return [parse_line(line) for line in input]


# Puzzle logic
def score_vec(ingredients, quantities):
    """Computes the score component vector, where each element is the 
    sum of the products of each ingredients properties and the quantity
    of that ingredient"""
    amounts = map(v.scalar_mul, ingredients, quantities)
    return [x if x >= 0 else 0 for x in v.vec_sum(amounts)]


def score(score_vec):
    """The cookie score is the product of the first four properties"""
    return ft.reduce(op.mul, score_vec[:-1])


def all_options(total: int, n: int):
    """Returns a sequence of all possible combinations of `n` items
    that sum to `total`"""
    if n == 2:
        return [[(total - x), x] for x in range(total+1)]
    else:
        return [[(total - x)] + sub_option
                for x in range(total+1)
                for sub_option in all_options(x, n-1)]


def max_score(ingredients, cal_constraint=False):
    """Computes the maximum possible score for the given ingredients.
    If `cal_constraint` is `True`, only cookie recipes with exactly 500
    calories are considered"""
    # If cal_constraint is True, filter_fn will return True when
    # exactly 500 calories. For cal_constraint = False, always return True
    def filter_fn(x):
        if cal_constraint:
            return x[4] == CALORIE_LIMIT
        else:
            return True
    # Generate all valid options for the quantities of each ingredient
    options = all_options(MAX_TEASPOONS, len(ingredients))
    # Generate the score component vector for each option
    score_vecs = (score_vec(ingredients, opt) for opt in options)
    # Return the maximum score for each vector, subject to the filter
    return max(score(x) for x in score_vecs if filter_fn(x))


# Puzzle solutions
def part1(input):
    """Computes the maximum cookie score for the given ingredients"""
    return max_score(input)


def part2(input):
    """Computes the maximum cookie score for cookies with exactly 500 calories"""
    return max_score(input, cal_constraint=True)
