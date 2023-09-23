"""Solution to https://adventofcode.com/2022/day/13"""
from functools import cmp_to_key
from utils.core import AoCSolution, split_at_blanklines
from toolz import concat, concatv


# Constants

divider_packets = [[[[2]], [[6]]]]

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


def sorted_packets(input):
    all_packets = concat(concatv(input, divider_packets))
    return sorted(all_packets, key=cmp_to_key(packet_compare))


def decoder_key(input):
    packets = sorted_packets(input)
    p0 = packets.index([[2]])+1
    p1 = packets.index([[6]])+1
    return p0 * p1

# Puzzle solutions


def part1(input):
    return inorder_packet_id_sum(input)


def part2(input):
    return decoder_key(input)


day13_soln = AoCSolution(parse, part1, part2)
