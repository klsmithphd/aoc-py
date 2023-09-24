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
    """If both values are lists, compare the first value of each list, 
    then the second value, and so on. If the left list runs out of items first, 
    the inputs are in the right order. If the right list runs out of items 
    first, the inputs are not in the right order. If the lists are the same 
    length and no comparison makes a decision about the order, 
    continue checking the next part of the input.
    """
    order_cmp = [x for x in map(packet_compare, a, b) if x != 0]
    if len(order_cmp) == 0:
        return compare(len(a), len(b))
    else:
        return order_cmp[0]


def packet_compare(a, b):
    """If both values are integers, the lower integer should come first.

    If both values are lists, see `vector_compare`

    If exactly one value is an integer, convert the integer to a list which 
    contains that integer as its only value, then retry the comparison.
    """
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


def isinorder(a, b) -> bool:
    """Boolean test to assess whether a is properly "in front of" b,
    i.e., ordered such a <= b"""
    return packet_compare(a, b) <= 0


def inorder_packet_id_sum(input):
    """Compute the sum of the indices of all the packet pairs that 
    are in order. The indices are 1-indexed, not 0-indexed."""
    return sum(idx+1 for idx, pair in enumerate(input) if isinorder(*pair))


def sorted_packets(input):
    """Add in the divider packets into the input, and then sort
    all packets according to the ordering logic defined."""
    all_packets = concat(concatv(input, divider_packets))
    return sorted(all_packets, key=cmp_to_key(packet_compare))


def decoder_key(input):
    """To find the decoder key for this distress signal, you need to determine 
    the indices of the two divider packets and multiply them together."""
    packets = sorted_packets(input)
    p0 = packets.index([[2]])+1
    p1 = packets.index([[6]])+1
    return p0 * p1

# Puzzle solutions


def part1(input):
    """Determine which pairs of packets are already in the right order. 
    What is the sum of the indices of those pairs?"""
    return inorder_packet_id_sum(input)


def part2(input):
    """Organize all of the packets into the correct order. 
    What is the decoder key for the distress signal?"""
    return decoder_key(input)


day13_soln = AoCSolution(parse, part1, part2)
