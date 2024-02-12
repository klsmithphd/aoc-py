"""Solution to https://adventofcode.com/2015/day/21"""
import collections as c


# Constants
Stats = c.namedtuple("Stats",
                     ["hit_points", "mana", "armor", "damage"],
                     defaults=[0]*4)


# Input parsing
def parse_line(line: str):
    attr, qty = line.split(": ")
    return "_".join(attr.lower().split(" ")), int(qty)


def parse(input):
    return Stats(**{k: v for k, v in (parse_line(line) for line in input)})

# Puzzle logic


# Puzzle solutions
