"""Solution to https://adventofcode.com/2015/day/18"""
import itertools as it
import more_itertools as mit
import utils.core as u
import toolz


# Input parsing
def parse_replacement(line: str):
    return line.split(" => ")


def parse(input):
    replacements, molecule = u.split_at_blanklines(input)
    return [parse_replacement(r) for r in replacements], molecule[0]


# Puzzle logic
def match_ranges(s: str, pattern: str):
    """Find all of the (potentially overlapping) index ranges within string `s`
    that match `pattern`"""
    size = len(pattern)
    char_ranges = enumerate(mit.sliding_window(s, size))
    return ((idx, idx+size) for idx, chars in char_ranges
            if "".join(chars) == pattern)


def single_replacements(s: str, repl):
    """For a given string `s`, and a `replacement` mapping, return all of the
    strings possibly constructed with a single replacement at a time"""
    old_s, new_s = repl
    return (s[:start]+new_s+s[end:] for start, end in match_ranges(s, old_s))


def all_replacements(repls, s: str):
    """For a collection of substring replacement mappings and a string `s`, 
    return all possible (possibly duplicated) new strings"""
    return it.chain(*(single_replacements(s, r) for r in repls))


def distinct_molecules(repls, s: str):
    """The set of distinct new molecules that can be generated via
    the sub-string replacement mappings"""
    return set(all_replacements(repls, s))


def ordered_replacements(repls, s: str):
    """Modifies the input to sort the replacement rules in descending order
    by size of the replacement (new) component, and reversing the order so
    that the replacements are structured new -> old. This allows us to work
    backward from the target molecule"""
    return [list(reversed(pair)) for pair in
            sorted(repls, key=lambda x: len(x[1]), reverse=True)], s


def defabricate(state):
    repls, s = state
    if s == "e":
        return repls, s
    else:
        return repls, toolz.first(all_replacements(repls, s))


def fabrication_steps(state):
    seq = mit.iterate(defabricate, ordered_replacements(*state))
    return [x[1] for x in it.takewhile(lambda s: s[1] != "e", seq)]


# Puzzle solutions
def part1(input):
    return len(distinct_molecules(*input))


def part2(input):
    return len(fabrication_steps(input))
