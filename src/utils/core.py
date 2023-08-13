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


def puzzle_input(filename) -> list[str]:
    """ 
    Load a puzzle input from the provided filename, returning a list of the
    lines of the input as strings
    """
    lines = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def standard_puzzle_input(year: int, day: int) -> list[str]:
    """ 
    Load a puzzle input for the given `year` and `day`, assuming that
    all puzzle inputs are stored in the `inputs` directory, in a 
    sub-directory per year, and each file is named according to the
    convention `dayNN-input.txt`
    """
    return puzzle_input(input_path(year, day))


@Pipe
def split_at_blanklines(lines):
    """
    Split a list of items into groups when separated by blank (empty) lines
    """
    return split_at(lines, lambda s: s == "")
