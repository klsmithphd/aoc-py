"""Solution to https://adventofcode.com/2016/day/4"""
import more_itertools as mit
import re
import utils.core as u
from collections import Counter, namedtuple


# Constants
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


# Input parsing
Room = namedtuple("Room", ["encrypted_name", "sector_id", "checksum"])


def parse_line(line: str):
    code, checksum = mit.first(re.findall(r"([\w\-]*)\[(\w{5})\]", line))
    segments = code.split('-')
    return Room(segments[:-1], int(segments[-1]), checksum)


def parse(input):
    return [parse_line(line) for line in input]


# Puzzle logic
def sort_key(freq):
    k, v = freq
    return (-v, k)


def isrealroom(room: Room):
    encrypted_name, _, checksum = room
    freqs = Counter("".join(encrypted_name))
    chars = (c for c, _ in mit.take(5, sorted(freqs.items(), key=sort_key)))
    return "".join(chars) == checksum


def real_room_sector_id_sum(rooms):
    return sum(room.sector_id for room in rooms if isrealroom(room))


def decipher(room: Room):
    encrypted_name, sector_id, _ = room
    mapping = dict(zip(ALPHABET, u.rotate(sector_id % 26, ALPHABET)))
    def decode(s): return "".join(mapping[ch] for ch in s)
    return " ".join(decode(s) for s in encrypted_name)


def north_pole_objects_room(rooms):
    room = mit.first(r for r in rooms if
                     isrealroom(r) and
                     decipher(r) == "northpole object storage")
    return room.sector_id


# Puzzle solutions
def part1(input):
    return real_room_sector_id_sum(input)


def part2(input):
    return north_pole_objects_room(input)
