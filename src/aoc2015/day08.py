"""Solution to https://adventofcode.com/2015/day/8"""


# Input parsing
parse = list


# Puzzle logic
def code_chars(s: str):
    return len(s)


def string_chars(s: str):
    return len(eval(s))


def unescaped_diff(input):
    return sum(code_chars(x) for x in input) - \
        sum(string_chars(x) for x in input)


# Puzzle solutions
def part1(input):
    return unescaped_diff(input)
