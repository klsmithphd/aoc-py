"""Solution to https://adventofcode.com/2016/day/3"""


# Input parsing
def parse_line(line: str):
    return tuple(int(x) for x in line.split())


def parse(input):
    return [parse_line(line) for line in input]
