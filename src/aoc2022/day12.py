"""Solution to https://adventofcode.com/2022/day/12"""
from toolz import first, concatv
from utils.core import AoCSolution, isequal
from utils.graph import DictGraph, dijkstra
from utils.grid.grid2d import Grid2D
from utils.grid.listgrid2d import strings_to_ListGrid2D

# Constants

START = -1
LOW = 0
END = 26
UNREACHABLE = 10000000

# Input parsing


def translate(char):
    """Convert a character into a numerial height value.
    `S` and `E` are treated specially, but all other characters
    are expected to be in the range ('a' - 'z') and will map to 
    ints from 0 to 25"""
    match char:
        case 'S': return START
        case 'E': return END
        case _: return ord(char) - ord('a')


def parse(input):
    return strings_to_ListGrid2D(translate, input)

# Puzzle logic


def find_matches(grid: Grid2D, value):
    """Find the position of any locations in the `grid` that have
    value `value`"""
    return (pos for pos in grid.positions() if grid.value(pos) == value)


def transitions(grid: Grid2D, pos):
    """Return a tuple of the position `pos` and a dict of all adjacent
    nodes in `grid` that are at most one level higher than the current 
    position."""
    node = grid.value(pos)
    candidates = grid.neighbors4(pos)
    return (pos, {x: 1 for x in candidates if grid.value(x)-node <= 1})


def grid_to_graph(grid: Grid2D):
    """Given the logic for determining the allowable transitions from
    one position to another, convert the grid into a Graph"""
    return DictGraph(dict(transitions(grid, v) for v in grid.positions()))


def shortest_path_length(graph, start, end):
    """Find the length of the shortest path between the start and end
    nodes"""
    path = dijkstra(graph, start, isequal(end))
    return len(path) - 1 if path else UNREACHABLE


def shortest_path_from_start(input):
    """Given the grid, find the length of the shortest path between the
    start and end cells"""
    graph = grid_to_graph(input)
    start = first(find_matches(input, START))
    end = first(find_matches(input, END))

    return shortest_path_length(graph, start, end)


def shortest_path_from_any_a(input):
    """Given the grid, the find length of the shortest path between 
    any 'a' or 'S' cells and the end cell"""
    graph = grid_to_graph(input)
    starts = concatv(find_matches(input, START), find_matches(input, LOW))
    end = first(find_matches(input, END))

    return min(shortest_path_length(graph, s, end) for s in starts)


# Puzzle solutions

def part1(input):
    """What is the fewest steps required to move from your current position 
    to the location that should get the best signal?"""
    return shortest_path_from_start(input)


def part2(input):
    """What is the fewest steps required to move starting from any square with 
    elevation a to the location that should get the best signal?"""
    return shortest_path_from_any_a(input)


day12_soln = AoCSolution(parse, part1, part2)
