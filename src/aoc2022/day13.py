"""Solution to https://adventofcode.com/2022/day/13"""
from utils.core import split_at_blanklines
from toolz import first

# Input parsing


def parse_pairs(pairs):
    return [eval(x) for x in pairs]


def parse(input):
    return [parse_pairs(pair) for pair in split_at_blanklines(input)]

# Puzzle logic


def compare(a, b):
    """https://docs.python.org/3.0/whatsnew/3.0.html#ordering-comparisons"""
    return (a > b) - (a < b)


def vector_compare(a, b):
    order_cmp = [x for x in map(packet_compare, a, b) if x != 0]
    if len(order_cmp) == 0:
        return compare(len(a), len(b))
    else:
        return order_cmp[0]


def packet_compare(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            return compare(a, b)
        else:
            return packet_compare([a], b)
    else:
        if isinstance(b, int):
            return packet_compare(a, [b])
        else:
            return vector_compare(a, b)


def isinorder(a, b):
    return packet_compare(a, b) <= 0


def inorder_packet_id_sum(input):
    return sum(idx+1 for idx, pair in enumerate(input) if isinorder(*pair))


# Puzzle solutions

def part1(input):
    return inorder_packet_id_sum(input)


# day13_soln = \
#     AoCSolution(parse,
#                 p1=
#                 p2=)
