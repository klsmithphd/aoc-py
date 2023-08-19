"""Solution to https://adventofcode.com/2022/day/5"""
from utils.core import AoCSolution, split_at_blanklines
from parse import parse


# Input parsing

def parse_stacks(stacks):
    return {1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"]}


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
