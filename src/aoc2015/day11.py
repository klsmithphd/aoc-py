"""Solution to https://adventofcode.com/2015/day/11"""
import cardinality
import more_itertools as mit
import toolz
import utils.core as u

# Constants
A_VAL = ord('a')
RIGHTMOST_INDEX = 7
ALPHABET_LENGTH = 26
XXYZZ = [23, 23, 24, 25, 25]

# Input parsing
parse = toolz.first


# Puzzle logic
def string_as_ints(s: str):
    """Converts a string to a list of integer values in the range 0-25"""
    return [ord(ch) - A_VAL for ch in s]


def ints_as_string(ints):
    """Converts a list of ints (0-25) to a string of lowercase letters"""
    return "".join(chr(i+A_VAL) for i in ints)


def nums_fn(fn, s: str):
    """Converts the string to a list of integer values, applies `fn` to
    the integer representation, and then converts back to a string
    representation"""
    return ints_as_string(fn(string_as_ints(s)))


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


DISALLOWED_SET = set(string_as_ints("ilo"))


def no_disallowed(ints):
    """Whether any disallowed numbers are included"""
    return cardinality.count(i for i in ints if i in DISALLOWED_SET) == 0


def valid_password(ints):
    """A valid password satisfies all the predicates"""
    return increasing_straight(ints) and \
        two_distinct_pairs(ints) and \
        no_disallowed(ints)


def increment(ints):
    """Increment the number represented as a list of ints (base 26) to the
    next value"""
    index = RIGHTMOST_INDEX
    if ints[index] + 1 < ALPHABET_LENGTH:
        ints[index] += 1
        return ints
    while index >= 0:
        ints[index] = 0
        index -= 1
        if ints[index] + 1 < ALPHABET_LENGTH:
            ints[index] += 1
            return ints


def next_wo_disallowed_chars(ints):
    """Returns the next password number sequence that doesn't contain any
    disallowed characters"""
    idx = u.index_of(lambda x: x in DISALLOWED_SET, ints)
    return ints[:idx] + [ints[idx]+1] + [0]*(7 - idx) if u.isnotnone(idx) else ints


def next_aabcc(ints):
    """Returns the next eight-digit sequence that has an `aabcc` pattern
    in the lowest digits. That is, a pattern that consists of two different
    pairs sandwiching a 3-digit increasing straight"""
    d0, d1, d2, *_ = ints
    if ints[3:] > XXYZZ:
        # If the last five chars are past xxyzz, the next option is aabcc (00122)
        # after incrementing the 2nd char
        print("here0")
        return [d0, d1, d2+1, 0, 0, 1, 2, 2]
    elif ints[3:] == XXYZZ:
        print("here1")
        # If exactly xxyzz, then we have a valid password
        return ints
    else:
        # If less than xxyzz, then jump to the next aabcc option to try
        a = max(ints[3:5])
        b = a+1
        c = b+1
        if ints[5:] > [b, c, c]:
            print("here2")
            # If the last three digits are already past bcc, we need to
            # bump and try the next option
            return next_aabcc([d0, d1, d2, b, b, 0, 0, 0])
        else:
            print("here3")
            # Else, we can return the aabcc pattern
            return [d0, d1, d2, a, a, b, c, c]


def has_a_pair(ints):
    """Whether the first 3 values contain a pair"""
    return ints[0] == ints[1] or ints[1] == ints[2]


def increment_fast(ints):
    """An optimized version of the incrementing that allows us to skip
    large swaths of the solution space"""
    new_ints = next_wo_disallowed_chars(increment(ints))
    if not increasing_triplet(new_ints[:3]) and not has_a_pair(new_ints[:3]):
        return next_aabcc(new_ints)
    else:
        return new_ints


def next_password(password):
    """Increment the password string to the next possible value"""
    return nums_fn(increment, password)


def next_valid_password(password):
    """Determine the next valid password after the one provided"""
    chain = mit.iterate(increment_fast, string_as_ints(password))
    next_valid = toolz.first(filter(valid_password, chain))
    return ints_as_string(next_valid)


# Puzzle solutions
def part1(input):
    """Find the next valid password after the one provided as input"""
    return next_valid_password(input)


def part2(input):
    """Find the second next valid password after the one provided"""
    return next_valid_password(next_password(part1(input)))
