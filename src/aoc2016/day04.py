"""Solution to https://adventofcode.com/2016/day/4"""
import more_itertools as mit
import re
import utils.core as u
from collections import Counter, namedtuple
from heapq import nsmallest


# Constants
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
TARGET_NAME = "northpole object storage"


# Input parsing
Room = namedtuple("Room", ["encrypted_name", "sector_id", "checksum"])


def parse_line(line: str):
    code, checksum = mit.first(re.findall(r"([\w\-]*)\[(\w{5})\]", line))
    segments = code.split('-')
    return Room(segments[:-1], int(segments[-1]), checksum)


def parse(input):
    return [parse_line(line) for line in input]


# Puzzle logic
def freq_alph_sort(frequency):
    """A key function for sorting the character frequencies first by 
    frequency (descending) then by character in alphabetic order (ascending)"""
    ch, freq = frequency
    return (-freq, ch)


def isrealroom(room: Room):
    """"A room is real if the checksum is the five most common characters
    in the encrypted name, in desc order, with ties broken by alphabetization"""
    encrypted_name, _, checksum = room
    freqs = Counter("".join(encrypted_name))
    chars = (c for c, _ in nsmallest(5, freqs.items(), key=freq_alph_sort))
    return "".join(chars) == checksum


def real_room_sector_id_sum(rooms):
    """The sum of the sector ids of all the real rooms"""
    return sum(room.sector_id for room in rooms if isrealroom(room))


def decipher(room: Room):
    """For a real room, apply a shift cipher to decipher the real room name"""
    encrypted_name, sector_id, _ = room
    mapping = dict(zip(ALPHABET, u.rotate(sector_id % 26, ALPHABET)))
    def decode(s): return "".join(mapping[ch] for ch in s)
    return " ".join(decode(s) for s in encrypted_name)


def north_pole_objects_room(rooms):
    """Find the real room sector id whose decrypted name is 
    `northpole object storage`"""
    room = mit.first(r for r in rooms
                     if isrealroom(r) and decipher(r) == TARGET_NAME)
    return room.sector_id


# Puzzle solutions
def part1(input):
    """Sum of the sector ids of all the real rooms"""
    return real_room_sector_id_sum(input)


def part2(input):
    """Sector id of the room where North Pole objects are stored"""
    return north_pole_objects_room(input)
