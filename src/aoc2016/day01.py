"""Solution to https://adventofcode.com/2016/day/1"""
import toolz


# Input parsing
def parse_instruction(inst: str):
    bearing = "right" if inst[:1] == "R" else "left"
    dist = int(inst[1:])
    return (bearing, dist)


def parse(input):
    return [parse_instruction(i) for i in toolz.first(input).split(", ")]


# Puzzle logic


# Puzzle solutions
