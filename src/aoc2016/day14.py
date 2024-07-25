"""Solution to https://adventofcode.com/2016/day/14"""
import re
import itertools as it
import more_itertools as mit
import utils.digest as dig


# Input parsing
parse = mit.first


# Puzzle logic
def hastriplechars(s: str):
    """Returns true if the string contains a sequence of at least three
    repeated characters"""
    return re.findall(r"(.)\1{2}", s)


def triple_char_key_candidates(salt: str):
    """Returns an (infinite) sequence of index, hash tuples that
    are potential key candidates based on the hash containing a sequence
    of a character repeated at least three times consecutively"""
    pairs = enumerate(dig.md5_str(f"{salt}{x}") for x in it.count())
    return ((idx,h) for idx,h in pairs if hastriplechars(h))


def fivepeat_in_thousand(windowed_candidates):
    """Predicate that tests whether any of the next thousand indices
    produces a hash that contains the tripled-character repeated five
    times"""
    idx, hsh = mit.first(windowed_candidates)
    match_str = "".join(re.findall(r"(.)\1{2}", hsh)[0] * 5)
    return any(i for i,h in windowed_candidates 
               if idx < i <= idx + 1000 and 
               re.findall(match_str, h) )

def pad_keys(salt):
    """Returns an infinite sequence of all the indices that produce valid
    one-time pad keys for the given salt"""
    tests = mit.windowed(triple_char_key_candidates(salt), 1001, 1)
    return (test[0][0] for test in tests if fivepeat_in_thousand(test))


def last_pad_key(salt):
    """Returns the last (64th) one-time pad key for the given salt"""
    return mit.first(it.islice(pad_keys(salt), 63, 64))

# Puzzle solutions
def part1(input):
    """What index produces the 64th one-time pad key"""
    return last_pad_key(input)
