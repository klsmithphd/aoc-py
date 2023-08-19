""" Solution to https://adventofcode.com/2022/day/1 """
from collections.abc import Iterable
from pipe import Pipe, map, sort, take
from utils.core import AoCSolution, split_at_blanklines

# Input parsing


def parse_chunk(chunk: Iterable[str]) -> list[int]:
    return [int(x) for x in chunk]


def parse(input: Iterable[str]) -> Iterable[list[int]]:
    return (parse_chunk(x) for x in split_at_blanklines(input))

# Puzzle logic


@Pipe
def sorted_totals(calories: Iterable[list[int]]) -> Iterable[int]:
    """
    Return a collection of all the `calorie` totals, sorted in descending order
    """
    return calories | map(sum) | sort(reverse=True)


def top_n_capacity_sum(calories: Iterable[list[int]], n: int) -> int:
    """
    Return the sum of the top `n` totals
    """
    return sum(calories | sorted_totals | take(n))

# Puzzle solutions


def part1(input: Iterable[list[int]]) -> int:
    """
    Find the Elf carrying the most Calories.
    How many total Calories is that Elf carrying?
    """
    return top_n_capacity_sum(input, n=1)


def part2(input: Iterable[list[int]]) -> int:
    """
    Find the top three Elves carrying the most Calories.
    How many Calories are those Elves carrying in total?
    """
    return top_n_capacity_sum(input, n=3)


day01_soln = AoCSolution(parse, part1, part2)
