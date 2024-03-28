"""Solution to https://adventofcode.com/2016/day/7"""
import cardinality
import itertools as it
import re


# Input parsing
def parse_line(line: str):
    chunks = re.findall(r"\w+", line)
    return (chunks[::2], chunks[1::2])


def parse(input):
    return [parse_line(line) for line in input]


# Puzzle logic
def hasabba(s: str):
    """Does the string `s` contain an ABBA sequence?

    An ABBA is any four-character sequence which consists of a pair of
    two different characters followed by the reverse of that pair, 
    such as xyyx or abba"""
    return bool(re.search(r"(.)(?!\1)(.)\2\1", s))


def hastlssupport(ip):
    """Does the IP have TLS support?

    An IP supports TLS if it has an ABBA sequence among its supernets
    but not among its hypernets"""
    supernets, hypernets = ip
    if any(hasabba(s) for s in hypernets):
        return False
    else:
        return any(hasabba(s) for s in supernets)


def all_abas(s: str):
    """Returns all ABA sequences in a string.

    An ABA is any three-character sequence which consists of the same 
    character twice with a different character between them, 
    such as xyx or aba."""
    return re.findall(r"(?=((.)(?!\2)(.)\2))", s)


def bab(aba):
    """Given an ABA regex Match, construct a literal BAB pattern"""
    _, a, b = aba
    return re.compile(b+a+b)


def hasbab(hypernets, bab):
    """Whether any of the hypernets matches the BAB regex"""
    return any(re.search(bab, net) for net in hypernets)


def hassslsupport(ip):
    """Does the IP support SSL?

    An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, 
    anywhere in the supernet sequences (outside any square bracketed sections), 
    and a corresponding Byte Allocation Block, or BAB, 
    anywhere in the hypernet sequences."""

    supernets, hypernets = ip
    babs = (bab(aba) for aba in it.chain(*(all_abas(s) for s in supernets)))
    return any(hasbab(hypernets, bab) for bab in babs)


# Puzzle solutions:
def part1(input):
    """How many IPs support TLS"""
    return cardinality.count(filter(hastlssupport, input))


def part2(input):
    """How many IPs support SSL"""
    return cardinality.count(filter(hassslsupport, input))
