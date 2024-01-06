"""Solution to https://adventofcode.com/2015/day/4"""
import hashlib
import itertools as it
import toolz


# Input parsing
parse = toolz.first


# Puzzle logic
def hexdigest(s: str):
    hasher = hashlib.md5()
    hasher.update(bytes(s, 'utf-8'))
    return hasher.hexdigest()


def not_five_zero_start(digest):
    return not digest[1].startswith("00000")


def not_six_zero_start(digest):
    return not digest[1].startswith("000000")


def decimal(secret: str, pred):
    hashes = enumerate(hexdigest(secret + str(i)) for i in it.count(1))
    return toolz.first(it.dropwhile(pred, hashes))[0] + 1


# Puzzle solutions
def part1(input):
    return decimal(input, not_five_zero_start)


def part2(input):
    return decimal(input, not_six_zero_start)
