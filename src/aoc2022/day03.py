"""Solution to https://adventofcode.com/2022/day/3"""
from more_itertools import sliced
from pipe import map, Pipe
from utils.core import AoCSolution

# Input parsing


def parse(input):
    return input

# Puzzle logic


def split_in_half(s: str):
    return sliced(s, len(s)//2)


def overlap(splits):
    s1, s2 = splits
    return set(s1).intersection(set(s2)).pop()


def overlaps(splits_seq):
    return splits_seq | map(overlap)


def priority(c: str):
    if c.isupper():
        return ord(c) - ord("A") + 27
    else:
        return ord(c) - ord("a") + 1


def overlap_priority_sum(seq):
    return sum(seq | map(split_in_half) | map(overlap) | map(priority))

# Puzzle solutions


day03_soln = \
    AoCSolution(parse,
                p1=overlap_priority_sum,
                p2=overlap_priority_sum)
