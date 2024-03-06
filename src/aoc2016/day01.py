"""Solution to https://adventofcode.com/2016/day/1"""
import itertools as it
import functools as ft
import more_itertools as mit
import toolz
import utils.grid as grid
import utils.vectors as v

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
    """Given an instruction to turn and then move forward a certain distance,
    determine the new state of the walker"""
    bearing, dist = inst
    return grid.forward(grid.turn(state, bearing), dist)


def move(insts):
    """Given all the instructions, determine the final state of the walker"""
    return ft.reduce(step, insts, START)


def distance(insts):
    """Compute the Manhattan distance from the starting point after following
    the instructions"""
    return v.manhattan(ORIGIN, move(insts)['pos'])


def all_points(insts):
    """Determine all the points passed through by the walker following
    the instructions"""
    endpoints = (p['pos'] for p in it.accumulate(insts, step, initial=START))
    all_pts = (grid.interpolated(*pair) for pair in it.pairwise(endpoints))
    return mit.unique_justseen(it.chain(*all_pts))


def first_duplicate(points):
    """Given a collection, find the first element that's a duplicate of
    any element earlier in the collection."""
    return toolz.first(mit.duplicates_everseen(points))


def distance_to_first_duplicate(insts):
    """Manhattan distance to the first location visited twice"""
    first_dupe = first_duplicate(all_points(insts))
    return v.manhattan(ORIGIN, first_dupe)


# Puzzle solutions
def part1(input):
    """Distance to Easter Bunny HQ given the instructions"""
    return distance(input)


def part2(input):
    """Distance to first location visited twice given the instructions"""
    return distance_to_first_duplicate(input)
