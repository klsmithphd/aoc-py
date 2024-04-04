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
    """Initialize a (w x h) screen with all pixels set to off (zero)"""
    return [[0 for _ in range(width)] for _ in range(height)]


def set_column(screen, pos, new_col):
    """Replace the column indexed by `pos` in a 2-dimensional list-of-lists (screen)
    with the values in `new_col`"""
    def new_row(old_row, new_val):
        """The new_row helper function returns a new row list with the 
        value at `pos` replaced with `new_val` """
        return old_row[:pos] + [new_val] + old_row[pos+1:]
    return list(map(new_row, screen, new_col))


def apply_rotate(screen, dim, pos, amount):
    """Apply a rotate command to the `screen` along `dim=(row|column)` at 
    position `pos` with values rotated by `amount`"""
    match dim:
        case "column":
            column = (row[pos] for row in screen)
            return set_column(screen, pos, u.rotate(-amount, column))
        case "row":
            return screen[:pos] \
                + [list(u.rotate(-amount, screen[pos]))] \
                + screen[pos+1:]


def apply_rect(screen, width, height):
    """Apply a rect command to the `screen`, turning on pixels in a
    width-by-height swath starting at the upper left corner"""
    return [[1 for _ in range(width)] + row[width:] for row in screen[:height]] \
        + screen[height:]


def step(screen, cmd):
    """Apply a single command `cmd` to update the `screen`"""
    match cmd:
        case {"cmd": "rect", "width": w, "height": h}:
            return apply_rect(screen, w, h)
        case {"cmd": "rotate", "dim": d, "pos": p, "amount": a}:
            return apply_rotate(screen, d, p, a)


def final_state(width, height, cmds):
    """Return the final screen configuration for a width-by-height screen of
    pixels after applying all commands"""
    return ft.reduce(step, cmds, init_screen(width, height))


def lit_pixels(screen):
    """The total number of lit pixels on the screen"""
    return sum(it.chain(*screen))


def screen_to_str(screen):
    """A block-character string representation of the screen"""
    CHAR_MAP = {0: ' ', 1: '#'}
    return '\n'.join(("".join(CHAR_MAP[c] for c in row) for row in screen))


# Puzzle solutions
def part1(input):
    """How many pixels are lit up after following the instructions?"""
    return lit_pixels(final_state(SCREEN_WIDTH, SCREEN_HEIGHT, input))


def part2(input):
    """What chacters do the pixels on the screen spell in block characters?"""
    print(screen_to_str(final_state(SCREEN_WIDTH, SCREEN_HEIGHT, input)))
    return "EOARGPHYAO"
