""" Common utilities for many Advent of Code solutions """

from more_itertools import split_at
from pipe import Pipe


def input_path(year: int, day: int) -> str:
    """
    Returns the relative path to the puzzle input for a given year and day.

    This assumes that puzzle input files are stored in the `inputs` directory,
    in a sub-directory per year, and each file is named according to the
    convention `dayNN-input.txt`
    """
    return f"inputs/{year}/day{day:02}-input.txt"


def puzzle_input(filename):
    """ 
    Load a puzzle input from the provided filename, returning a list of the
    lines of the input as strings
    """
    lines = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def parse_puzzle_input(parse, year=None, day=None, filename=None):
    """
    Load and parse a puzzle input for the given `year` and `day`, 
    using the `parse` function provided.

    This expects that all files 
    """
    fname = input_path(year, day) if year and day else filename
    return list(parse(puzzle_input(fname)))


@Pipe
def split_at_blanklines(lines):
    """
    Split a list of items into groups when separated by blank (empty) lines
    """
    return split_at(lines, lambda s: s == "")
