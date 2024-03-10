"""Solution to https://adventofcode.com/2016/day/4"""
import more_itertools as mit
import re
from collections import Counter


# Input parsing
def parse_line(line: str):
    code, checksum = mit.first(re.findall(r"([\w\-]*)\[(\w{5})\]", line))
    segments = code.split('-')
    return (segments[:-1], int(segments[-1]), checksum)


def parse(input):
    return [parse_line(line) for line in input]


# Puzzle logic
def sort_key(freq):
    k, v = freq
    return (-v, k)


def isrealroom(room):
    encrypted_name, _, checksum = room
    freqs = Counter("".join(encrypted_name))
    chars = (c for c, f in mit.take(5, sorted(freqs.items(), key=sort_key)))
    return "".join(chars) == checksum


def real_room_sector_id_sum(rooms):
    return sum(room[1] for room in rooms if isrealroom(room))


# Puzzle solutions
def part1(input):
    return real_room_sector_id_sum(input)
