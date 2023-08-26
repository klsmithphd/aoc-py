"""Solution to https://adventofcode.com/2022/day/5"""
from functools import reduce, partial
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


def step(stacks, move, one_at_a_time=True):
    qty, src, dst = move
    to_move = stacks[src][-qty:]
    popped = list(reversed(to_move)) if one_at_a_time else to_move
    return {**stacks, src: stacks[src][:-qty], dst: stacks[dst]+popped}


part2_step = partial(step, one_at_a_time=False)


def stack_tops(stacks):
    return ''.join(stacks.values() | map(lambda s: s[-1]))


# Puzzle solutions

def part1(input):
    """
    After the rearrangement procedure completes, what crate ends up on top 
    of each stack?
    """
    stacks = input['stacks']
    moves = input['moves']
    final_stacks = reduce(step, moves, stacks)
    return stack_tops(final_stacks)


def part2(input):
    """
    After the rearrangement procedure completes, what crate ends up on top 
    of each stack?
    """
    stacks = input['stacks']
    moves = input['moves']
    final_stacks = reduce(part2_step, moves, stacks)
    return stack_tops(final_stacks)


day05_soln = AoCSolution(parse_input, part1, part2)
