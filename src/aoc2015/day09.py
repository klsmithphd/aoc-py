"""Solution to https://adventofcode.com/2015/day/9"""
import itertools as it
import toolz


# Input parsing
def parse_line(line: str):
    a, _, b, _, c = line.split()
    return [(a, b, int(c)), (b, a, int(c))]


def parse(input):
    dists = sorted(it.chain.from_iterable(parse_line(line) for line in input))
    return {k: {b: c for _, b, c in g} for k, g in it.groupby(dists, toolz.first)}
