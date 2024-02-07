"""Solution to https://adventofcode.com/2015/day/18"""
import utils.core as u


# Input parsing
def parse_replacement(line: str):
    return line.split(" => ")


def parse(input):
    replacements, molecule = u.split_at_blanklines(input)
    return [parse_replacement(r) for r in replacements], molecule[0]
