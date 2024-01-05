"""Solution to https://adventofcode.com/2015/day/1"""
import collections
import itertools as it

# Input parsing
mapping = {'(': 1, ')': -1}


def parse(input):
    return [mapping[x] for x in input[0]]


# Puzzle logic
def final_floor(input):
    return sum(input)


# From https://github.com/wbolster/cardinality
def count(iter):
    d = collections.deque(enumerate(iter, 1), maxlen=1)
    return d[0][0] if d else 0


def first_time_in_basement(input):
    return count(it.takewhile(lambda x: x != -1, it.accumulate(input))) + 1
