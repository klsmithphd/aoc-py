"""Solution to https://adventofcode.com/2015/day/18"""
import functools as ft
import itertools as it
import more_itertools as mit


# Constants
ITERATIONS = 100


# Input parsing
@ft.cache
def grid(size):
    return [(x, y) for y in range(size) for x in range(size)]


def parse(input):
    contents = list(input)
    size = len(contents)
    return (size, {(x, y) for x, y in grid(size) if contents[y][x] == '#'})


# Puzzle logic
@ft.cache
def neighbors(x, y):
    return [(nx, ny)
            for ny in range(y-1, y+2)
            for nx in range(x-1, x+2)
            if (nx, ny) != (x, y)]


def on_neighbors(lights, x, y):
    return sum(1 for nx, ny in neighbors(x, y) if (nx, ny) in lights)


@ft.cache
def corners(size):
    return {(0, 0), (size-1, 0), (0, size-1), (size-1, size-1)}


def step(state, corners_on=False):
    size, lights = state
    new_lights = {(x, y) for x, y in grid(size)
                  if (x, y) in lights and 2 <= on_neighbors(lights, x, y) <= 3
                  or (x, y) not in lights and on_neighbors(lights, x, y) == 3}
    return size, new_lights | corners(size) if corners_on else new_lights


def lights_at_n(state, n, corners_on=False):
    seq = mit.iterate(lambda x: step(x, corners_on), state)
    return len(next(it.islice(seq, n, n+1))[1])


# Puzzle solutions
def part1(input):
    return lights_at_n(input, ITERATIONS)


def part2(input):
    size, lights = input
    adj_input = (size, corners(size) | lights)
    return lights_at_n(adj_input, ITERATIONS, corners_on=True)
