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


def not_five_zero_start(digest):
    """Returns false unless the supplied bytes start with 5 zeros"""
    return not digest[1] < b'\x00\x00\x10'


def not_six_zero_start(digest):
    """Returns false unless the supplied bytes are exactly 6 zeros"""
    return not digest[1] == b'\x00\x00\x00'


def decimal(secret: str, pred):
    """Find the first integer that *fails* to satisfy the predicate `pred`"""
    hashes = enumerate(digest_prefix(f"{secret}{i}") for i in it.count(1))
    return toolz.first(it.dropwhile(pred, hashes))[0] + 1


# Puzzle solutions
def part1(input):
    "Finds the first integer where the MD5 hash starts with five zeros in hex"
    return decimal(input, not_five_zero_start)


def part2(input):
    "Finds the first integer where the MD5 hash starts with six zeros in hex"
    return decimal(input, not_six_zero_start)
