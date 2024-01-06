"""Solution to https://adventofcode.com/2015/day/3"""
import itertools as it
import operator as op
import toolz


# Input parsing
parse = toolz.first


# Puzzle logic
def tuple_add(a, b):
    return tuple(map(op.add, a, b))


def delta(dir):
    match dir:
        case "^": return (0, 1)
        case "v": return (0, -1)
        case ">": return (1, 0)
        case "<": return (-1, 0)


def move_dir(pos, dir):
    return tuple_add(delta(dir), pos)


def houses_visited(directions):
    return it.accumulate(directions, move_dir, initial=(0, 0))


def distinct_houses_visited(directions):
    return len(set(houses_visited(directions)))


# Puzzle solutions:
def part1(input):
    return distinct_houses_visited(input)
