"""Solution to https://adventofcode.com/2015/day/5"""
import cardinality
import re

# Input parsing
parse = list


# Puzzle logic
def three_vowels(s: str):
    """"Does the string contain at least three vowels (of the set `aeiou`)?"""
    return len(re.findall(r"[aeiou]", s)) >= 3


def repeated_char(s: str):
    """Does the string contain at least one repeated letter?"""
    return re.search(r"(\w)\1", s) is not None


def no_invalid_pairs(s: str):
    """Does the string not contain the strings `ab` `cd` `pq` or `xy`?"""
    return re.search(r"ab|cd|pq|xy", s) is None


def part1_nice(s: str):
    """A string is nice in part1 if it satisfies the three rules above"""
    return three_vowels(s) and repeated_char(s) and no_invalid_pairs(s)


def non_overlapping_pair(s: str):
    """Does the string contain a pair of any two letters that appear at
    least twice without overlapping?"""
    return re.search(r"(\w\w).*\1", s) is not None


def repeat_with_letter_between(s: str):
    """Does the string contain one letter that repeats with exactly one
    letter in between?"""
    return re.search(r"(\w)\w\1", s) is not None


def part2_nice(s: str):
    """A string is nice in part2 if it satisfies the two rules above"""
    return non_overlapping_pair(s) and repeat_with_letter_between(s)


def nice_count(pred, strings):
    """Counts the number of strings that satisfy the nice rules"""
    return cardinality.count(filter(pred, strings))


# Puzzle solutions
def part1(input):
    """The number of input strings that are nice using the rules in part1"""
    return nice_count(part1_nice, input)


def part2(input):
    """The number of input strings that are nice using the rules in part2"""
    return nice_count(part2_nice, input)
