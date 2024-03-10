"""Solution to https://adventofcode.com/2016/day/4"""
import more_itertools as mit
import re


# Input parsing
def parse_line(line: str):
    code, checksum = mit.first(re.findall(r"([\w\-]*)\[(\w{5})\]", line))
    segments = code.split('-')
    return (segments[:-1], int(segments[-1]), checksum)


def parse(input):
    return [parse_line(line) for line in input]
