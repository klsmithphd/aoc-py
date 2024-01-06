"""Solution to https://adventofcode.com/2015/day/4"""
import hashlib
import itertools as it
import toolz


# Input parsing
parse = toolz.first


# Puzzle logic
def digest_prefix(s: str):
    """First three bytes of the MD5 digest of the supplied string"""
    hasher = hashlib.md5(s.encode())
    return hasher.digest()[:3]


def five_zero_start(digest):
    """Does the supplied digest prefix start with 5 zeros"""
    return digest < b'\x00\x00\x10'


def six_zero_start(digest):
    """Does the supplied diggest prefix start with 6 zeros"""
    return digest == b'\x00\x00\x00'


def decimal(secret: str, pred):
    """Find the first integer that satisfies the predicate `pred`"""
    def passing_hash(x): return pred(digest_prefix(f"{secret}{x}"))
    return toolz.first(filter(passing_hash, it.count(1)))


# Puzzle solutions
def part1(input):
    "Finds the first integer where the MD5 hash starts with five zeros in hex"
    return decimal(input, five_zero_start)


def part2(input):
    "Finds the first integer where the MD5 hash starts with six zeros in hex"
    return decimal(input, six_zero_start)
