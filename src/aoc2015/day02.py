"""Solution to https://adventofcode.com/2015/day/2"""


# Input parsing
def parse_line(line: str):
    return tuple(sorted(map(int, line.split('x'))))


def parse(input):
    return [parse_line(x) for x in input]


# Puzzle-logic
def wrapping_paper_area(a, b, c):
    """Computes the wrapping paper area given the three dimensions of a box.

    The dimensions must be already ordered in ascending size. The wrapping 
    paper formula is the sum of the areas of all the sides plus an extra
    amount equal to the area of the smallest side."""
    assert a <= b <= c
    return (2 * a * b) + (2 * b * c) + (2 * a * c) + (a * b)


def ribbon_length(a, b, c):
    """Computes the ribbon length given the three dimensions of a box.

    The dimensions must already be ordered in ascending size. The ribbon 
    formula is the sum of the perimeter of the smallest side of the box 
    plus an extra amount equal to the volume of the box."""
    assert a <= b <= c
    return (2 * (a + b)) + (a * b * c)


# Puzzle solutions
def part1(input):
    """Computes the total wrapping paper required for all the input boxes"""
    return sum(wrapping_paper_area(*box) for box in input)


def part2(input):
    """Computes the total ribbon length required for all the input boxes"""
    return sum(ribbon_length(*box) for box in input)
