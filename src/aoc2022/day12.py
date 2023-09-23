"""Solution to https://adventofcode.com/2022/day/12"""
from toolz import first
from utils.graph import DictGraph, dijkstra
from utils.grid.grid2d import Grid2D
from utils.grid.listgrid2d import strings_to_ListGrid2D
# from utils.core import AoCSolution

# Input parsing

START = -1
END = 26


def translate(char):
    match char:
        case 'S':
            return START
        case 'E':
            return END
        case _:
            return ord(char) - ord('a')


def parse(input):
    return strings_to_ListGrid2D(translate, input)

# Puzzle logic


def find_matches(grid: Grid2D, value):
    return (pos for pos in grid.positions() if grid.value(pos) == value)


def transitions(grid: Grid2D, pos):
    node = grid.value(pos)
    candidates = grid.neighbors4(pos)
    return (pos, {x: 1 for x in candidates if grid.value(x)-node <= 1})


def grid_to_graph(grid: Grid2D):
    return DictGraph(dict(transitions(grid, v) for v in grid.positions()))


def shortest_path_length(graph, start, end):
    path = dijkstra(graph, start, lambda x: x == end)
    return len(path) - 1


def shortest_path_from_start(input):
    graph = grid_to_graph(input)
    start = first(find_matches(input, START))
    end = first(find_matches(input, END))

    return shortest_path_length(graph, start, end)


# Puzzle solutions

def part1(input):
    return shortest_path_from_start(input)

# day12_soln = \
#     AoCSolution(parse,
#                 p1=
#                 p2=)
