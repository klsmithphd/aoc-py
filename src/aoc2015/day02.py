"""Solution to https://adventofcode.com/2015/day/2"""


# Input parsing
def parse_line(line: str):
    return tuple(map(int, line.split('x')))


def parse(input):
    return [parse_line(x) for x in input]


# Puzzle-logic
def wrapping_paper_area(box):
    """Computes the total wrapping paper area required for a `box`
    (a tuple of a length, width, and height value). The wrapping paper
    formula is the sum of the areas of all the sides plus an extra
    amount equal to the area of the smallest side"""
    a, b, c = sorted(box)
    return (2 * a * b) + (2 * b * c) + (2 * a * c) + (a * b)


# Puzzle solutions
def part1(input):
    """Computes the total wrapping paper required for all the input"""
    return sum(wrapping_paper_area(x) for x in input)
