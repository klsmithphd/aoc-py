"""Solution to https://adventofcode.com/2022/day/3"""
from functools import reduce, partial
from more_itertools import sliced, chunked
from pipe import map, Pipe
from utils.core import AoCSolution

# Input parsing


def parse(input):
    return input

# Puzzle logic


def split_in_half(s: str):
    return sliced(s, len(s)//2)


def chunked_in_thirds(seq: list[str]):
    return chunked(seq, 3)


def set_intersection(x: set, y: set):
    return x.intersection(y)


def overlap(splits):
    return reduce(set_intersection, splits | map(set)).pop()


def priority(c: str):
    if c.isupper():
        return ord(c) - ord("A") + 27
    else:
        return ord(c) - ord("a") + 1


def overlap_priority_sum(seq, split_half=True):
    chunks = seq | map(split_in_half) if split_half else chunked_in_thirds(seq)
    return sum(chunks | map(overlap) | map(priority))

# Puzzle solutions


day03_soln = \
    AoCSolution(parse,
                p1=overlap_priority_sum,
                p2=partial(overlap_priority_sum, split_half=False))
