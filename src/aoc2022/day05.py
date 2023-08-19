"""Solution to https://adventofcode.com/2022/day/5"""
from itertools import zip_longest
from utils.core import AoCSolution, split_at_blanklines
from pipe import Pipe, islice, map, reverse, skip, skip_while
from parse import parse


# Input parsing


def parse_stack(stack):
    crates = list(
        reversed(list(stack | skip_while(lambda x: x == ' '))) | skip(1))
    return crates


def parse_stacks(stacks):
    # return {1: ["Z", "N"],
    #         2: ["M", "C", "D"],
    #         3: ["P"]}

    crate_stacks = list(zip_longest(*stacks, fillvalue=' ') |
                        islice(1, None, 4) |
                        map(parse_stack))
    return dict(zip(range(1, len(crate_stacks)+1), crate_stacks))


def parse_move(move):
    return parse("move {qty:d} from {from:d} to {to:d}", move).named


def parse_moves(moves):
    return [parse_move(move) for move in moves]


def parse_input(input):
    stacks, moves = split_at_blanklines(input)
    return {"stacks": parse_stacks(stacks),
            "moves": parse_moves(moves)}

# Puzzle logic


# Puzzle solutions

# day05_soln = \
#     AoCSolution(parse,
#                 p1=
#                 p2=)
