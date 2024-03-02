"""Solution to https://adventofcode.com/2015/day/25"""
import re
import toolz
import utils.math as math


# Constants
FIRST_CODE = 20151125
MODULUS = 33554393
MULTIPLER = 252533


# Input parsing
def parse(input):
    return [int(x) for x in re.findall(r"\d+", toolz.first(input))]


# Puzzle logic
def lazy_caterer(n):
    """Computes the nth value in the lazy caterer's sequence using the formula
    p = (n^2 + n + 2)/2

    See https://en.wikipedia.org/wiki/Lazy_caterer%27s_sequence

    For this puzzle, the importance of this sequence is that it represents
    the code number for the first element in each row on the infinite sheet
    of paper. """
    return (n*n + n + 2)//2


def code_number(row, col):
    """Returns the code number (from 1 to infinity) that is found on the
    infinite sheet of codes at the given `row` and `col` (both 1-offset)."""

    # Imagine each *tier* is counted starting at row=1, col=1 in the upper-left
    # and then numbered sequentially for each diagonal going from
    # row=n, col=1 to row=1, col=n, i.e. this table depicts the tier value
    # for various row, col pairs:
    #    | 1   2   3   4   5   6
    # ---+---+---+---+---+---+---+
    #  1 |  1   2   3   4   5   6
    #  2 |  2   3   4   5   6   7
    #  3 |  3   4   5   6   7   8
    #  4 |  4   5   6   7   8   9
    #  5 |  5   6   7   8   9  10
    #  6 |  6   7   8   9  10  11

    # The tier then tells us where we are in the lazy caterer's sequence,
    # and then we add in the column offset to get the code number
    return lazy_caterer(row + col - 2) + col - 1


def code(row, col):
    """The code value from the infinite code sheet at the given `row` and `col`,
    (both 1-offset)"""
    code_num = code_number(row, col)-1
    return math.mod_mul(MODULUS, FIRST_CODE,
                        math.mod_pow(MODULUS, MULTIPLER, code_num))


# Puzzle solutions
def part1(input):
    """The code value at the row/col positions (both 1-offset) in the input"""
    return code(*input)
