"""Solution to https://adventofcode.com/2022/day/5"""
from collections import namedtuple
from functools import reduce, partial
from itertools import zip_longest
from parse import parse as str_parse
from pipe import Pipe, islice, map
from utils.core import split_at_blanklines


# Input parsing

Move = namedtuple('Move', ['qty', 'src', 'dst'])
Day05Input = namedtuple('Day05Input', ['stacks', 'moves'])


def parse_stack(stack):
    return [x for x in stack if x and str.isalpha(x)]


def parse_stacks(stacks):
    crate_stacks = list(zip_longest(*reversed(stacks)) |  # transpose rows/cols
                        islice(1, None, 4) |  # only the cols with "crates"
                        map(parse_stack))  # convert chars into lists
    n = len(crate_stacks)+1
    return dict(zip(range(1, n), crate_stacks))


def parse_move(move):
    values = str_parse("move {:d} from {:d} to {:d}", move).fixed
    return Move(*values)


def parse_moves(moves):
    return [parse_move(move) for move in moves]


def parse(input):
    stacks, moves = split_at_blanklines(input)
    return Day05Input(parse_stacks(stacks), parse_moves(moves))

# Puzzle logic


def step(stacks, move, one_at_a_time=True):
    qty, src, dst = move
    to_move = stacks[src][-qty:]
    popped = list(reversed(to_move)) if one_at_a_time else to_move
    return {**stacks,
            src: stacks[src][:-qty],
            dst: stacks[dst]+popped}


def stack_tops(stacks):
    return ''.join(s[-1] for s in stacks.values())


def stack_tops_after_steps(input, part1=True):
    stacks, moves = input
    step_fn = step if part1 else partial(step, one_at_a_time=False)
    final_stacks = reduce(step_fn, moves, stacks)
    return stack_tops(final_stacks)


# Puzzle solutions

def part1(input):
    """
    After the rearrangement procedure completes, what crate ends up on top 
    of each stack?
    """
    return stack_tops_after_steps(input, part1=True)


def part2(input):
    """
    After the rearrangement procedure completes, what crate ends up on top 
    of each stack?
    """
    return stack_tops_after_steps(input, part1=False)
