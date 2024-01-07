"""Solution to https://adventofcode.com/2015/day/8"""


# Constants
bslash = '\x5c'  # '\'


# Input parsing
parse = list


# Puzzle logic
def unescape(s: str):
    """Unescape the string"""
    return eval(s)


def escape(s: str):
    """Escape backslashes and double-quote character and wrap in new
    double quotes"""
    return '"' + s.replace(bslash, r'\\').replace(r'"', r'\"') + '"'


def unescaped_diff(input):
    """The total difference in size between the code for the string literals
    and the actual strings"""
    return sum(len(x) for x in input) - sum(len(unescape(x)) for x in input)


def escaped_diff(input):
    """The total difference in size between the code for the re-escaped
    string literals and the original coded strings"""
    return sum(len(escape(x)) for x in input) - sum(len(x) for x in input)


# Puzzle solutions
def part1(input):
    """Difference in size between unescaped and escaped strings"""
    return unescaped_diff(input)


def part2(input):
    """Difference in size between doubly escaped and escaped strings"""
    return escaped_diff(input)
