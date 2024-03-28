"""Solution to https://adventofcode.com/2016/day/7"""
import re


# Input parsing
def parse_line(line: str):
    chunks = re.findall(r"\w+", line)
    return (chunks[::2], chunks[1::2])


def parse(input):
    return [parse_line(line) for line in input]
