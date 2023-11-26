"""Solution to https://adventofcode.com/2022/day/14"""
from more_itertools import flatten, sliding_window
# from utils.core import AoCSolution

# Input parsing

def parse_line(line: str):
    return [tuple(map(int, coord.split(","))) for coord in line.split(" -> ")]


def points(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    dy = 1 if y1 <= y2 else -1
    dx = 1 if x1 <= x2 else -1
    return [(x, y) for x in range(x1, x2+dx, dx) for y in range(y1, y2+dy, dy)]


def trace_lines(line):
    return flatten(points(*x) for x in sliding_window(line, 2))


def rocks(input):
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
    x,y = pos
    if (x, y+1) not in stuff:
        return (x, y+1)
    elif (x-1, y+1) not in stuff:
        return (x-1, y+1)
    elif (x+1, y+1) not in stuff:
        return (x+1, y+1)
    else:
        return (x,y)
        
    
def next_grain_pos(stuff, low_point):
    pos = (500, 0)
    # Logically, this ought to be "iterate_until_static"
    # In clojure, I called that `converge`
    while True:        
        next_pos = move_grain(stuff, pos)
        if pos == next_pos or next_pos[1] > low_point:
            break
        else:
            pos = next_pos
    return pos


def lowest(stuff):
    return max(x[1] for x in stuff)

def deposit_sand_grains(rocks, part1=True):
    stuff = set(rocks)
    lowest_rock = lowest(stuff)
    low_point = lowest_rock if part1 else lowest_rock + 1
    while True:
        next_grain = next_grain_pos(stuff, low_point)
        if part1:
            if next_grain[1] == low_point:
                break
        else:
            if next_grain == (500, 0):
                stuff.add(next_grain)
                break
        stuff.add(next_grain)
    return stuff


def grains_until_stopped(rocks, part1=True):
    original = len(rocks)
    final = len(deposit_sand_grains(rocks, part1))
    return final - original


# Puzzle solutions

def part1(input):
    """
    Using your scan, simulate the falling sand. How many units of sand come 
    to rest before sand starts flowing into the abyss below?
    """
    return grains_until_stopped(input)

def part2(input):
    """
    Using your scan, simulate the falling sand until the source of the sand 
    becomes blocked. How many units of sand come to rest?
    """
    return grains_until_stopped(input, False)


# day14_soln = \
#     AoCSolution(parse,
#                 p1=
#                 p2=)
