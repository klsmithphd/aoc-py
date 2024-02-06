"""Solution to https://adventofcode.com/2015/day/18"""
# import functools as ft


# Input parsing
def parse(input):
    size = len(input)
    return (size,
            {(x, y)
             for y in range(size)
             for x in range(size)
             if input[y][x] == '#'})


# Puzzle logic
# @ft.cache
def neighbors(x, y):
    return ((nx, ny)
            for ny in range(y-1, y+2)
            for nx in range(x-1, x+2)
            if (nx, ny) != (x, y))


def on_neighbors(lights, x, y):
    return sum(1 for nx, ny in neighbors(x, y) if (nx, ny) in lights)


def step(state):
    size, lights = state
    new_lights = {(x, y)
                  for y in range(size)
                  for x in range(size)
                  if (x, y) in lights and 2 <= on_neighbors(lights, x, y) <= 3
                  or (x, y) not in lights and on_neighbors(lights, x, y) == 3}
    return size, new_lights


# Puzzle solutions
