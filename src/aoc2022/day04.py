"""Solution to https://adventofcode.com/2022/day/4"""
from pipe import map, filter
from utils.core import AoCSolution

# Input parsing


def parse_range(rnge):
    l, r = rnge.split("-")
    return [int(l), int(r)]


def parse_line(line):
    return [parse_range(x) for x in line.split(",")]


def parse(input):
    return input | map(parse_line)

# Puzzle logic


def isfully_contained(i1, i2):
    l1, r1 = i1
    l2, r2 = i2
    #     l1-r1
    # l2----------r2
    # OR
    # l1----------r1
    #     l2--r2
    return (l2 <= l1 <= r1 <= r2) or \
           (l1 <= l2 <= r2 <= r1)


def isoverlapping(i1, i2):
    l1, r1 = i1
    l2, r2 = i2
   # l1-----r1
   #     l2------r2
   # OR
   #       l1-----r1
   # l2------r2
   # OR
   #     l1-r1
   # l2----------r2
   # OR
   # l1----------r1
   #     l2--r2
    return (l1 <= l2 <= r1 <= r2) or \
           (l2 <= l1 <= r2 <= r1) or \
           (l2 <= l1 <= r1 <= r2) or \
           (l1 <= l2 <= r2 <= r1)


def fully_contained_count(input):
    return sum(1 for x in input if isfully_contained(*x))
    # return len(list(input | filter(lambda row: isfully_contained(*row))))


def overlapping_count(input):
    return sum(1 for x in input if isoverlapping(*x))

# Puzzle solutions


day04_soln = \
    AoCSolution(parse,
                p1=fully_contained_count,
                p2=overlapping_count)
