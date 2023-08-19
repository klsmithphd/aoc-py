"""Common utilities for many Advent of Code solutions"""
from collections.abc import Iterable
from more_itertools import split_at, with_iter
from pathlib import Path


class AoCSolution():
    """Simple wrapper class for Advent of Code solutions"""

    def __init__(self, parse, part1, part2):
        self.__parse = parse
        self.__part1 = part1
        self.__part2 = part2

    def parse(self, input: Iterable[str]):
        "Parse the raw input into a data structure useful for the puzzle"
        return self.__parse(input)

    def part1(self, input):
        "Return the part1 solution for the day's puzzle, given `input`"
        return self.__part1(self.parse(input))

    def part1_doc(self):
        "Return the description of the solution for part1"
        return self.__part1.__doc__

    def part2(self, input):
        "Return the part2 solution for the day's puzzle, given `input`"
        return self.__part2(self.parse(input))

    def part2_doc(self):
        "Return the description of the solution for part2"
        return self.__part2.__doc__


def input_path(year: int, day: int) -> Path:
    """
    Returns the relative path to the puzzle input for a given year and day.

    This assumes that puzzle input files are stored in the `inputs` directory,
    in a sub-directory per year, and each file is named according to the
    convention `dayNN-input.txt`
    """
    return Path(f"inputs/{year}/day{day:02}-input.txt")


def puzzle_input_iter(path: Path) -> Iterable[str]:
    """ 
    Load a puzzle input from the provided `path`, returning an iterator over
    the lines of the input as strings
    """
    return (line.rstrip() for line in with_iter(open(path)))


def puzzle_input(path: Path) -> list[str]:
    """ 
    Load a puzzle input from the provided `path`, returning a list of the
    lines of the input as strings
    """
    return [line for line in puzzle_input_iter(path)]


def standard_puzzle_input(year: int, day: int) -> list[str]:
    """ 
    Load a puzzle input for the given `year` and `day`, assuming that
    all puzzle inputs are stored in the `inputs` directory, in a 
    sub-directory per year, and each file is named according to the
    convention `dayNN-input.txt`
    """
    return puzzle_input(input_path(year, day))


def split_at_blanklines(lines: Iterable[str]) -> Iterable[list[str]]:
    """
    Split a list of items into groups when separated by blank (empty) lines
    """
    return split_at(lines, lambda s: s == "")
