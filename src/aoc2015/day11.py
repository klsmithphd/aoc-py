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
    """Converts a string to a list of integer values in the range 0-25"""
    return [ord(ch) - a_val for ch in s]


def ints_as_string(ints):
    """Converts a list of ints (0-25) to a string of lowercase letters"""
    return "".join(chr(i+a_val) for i in ints)


def increasing_triplet(ints):
    """Whether the three values are consecutively increasing"""
    a, b, c = ints
    return (c - b == 1) and (b - a == 1)


def increasing_straight(ints):
    """Whether the numbers contain any consecutively increasing triplets"""
    return any(increasing_triplet(trip) for trip in mit.windowed(ints, 3))


def matching_pair(pair):
    """Whether the pair matches"""
    a, b = pair
    return a == b


def two_distinct_pairs(ints):
    """Whether there are at least two distinct pairs"""
    distinct_pairs = set(filter(matching_pair, mit.windowed(ints, 2)))
    return len(distinct_pairs) >= 2


disallowed_set = set(string_as_ints("iol"))


def no_disallowed(ints):
    """Whether any disallowed numbers are included"""
    return cardinality.count(i for i in ints if i in disallowed_set) == 0


def valid_password(ints):
    """A valid password satisfies all the predicates"""
    return increasing_straight(ints) and \
        two_distinct_pairs(ints) and \
        no_disallowed(ints)


def increment(ints):
    """Increment the number represented as a list of ints (base 26) to the
    next value"""
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
    """Increment the password string to the next possible value"""
    return ints_as_string(increment(string_as_ints(password)))


def next_valid_password(password):
    """Determine the next valid password after the one provided"""
    chain = mit.iterate(increment, string_as_ints(password))
    next_valid = toolz.first(filter(valid_password, chain))
    return ints_as_string(next_valid)


# Puzzle solutions
def part1(input):
    """Find the next valid password after the one provided as input"""
    return next_valid_password(input)


def part2(input):
    """Find the second next valid password after the one provided"""
    return next_valid_password(next_password(part1(input)))
