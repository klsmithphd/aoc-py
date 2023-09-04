"""Solution to https://adventofcode.com/2022/day/8"""
# from utils.core import AoCSolution
from more_itertools import flatten


# Input parsing


def parse(input):
    return [[int(x) for x in line] for line in input]

# Puzzle logic


def transpose(m):
    return [list(col) for col in zip(*m)]


def greatest_so_far(row):
    mx = -1
    for x in row:
        if x > mx:
            mx = x
            yield 1
        else:
            yield 0


def trees_visible_from_left(row):
    return list(greatest_so_far(row))


def trees_visible_in_row(row):
    return list(map(lambda a, b: a or b,
                    trees_visible_from_left(row),
                    reversed(trees_visible_from_left(reversed(row)))))


def trees_visible_horiz(grid):
    return [trees_visible_in_row(row) for row in grid]


def trees_visible_count(grid):
    return sum(map(lambda a, b: a or b,
                   flatten(trees_visible_horiz(grid)),
                   flatten(transpose(trees_visible_horiz(transpose(grid))))))


# Puzzle solutions

def part1(input):
    return trees_visible_count(input)

# day08_soln = \
#     AoCSolution(parse,
#                 p1=
#                 p2=)
