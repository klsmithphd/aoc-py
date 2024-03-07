"""Solution to https://adventofcode.com/2016/day/2"""
import itertools as it
import functools as ft


# Constants
FIRST_POS = (0, 0)

# 1 2 3
# 4 5 6
# 7 8 9
SQUARE_KEYPAD = {
    (-1, 1): '1',  (0, 1): '2',  (1, 1): '3',
    (-1, 0): '4',  (0, 0): '5',  (1, 0): '6',
    (-1, -1): '7', (0, -1): '8', (1, -1): '9'
}

#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D
DIAMOND_KEYPAD = {
    (2, 2): '1',
    (1, 1): '2', (2, 1): '3', (3, 1): '4',
    (0, 0): '5', (1, 0): '6', (2, 0): '7', (3, 0): '8', (4, 0): '9',
    (1, -1): 'A', (2, -1): 'B', (3, -1): 'C',
    (2, -2): 'D'
}


# Input parsing
parse = list


# Puzzle logics
def intended_step(pos, cmd):
    """Determine the grid position that `cmd` would have you try to move to next"""
    x, y = pos
    match cmd:
        case 'U': return (x, y+1)
        case 'D': return (x, y-1)
        case 'R': return (x+1, y)
        case 'L': return (x-1, y)


def move(keypad, pos, cmd):
    """Apply the given `cmd` to move (or not move if impossible) to the next
    position on the keypad"""
    goto = intended_step(pos, cmd)
    return goto if goto in keypad.keys() else pos


def digit_pos(keypad, start, cmds):
    """Determine where you end up following the instructions (`cmds`) for a
    single digit, starting at `start`"""
    return ft.reduce(ft.partial(move, keypad), cmds, start)


def all_digits_pos(keypad, cmds):
    """Determine the grid positions of all digits, given the sequential cmds
    for each one"""
    return it.accumulate(cmds, ft.partial(digit_pos, keypad), initial=FIRST_POS)


def bathroom_code(keypad, cmds):
    """Compute the bathroom code for the given `keyboard` layout and set of 
    `cmds`"""
    return "".join(keypad.get(pos) for pos in
                   it.islice(all_digits_pos(keypad, cmds), 1, None))


square_bathroom_code = ft.partial(bathroom_code, SQUARE_KEYPAD)
diamond_bathroom_code = ft.partial(bathroom_code, DIAMOND_KEYPAD)


# Puzzle solutions
def part1(input):
    """What's the bathroom code given the provided instructions (square keypad)"""
    return square_bathroom_code(input)


def part2(input):
    """What's the bathroom code given the provided instructions (diamond keypad)"""
    return diamond_bathroom_code(input)
