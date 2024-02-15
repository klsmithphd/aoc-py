"""Solution to https://adventofcode.com/2015/day/23"""
import collections as c


# Constants


# Input parsing
Instruction = c.namedtuple(
    "Instruction",
    ["inst", "arg1", "arg2"],
    defaults=[None])


def number_cast(s: str):
    return int(s) if s not in {"a", "b"} else s


def parse_line(line: str):
    inst, rest = line.split(" ", 1)
    print(inst, rest)
    args = [number_cast(x) for x in rest.split(", ")]
    print(args)
    return Instruction(inst, *args)


def parse(input):
    return [parse_line(line) for line in input]


# Puzzle logic


# Puzzle solutions
