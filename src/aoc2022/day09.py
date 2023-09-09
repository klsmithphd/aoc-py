"""Solution to https://adventofcode.com/2022/day/9"""
from itertools import accumulate, repeat
from more_itertools import flatten
from operator import add, sub
from utils.core import AoCSolution

# Constants

MOVES = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}


# Input parsing


def parse_line(line):
    char, count = line.split()
    return (char, int(count))


def parse(input):
    return flatten(repeat(*parse_line(line)) for line in input)

# Puzzle logic

# Move to a utility module


def tmap(f, *args):
    return tuple(map(f, *args))


def cap(num):
    return num // 2 if num % 2 == 0 else num


def tail_delta(head, tail):
    """
    Compute the amount by which the tail position should change based on the
    new position of the knot in front of it
    """
    diff = tmap(sub, head, tail)
    if (abs(diff[0]) <= 1 and abs(diff[1]) <= 1):
        return (0, 0)
    else:
        return tmap(cap, diff)


def move_tail(head, tail):
    """
    Update the tail position based on the knot in front of it
    """
    return tmap(add, tail, tail_delta(head, tail))


def step(chain, cmd):
    newhead = tmap(add, chain[0], MOVES[cmd])
    return list(accumulate(chain[1:], move_tail, initial=newhead))


def all_moves(cmds, chain_len):
    return accumulate(cmds, step, initial=list(repeat((0, 0), chain_len)))


def unique_tail_positions(cmds, chain_len):
    return set(x[-1] for x in all_moves(cmds, chain_len))


def unique_tail_pos_count(cmds, chain_len):
    return len(unique_tail_positions(cmds, chain_len))


# Puzzle solutions

def part1(input):
    """
    Simulate your complete hypothetical series of motions. How many positions 
    does the tail of the rope visit at least once?
    """
    return unique_tail_pos_count(input, 2)


def part2(input):
    """
    Simulate your complete series of motions on a larger rope with ten knots. 
    How many positions does the tail of the rope visit at least once?
    """
    return unique_tail_pos_count(input, 10)


day09_soln = AoCSolution(parse, part1, part2)
