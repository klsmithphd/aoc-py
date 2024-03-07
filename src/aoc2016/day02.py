"""Solution to https://adventofcode.com/2016/day/2"""
import itertools as it
import functools as ft


# Constants
FIRST_POS = (0, 0)

SQUARE_KEYPAD = {
    (-1, 1): 1,  (0, 1): 2,  (1, 1): 3,
    (-1, 0): 4,  (0, 0): 5,  (1, 0): 6,
    (-1, -1): 7, (0, -1): 8, (1, -1): 9
}


# Input parsing
parse = list


# Puzzle logics
def intended_step(pos, cmd):
    x, y = pos
    match cmd:
        case 'U': return (x, y+1)
        case 'D': return (x, y-1)
        case 'R': return (x+1, y)
        case 'L': return (x-1, y)


def move(keypad, pos, cmd):
    goto = intended_step(pos, cmd)
    return goto if goto in keypad.keys() else pos


def digit_pos(keypad, start, cmds):
    return ft.reduce(ft.partial(move, keypad), cmds, start)


def all_digits_pos(keypad, cmds):
    return it.accumulate(cmds, ft.partial(digit_pos, keypad), initial=FIRST_POS)


def bathroom_code(keypad, cmds):
    return "".join(str(keypad.get(pos)) for pos in
                   it.islice(all_digits_pos(keypad, cmds), 1, None))


square_bathroom_code = ft.partial(bathroom_code, SQUARE_KEYPAD)


def part1(input):
    return square_bathroom_code(input)
