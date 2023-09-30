"""Solution to https://adventofcode.com/2022/day/14"""
from more_itertools import flatten, sliding_window
# from utils.core import AoCSolution

# Input parsing


def parse_line(line: str):
    return [tuple(map(int, coord.split(","))) for coord in line.split(" -> ")]


def parse(input):
    return [parse_line(line) for line in input]

# Puzzle logic


def points(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    dy = 1 if y1 <= y2 else -1
    dx = 1 if x1 <= x2 else -1
    return [(x, y) for x in range(x1, x2+dx, dx) for y in range(y1, y2+dy, dy)]


def trace_lines(line):
    return flatten(points(*x) for x in sliding_window(line, 2))


def rocks(input):
    return set(flatten(trace_lines(line) for line in input))


# Puzzle solutions

# day14_soln = \
#     AoCSolution(parse,
#                 p1=
#                 p2=)
