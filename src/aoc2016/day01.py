"""Solution to https://adventofcode.com/2016/day/1"""
import functools as ft
import toolz
import utils.grid as grid

# Constants
ORIGIN = (0, 0)
START = {'pos': ORIGIN, 'heading': 'n'}


# Input parsing
def parse_instruction(inst: str):
    bearing = "right" if inst[:1] == "R" else "left"
    dist = int(inst[1:])
    return (bearing, dist)


def parse(input):
    return [parse_instruction(i) for i in toolz.first(input).split(", ")]


# Puzzle logic
def step(state, inst):
    bearing, dist = inst
    return grid.forward(grid.turn(state, bearing), dist)


def move(instructions):
    return ft.reduce(step, instructions, START)


# Puzzle solutions
