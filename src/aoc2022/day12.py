"""Solution to https://adventofcode.com/2022/day/12"""
from utils.grid.grid2d import Grid2D
from utils.grid.listgrid2d import strings_to_ListGrid2D
# from utils.core import AoCSolution

# Input parsing


def translate(char):
    match char:
        case 'S':
            return -1
        case 'E':
            return 26
        case _:
            return ord(char) - ord('a')


def parse(input):
    return strings_to_ListGrid2D(translate, input)

# Puzzle logic


def find_matches(grid: Grid2D, value):
    return [pos for pos in grid.positions() if grid.value(pos) == value]


def transitions(grid: Grid2D, pos):
    node = grid.value(pos)
    candidates = grid.neighbors4(pos)
    allowed = [x for x in candidates if grid.value(x)-node <= 1]


# Puzzle solutions

# day12_soln = \
#     AoCSolution(parse,
#                 p1=
#                 p2=)
