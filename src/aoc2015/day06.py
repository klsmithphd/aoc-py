"""Solution to https://adventofcode.com/2015/day/6"""
import cardinality
import collections
import functools
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
    return [[0 for x in range(1000)] for y in range(1000)]


toggle = {0: 1, 1: 0}


def part1_update(grid, cmd, x, y):
    match cmd:
        case "turn on":  grid[y][x] = 1
        case "turn off": grid[y][x] = 0
        case "toggle":   grid[y][x] = toggle[grid[y][x]]


def dec_min_zero(x):
    return 0 if x == 0 else x-1


def part2_update(grid, cmd, x, y):
    match cmd:
        case "turn on":  grid[y][x] += 1
        case "turn off": grid[y][x] = dec_min_zero(grid[y][x])
        case "toggle":   grid[y][x] += 2


def update_grid(update_fn, grid, instruction):
    cmd, start, end = instruction
    sx, sy = start
    ex, ey = end
    for y in range(sy, ey+1):
        for x in range(sx, ex+1):
            update_fn(grid, cmd, x, y)
    return grid


def brightness(grid):
    return sum(it.chain(*grid))


# Puzzle solutions
def part1(input):
    update = functools.partial(update_grid, part1_update)
    return brightness(functools.reduce(update, input, init_grid()))


def part2(input):
    update = functools.partial(update_grid, part2_update)
    return brightness(functools.reduce(update, input, init_grid()))
