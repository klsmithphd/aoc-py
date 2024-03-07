"""Solution to https://adventofcode.com/2016/day/3"""
import cardinality


# Input parsing
def parse_line(line: str):
    return tuple(int(x) for x in line.split())


def parse(input):
    return [parse_line(line) for line in input]


# Puzzle logic
def isvalidtriangle(triangle):
    a, b, c = triangle
    return a + b > c and b + c > a and c + a > b


def count_valid(triangles):
    return cardinality.count(x for x in triangles if isvalidtriangle(x))


# Puzzle solutions
def part1(input):
    return count_valid(input)
