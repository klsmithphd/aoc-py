"""Solution to https://adventofcode.com/2015/day/11"""
import cardinality
import itertools as it
import more_itertools as mit
import toolz

# Constants
a_val = ord('a')
rightmost_index = 7
alphabet_length = 26

# Input parsing
parse = toolz.first


# Puzzle logic
def string_as_ints(s: str):
    return [ord(ch) - a_val for ch in s]


def ints_as_string(ints):
    return "".join(chr(i+a_val) for i in ints)


def increasing_triplet(ints):
    a, b, c = ints
    return (c - b == 1) and (b - a == 1)


def increasing_straight(ints):
    return any(increasing_triplet(trip) for trip in mit.windowed(ints, 3))


def matching_pair(pair):
    a, b = pair
    return a == b


def two_distinct_pairs(ints):
    distinct_pairs = set(filter(matching_pair, mit.windowed(ints, 2)))
    return len(distinct_pairs) >= 2


disallowed_set = set(string_as_ints("iol"))


def no_disallowed(ints):
    return cardinality.count(i for i in ints if i in disallowed_set) == 0


def valid_password(ints):
    return increasing_straight(ints) and \
        two_distinct_pairs(ints) and \
        no_disallowed(ints)


def increment(ints):
    index = rightmost_index
    if ints[index] + 1 < alphabet_length:
        ints[index] += 1
        return ints
    while index >= 0:
        ints[index] = 0
        index -= 1
        if ints[index] + 1 < alphabet_length:
            ints[index] += 1
            return ints


def next_password(password):
    return ints_as_string(increment(string_as_ints(password)))


def next_valid_password(password):
    chain = mit.iterate(increment, string_as_ints(password))
    next_valid = toolz.first(filter(valid_password, chain))
    return ints_as_string(next_valid)


# Puzzle solutions
def part1(input):
    return next_valid_password(input)


def part2(input):
    return next_valid_password(next_password(part1(input)))
