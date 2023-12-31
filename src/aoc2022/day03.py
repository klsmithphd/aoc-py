"""Solution to https://adventofcode.com/2022/day/3"""
from functools import reduce
from more_itertools import sliced, chunked
from pipe import map

# Input parsing


def parse(input):
    return input

# Puzzle logic


def split_in_half(seq):
    """
    Divide a sequence into two, cut at the midpoint
    """
    return sliced(seq, len(seq)//2)


def chunked_in_thirds(seq):
    """
    Divide a sequence into chunks of size 3 elements
    """
    return chunked(seq, 3)


def overlap(splits):
    """
    For a collection of items `splits`, find the (asssumed) sole value
    that they all have in common
    """
    return reduce(set.intersection, splits | map(set)).pop()


def priority(c: str):
    """
    Lowercase item types `a` through `z` have priorities 1 through 26.
    Uppercase item types `A` through `Z` have priorities 27 through 52.
    """
    if c.isupper():
        return ord(c) - ord("A") + 27
    else:
        return ord(c) - ord("a") + 1


def overlap_priority_sum(seq, part1=True):
    """
    Using the item-to-priority value mapping, compute the sum of the
    priorities, using the logic for splitting in half for part1 or grouping
    by thirds for part2"
    """
    chunks = seq | map(split_in_half) if part1 else chunked_in_thirds(seq)
    return sum(chunks | map(overlap) | map(priority))

# Puzzle solutions


def part1(input):
    """
    Find the item type that appears in both compartments of each
    rucksack. What is the sum of the priorities of those item types?
    """
    return overlap_priority_sum(input, part1=True)


def part2(input):
    """
    Find the item type that corresponds to the badges of each three-Elf
    group. What is the sum of the priorities of those item types?
    """
    return overlap_priority_sum(input, part1=False)
