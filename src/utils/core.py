"""Common utilities for many Advent of Code solutions"""
from collections.abc import Iterable
from pathlib import Path
import itertools as it
import more_itertools as mit
import toolz


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
    return (line.rstrip() for line in mit.with_iter(open(path)))


def puzzle_input(path: Path) -> list[str]:
    """ 
    Load a puzzle input from the provided `path`, returning a list of the
    lines of the input as strings
    """
    return [line for line in puzzle_input_iter(path)]


def standard_puzzle_input(year: int, day: int) -> Iterable[str]:
    """ 
    Load a puzzle input for the given `year` and `day` from the standard
    location, returning an iterator over the lines of the input file as strings
    """
    return puzzle_input_iter(input_path(year, day))


def isequal(x):
    """Returns a function that will test for equality with `x` """
    return lambda y: y == x


def split_at_blanklines(lines: Iterable[str]) -> Iterable[list[str]]:
    """
    Split a list of items into groups when separated by blank (empty) lines
    """
    return mit.split_at(lines, isequal(""))


def isnotnone(x):
    """Returns True if the argument `x` is not None"""
    return x is not None


def index_of(pred, coll):
    """Returns the index of the first item `x` in `coll` that satisfies 
    `pred(x) == True`.

    Only returns the index of the first match, even if there are multiple
    matches. Returns `None` if no element satisfies the predicate."""
    try:
        return toolz.first(i[0] for i in enumerate(coll) if pred(i[1]))
    except StopIteration:
        return None


def iter_equals(iter1, iter2):
    """Checks whether two iterators return the same elements. 

    WARNING: This will exhaust both iterators, so make sure that they aren't 
    needed again!"""
    return all(a == b for a, b in it.zip_longest(iter1, iter2, fillvalue=object()))


def iter_peek(iterator):
    """For any iterator/generator, returns the first element and a new iterator
    that represents all the elements of the original"""
    first = next(iterator)
    return first, it.chain([first], iterator)
