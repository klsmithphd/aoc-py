"""Solution to https://adventofcode.com/2015/day/14"""
import itertools as it
import functools as ft
import operator as op
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
def score_vec(ingredients, quantities):
    """Computes the score component vector, where each element is the 
    sum of the products of each ingredients properties and the quantity
    of that ingredient"""
    def scalar_mult(ing, qty): return [i*qty for i in ing]
    amounts = map(scalar_mult, ingredients, quantities)
    return [x if x >= 0 else 0 for x in map(sum, zip(*amounts))]


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


def max_score(ingredients):
    """Computes the maximum possible score for the given ingredients."""
    options = all_options(MAX_TEASPOONS, len(ingredients))
    score_vecs = (score_vec(ingredients, opt) for opt in options)
    return max(score(x) for x in score_vecs)
    # return max(score(score_vec(ingredients, opt)) for opt in all_options(MAX_TEASPOONS, len(ingredients)))


# Puzzle solutions
def part1(input):
    """Computes the maximum cookie score for the given ingredients"""
    return max_score(input)
