"""Solution to https://adventofcode.com/2016/day/7"""
import cardinality
import re


# Input parsing
def parse_line(line: str):
    chunks = re.findall(r"\w+", line)
    return (chunks[::2], chunks[1::2])


def parse(input):
    return [parse_line(line) for line in input]


# Puzzle logic
def hasabba(s: str):
    return bool(re.search(r"(.)(?!\1)(.)\2\1", s))


def hastlssupport(ip):
    supernets, hypernets = ip
    if any(hasabba(s) for s in hypernets):
        return False
    else:
        return any(hasabba(s) for s in supernets)


# Puzzle solutions:
def part1(input):
    return cardinality.count(filter(hastlssupport, input))
