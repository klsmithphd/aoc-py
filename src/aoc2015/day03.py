"""Solution to https://adventofcode.com/2015/day/3"""
import itertools as it
import toolz
import utils.vectors as v


# Constants
dir_dict = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}

# Input parsing
parse = toolz.first


# Puzzle logic
def visits(dirs):
    """Convert `dirs` into an iterable of the positions visited"""
    return it.accumulate((dir_dict[x] for x in dirs), v.vec_add, initial=(0, 0))


def split_visits(dirs):
    """Convert `dirs` into an iterable of the positions visited by santa
    first and his robot clone when splitting the directions"""
    return it.chain(visits(it.islice(dirs, 0, None, 2)),
                    visits(it.islice(dirs, 1, None, 2)))


def distinct_visits(dirs, visits):
    """Number of unique positions reached given the collection of `dirs`
    and a function `visits` that knows how to convert those directions
    into positions visited"""
    return len(set(visits(dirs)))


# Puzzle solutions:
def part1(input):
    """Number of distinct houses visted with santa following the directions"""
    return distinct_visits(input, visits)


def part2(input):
    """Number of distinct houses visited with santa/robot splitting the directions"""
    return distinct_visits(input, split_visits)
