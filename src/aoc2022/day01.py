""" Solution to https://adventofcode.com/2022/day/1"""

from utils.core import split_at_blanklines, parse_puzzle_input
from pipe import Pipe, map, sort, take
import sys

# Input parsing


def parse_chunk(chunk):
    return [int(x) for x in chunk]


def parse(input):
    return input | split_at_blanklines | map(parse_chunk)

# Puzzle logic


@Pipe
def sorted_totals(calories):
    return calories | map(sum) | sort(reverse=True)


def top_n_capacity_sum(n, calories):
    return sum(calories | sorted_totals | take(n))

# Puzzle solutions


def day01_part1(input):
    return top_n_capacity_sum(1, input)


def day01_part2(input):
    return top_n_capacity_sum(3, input)


if __name__ == "__main__":
    input = parse_puzzle_input(parse, year=2022, day=1, filename=sys.argv[1])
    print(day01_part1(input))
    print(day01_part2(input))
