"""Solution to https://adventofcode.com/2016/day/8"""
import itertools as it
import functools as ft
import re
import utils.core as u


# Constants
SCREEN_WIDTH = 50
SCREEN_HEIGHT = 6


# Input parsing
def parse_rect(line: str):
    w, h = (int(i) for i in re.findall(r"\d+", line))
    return {"cmd": "rect", "width": w, "height": h}


def parse_rotate(line: str):
    d, p, a = re.search(r"(row|column) [x|y]=(\d+) by (\d+)", line).groups()
    return {"cmd": "rotate", "dim": d, "pos": int(p), "amount": int(a)}


def parse_line(line: str):
    if line.startswith("rect"):
        return parse_rect(line)
    else:
        return parse_rotate(line)


def parse(input):
    return [parse_line(line) for line in input]


# Puzzle logic
def init_screen(width, height):
    return [[0 for _ in range(width)] for _ in range(height)]


# Copied from 2015/day06
# def update_slice(up_fn, start, end, lst):
#     """Update a subset (slice) of the values in a list from start (inclusive)
#     to end (exclusive)"""
#     return lst[:start] + [up_fn(i) for i in lst[start:end]] + lst[end:]


# Copied from 2015/day06
# def update_grid_immutable(update_fn, grid, instruction):
#     """Updates the `grid` according to the `instruction` using the
#     interpretation of the `update_fn`"""
#     cmd, start, end = instruction
#     sx, sy = start
#     ex, ey = end
#     # This partial function updates the x-values within a y-slice
#     update_row = ft.partial(update_slice, ft.partial(update_fn, cmd), sx, ex+1)
#     return update_slice(update_row, sy, ey+1, grid)


def set_column(screen, pos, new_col):
    def new_row(old_row, new_val):
        return old_row[:pos] + [new_val] + old_row[pos+1:]
    return [new_row(old, new) for old, new in zip(screen, new_col)]
    # return list(map(new_row, screen, new_col))


def apply_rotate(screen, dim, pos, amount):
    if dim == "column":
        column = (row[pos] for row in screen)
        return set_column(screen, pos, u.rotate(-amount, column))
    else:
        return screen[:pos] + [list(u.rotate(-amount, screen[pos]))] + screen[pos+1:]


def apply_rect(screen, width, height):
    return [[1 for _ in range(width)] + row[width:] for row in screen[:height]] \
        + screen[height:]


def step(screen, cmd):
    match cmd:
        case {"cmd": "rect", "width": w, "height": h}:
            return apply_rect(screen, w, h)
        case {"cmd": "rotate", "dim": d, "pos": p, "amount": a}:
            return apply_rotate(screen, d, p, a)


def final_state(width, height, cmds):
    return ft.reduce(step, cmds, init_screen(width, height))


def lit_pixels(screen):
    return sum(it.chain(*screen))


# Puzzle solutions
def part1(input):
    return lit_pixels(final_state(SCREEN_WIDTH, SCREEN_HEIGHT, input))
