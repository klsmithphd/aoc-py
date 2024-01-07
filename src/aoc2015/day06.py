"""Solution to https://adventofcode.com/2015/day/6"""
import collections
import functools as ft
import itertools as it
import re


# Input parsing
Instruction = collections.namedtuple("Instruction", ["cmd", "start", "end"])
pattern = r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)"


def parse_line(line: str):
    a, b, c, d, e = re.findall(pattern, line)[0]
    return Instruction(a, (int(b), int(c)), (int(d), int(e)))


def parse(input):
    return [parse_line(line) for line in input]


# Puzzle logic
def init_grid():
    """Constructs a 1000 x 1000 list of lists filled with zeroes"""
    return [[0 for _ in range(1000)] for _ in range(1000)]


def part1_update(cmd, val):
    """Updates the light value using the logic of part 1"""
    match cmd:
        case "turn on": return 1
        case "turn off": return 0
        case "toggle": return val ^ 1


def part2_update(cmd, val):
    """Updates the light value using the logic of part 2"""
    match cmd:
        case "turn on": return val + 1
        case "turn off": return val - 1 if val > 0 else 0
        case "toggle": return val + 2


def update_grid_mutable(update_fn, grid, instruction):
    """An implementation of the solution that mutates the values in place.

    This solution is roughly twice as fast as the `update_grid_immutable`
    solution below because it doesn't involve any creation of new lists
    or copying values into them."""
    cmd, start, end = instruction
    sx, sy = start
    ex, ey = end
    for y in range(sy, ey+1):
        for x in range(sx, ex+1):
            grid[y][x] = update_fn(cmd, grid[y][x])
    return grid


def update_slice(up_fn, start, end, lst):
    """Update a subset (slice) of the values in a list from start (inclusive)
    to end (exclusive)"""
    return lst[:start] + [up_fn(i) for i in lst[start:end]] + lst[end:]


def update_grid_immutable(update_fn, grid, instruction):
    """Updates the `grid` according to the `instruction` using the 
    interpretation of the `update_fn`"""
    cmd, start, end = instruction
    sx, sy = start
    ex, ey = end
    # This partial function updates the x-values within a y-slice
    update_row = ft.partial(update_slice, ft.partial(update_fn, cmd), sx, ex+1)
    return update_slice(update_row, sy, ey+1, grid)


def brightness(grid):
    "Computes the overall brightness of the grid (sum of all the light values)"
    return sum(it.chain(*grid))


# Puzzle solutions
def part1(input):
    "How many lights are on using the interpretation of part1"
    update = ft.partial(update_grid_immutable, part1_update)
    return brightness(ft.reduce(update, input, init_grid()))


def part2(input):
    "Total brightness of the lights using the interpretation in part2s"
    update = ft.partial(update_grid_immutable, part2_update)
    return brightness(ft.reduce(update, input, init_grid()))
