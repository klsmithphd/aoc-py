""" Solution to https://adventofcode.com/2022/day/1"""
from utils.core import split_at_blanklines
from pipe import Pipe, map, sort, take


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


def top_n_capacity_sum(n, calories):
    """
    Return the sum of the top `n` totals
    """
    return sum(calories | sorted_totals | take(n))

# Puzzle solutions


def day01_part1(input):
    """
    Find the Elf carrying the most Calories. 
    How many total Calories is that Elf carrying?
    """
    return top_n_capacity_sum(1, input)


def day01_part2(input):
    """
    Find the top three Elves carrying the most Calories. 
    How many Calories are those Elves carrying in total?
    """
    return top_n_capacity_sum(3, input)
