"""Solution to https://adventofcode.com/2015/day/18"""
import itertools as it
import more_itertools as mit
import utils.core as u


# Input parsing
def parse_replacement(line: str):
    return line.split(" => ")


def parse(input):
    replacements, molecule = u.split_at_blanklines(input)
    return [parse_replacement(r) for r in replacements], molecule[0]


# Puzzle logic
def match_ranges(s: str, pattern: str):
    size = len(pattern)
    char_ranges = enumerate(mit.sliding_window(s, size))
    return ((idx, idx+size) for idx, chars in char_ranges
            if "".join(chars) == pattern)


def single_replacements(s: str, repl):
    old, new_s = repl
    return (s[:start]+new_s+s[end:] for start, end in match_ranges(s, old))


def distinct_molecules(replacements, molecule):
    return set(it.chain(*(single_replacements(molecule, r) for r in replacements)))


# Puzzle solutions
def part1(input):
    return len(distinct_molecules(*input))
