"""Solution to https://adventofcode.com/2015/day/10"""
import itertools as it
import more_itertools as mit
import toolz


# Input parsing
parse = toolz.first


# Puzzle logic
def look_and_say(s: str):
    """Implements the Look-and-say sequence
    https://en.wikipedia.org/wiki/Look-and-say_sequence"""
    chunks = mit.split_when(s, lambda x, y: y != x)
    counts = it.chain.from_iterable((len(i), i[0]) for i in chunks)
    return "".join(str(i) for i in counts)


def nth_value(n, seed):
    """Starting from `seed`, run the look_and_say fn `n` times"""
    return len(toolz.nth(n, mit.iterate(look_and_say, seed)))


# Puzzle solutions
def part1(input):
    """Length of string after 40 iterations given the puzzle input seed"""
    return nth_value(40, input)


def part2(input):
    """Length of the string after 50 iterations given the puzzle input seed"""
    return nth_value(50, input)
