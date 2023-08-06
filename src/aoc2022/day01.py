""" Solution to https://adventofcode.com/2022/day/1"""

from more_itertools import split_at
from pipe import Pipe, map, sort, take
import fileinput
import sys


@Pipe
def split_at_blanklines(lines):
    return split_at(lines, lambda s: not s)


def parse_chunk(chunk):
    return [int(x) for x in chunk]


def parse(input):
    return input | split_at_blanklines | map(parse_chunk)


@Pipe
def sorted_totals(calories):
    return calories | map(sum) | sort(reverse=True)


def top_n_capacity_sum(n, calories):
    return sum(calories | sorted_totals | take(n))


# def day01_part1_soln():
#     return top_n_capacity_sum(1, foo)


# def day01_part2_soln():
#     return top_n_capacity_sum(3, foo)


filename = "/Users/klsmith/Documents/projects/2scientists/aoc-clj/resources/2022/day01-input.txt"


def puzzle_input(filename):
    lines = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

# print(len(list(parse(puzzle_input(filename)))))

# with fileinput.input(files=("2022/2022/dummy.txt")) as f:
#     print(list(f | take(2)))


if __name__ == "__main__":
    input = list(parse(puzzle_input(sys.argv[1])))
    print(top_n_capacity_sum(1, input))
    print(top_n_capacity_sum(3, input))
