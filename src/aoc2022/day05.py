"""Solution to https://adventofcode.com/2022/day/5"""
from functools import reduce
from itertools import zip_longest
from utils.core import AoCSolution, split_at_blanklines
from pipe import Pipe, islice, map, reverse, skip, take_while
from parse import parse


# Input parsing


def parse_stack(stack):
    crates = list(stack | take_while(lambda x: x != ' ') | skip(1))
    return crates


def parse_stacks(stacks):
    # return {1: ["Z", "N"],
    #         2: ["M", "C", "D"],
    #         3: ["P"]}

    crate_stacks = list(zip_longest(*reversed(stacks), fillvalue=' ') |
                        islice(1, None, 4) |
                        map(parse_stack))
    return dict(zip(range(1, len(crate_stacks)+1), crate_stacks))


def parse_move(move):
    return parse("move {:d} from {:d} to {:d}", move).fixed


def parse_moves(moves):
    return [parse_move(move) for move in moves]


def parse_input(input):
    stacks, moves = split_at_blanklines(input)
    return {"stacks": parse_stacks(stacks),
            "moves": parse_moves(moves)}

# Puzzle logic

# Imperative style
# def move(stacks, move):
#     qty, src, dst = move
#     for i in range(qty):
#         stacks[dst].append(stacks[src].pop())
#     return stacks


def step(stacks, move):
    qty, src, dst = move
    popped = list(reversed(stacks[src][-qty:]))
    return {**stacks, src: stacks[src][:-qty], dst: stacks[dst]+popped}


def stack_tops(stacks):
    return ''.join(stacks.values() | map(lambda s: s[-1]))


# Puzzle solutions

def part1(input):
    stacks = input['stacks']
    moves = input['moves']
    final_stacks = reduce(step, moves, stacks)
    return stack_tops(final_stacks)

# day05_soln = \
#     AoCSolution(parse,
#                 p1=
#                 p2=)
