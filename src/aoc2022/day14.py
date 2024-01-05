"""Solution to https://adventofcode.com/2022/day/14"""
from more_itertools import flatten, sliding_window

# Constants

START_POS = (500, 0)


# Input parsing

def parse_line(line: str):
    """Convert the string representation of a set of points separated by
    " -> " into a list of point tuples"""
    return [tuple(map(int, coord.split(","))) for coord in line.split(" -> ")]


def points(pos1, pos2):
    """Return all the points (endpoints inclusive) beteen `pos1` and `pos2`"""
    x1, y1 = pos1
    x2, y2 = pos2
    dy = 1 if y1 <= y2 else -1
    dx = 1 if x1 <= x2 else -1
    return [(x, y) for x in range(x1, x2+dx, dx) for y in range(y1, y2+dy, dy)]


def trace_lines(endpoints):
    """Return all of the points along the lines adjoining a series of 
    `endpoints`"""
    return flatten(points(*x) for x in sliding_window(endpoints, 2))


def rocks(input):
    """Return a set of all the points that make up the "rocks" in the
    input data"""
    return set(flatten(trace_lines(line) for line in input))


def parse(input):
    return rocks(parse_line(line) for line in input)

# Puzzle logic


def move_grain(stuff, pos):
    """A unit of sand always falls down one step if possible. 
    If the tile immediately below is blocked (by rock or sand), 
    the unit of sand attempts to instead move diagonally one step down and 
    to the left. If that tile is blocked, the unit of sand attempts to instead 
    move diagonally one step down and to the right. Sand keeps moving as long
    as it is able to do so, at each step trying to move down, then down-left, 
    then down-right. If all three possible destinations are blocked, 
    the unit of sand comes to rest and no longer moves."""
    x, y = pos
    if (x, y+1) not in stuff:
        return (x, y+1)
    elif (x-1, y+1) not in stuff:
        return (x-1, y+1)
    elif (x+1, y+1) not in stuff:
        return (x+1, y+1)
    else:
        return (x, y)


def next_grain_pos(stuff, low_point):
    """
    Returns the location of the next sand grain to be deposited, given
    the rocks and previously deposited sand grains in `stuff` and the 
    `low_point` which is not be exceeded. 
    """
    pos = START_POS
    while True:
        next_pos = move_grain(stuff, pos)
        if pos == next_pos or next_pos[1] > low_point:
            break
        pos = next_pos
    return pos


def lowest(stuff):
    """Returns the greatest y coordinate"""
    return max(x[1] for x in stuff)


def deposit_sand_grains(rocks, part1=True):
    """Returns the final set of all rocks and deposited sand grains, 
    starting with the `rocks`. For the part1 puzzle logic, use
    `part1 = True`. Set to `False` for part2."""
    stuff = set(rocks)
    lowest_rock = lowest(stuff)
    low_point = lowest_rock if part1 else lowest_rock + 1
    while True:
        next_grain = next_grain_pos(stuff, low_point)
        if part1:
            if next_grain[1] == low_point:
                break
        else:
            if next_grain == START_POS:
                stuff.add(next_grain)
                break
        stuff.add(next_grain)
    return stuff


def grains_deposited(rocks, part1=True):
    """Returns the number of sand grains deposited, given the 
    initial configuration of `rocks`, and the stopping criteria used.
    """
    rock_count = len(rocks)
    total_count = len(deposit_sand_grains(rocks, part1))
    return total_count - rock_count


# Puzzle solutions

def part1(input):
    """
    Using your scan, simulate the falling sand. How many units of sand come 
    to rest before sand starts flowing into the abyss below?
    """
    return grains_deposited(input)


def part2(input):
    """
    Using your scan, simulate the falling sand until the source of the sand 
    becomes blocked. How many units of sand come to rest?
    """
    return grains_deposited(input, False)
