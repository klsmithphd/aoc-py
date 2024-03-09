"""Solution to https://adventofcode.com/2016/day/3"""
import cardinality
import itertools as it
import more_itertools as mit


# Input parsing
def parse_line(line: str):
    return tuple(int(x) for x in line.split())


def parse(input):
    return [parse_line(line) for line in input]


# Puzzle logic
def isvalidtriangle(triangle):
    """A triangle is valid if the sum of two sides are strictly greater than
    the remaining side"""
    a, b, c = triangle
    return a + b > c and b + c > a and c + a > b


def count_valid(triangles):
    """Count of triangles considered valid"""
    return cardinality.count(x for x in triangles if isvalidtriangle(x))


def groupby_columns(triangles):
    """Re-interpret the data with triangles spanning three consecutive rows
    in the same column"""
    return it.chain(*(zip(*a) for a in mit.batched(triangles, 3)))


# Puzzle solutions
def part1(input):
    """How many triangles are valid"""
    return count_valid(input)


def part2(input):
    """How many triangles are valid re-interpreting the data as spanning 3 rows"""
    return count_valid(groupby_columns(input))
