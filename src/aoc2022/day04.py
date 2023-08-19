"""Solution to https://adventofcode.com/2022/day/4"""
from pipe import map
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


def overlapping_count(input):
    return sum(1 for x in input if isoverlapping(*x))

# Puzzle solutions


def part1(input):
    """
    In how many assignment pairs does one range fully contain the other?
    """
    return fully_contained_count(input)


def part2(input):
    """
    In how many assignment pairs do the ranges overlap?
    """
    return overlapping_count(input)


day04_soln = AoCSolution(parse, part1, part2)