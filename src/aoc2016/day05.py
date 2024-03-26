"""Solution to https://adventofcode.com/2016/day/5"""
import hashlib
import itertools as it
import more_itertools as mit


# Input parsing
def parse(input):
    return mit.first(input)


# Puzzle logic
def md5_bytes(s: str):
    return hashlib.md5(s.encode()).digest()


def isfivezerostart(bytes):
    return bytes[:3] < b'\x00\x00\x10'


def five_zero_indices(prefix: str):
    return (x for x in it.count(0) if isfivezerostart(md5_bytes(f"{prefix}{x}")))


def five_zero_hashes(prefix: str):
    indices = it.count(0)
    bytes = (md5_bytes(f"{prefix}{idx}") for idx in indices)
    return (hash for hash in bytes if isfivezerostart(hash))


def password_part1(prefix: str):
    return "".join(hex(b[2])[2:] for b in mit.take(8, five_zero_hashes(prefix)))
