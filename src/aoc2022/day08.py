"""Solution to https://adventofcode.com/2022/day/8"""
from itertools import takewhile
from more_itertools import flatten
from utils.core import AoCSolution

# Input parsing


def parse(input):
    return [[int(x) for x in line] for line in input]

# Puzzle logic


def transpose(m):
    return [list(col) for col in zip(*m)]


def greatest_so_far(row):
    mx = -1
    for x in row:
        if x > mx:
            mx = x
            yield 1
        else:
            yield 0


def trees_visible_from_left(row):
    return list(greatest_so_far(row))


def trees_visible_in_row(row):
    return list(map(lambda a, b: a or b,
                    trees_visible_from_left(row),
                    reversed(trees_visible_from_left(reversed(row)))))


def trees_visible_horiz(grid):
    return [trees_visible_in_row(row) for row in grid]


def trees_visible_count(grid):
    return sum(map(lambda a, b: a or b,
                   flatten(trees_visible_horiz(grid)),
                   flatten(transpose(trees_visible_horiz(transpose(grid))))))


def tree_distance(row, i):
    t = row[i]
    l = [] if i == 0 else row[i-1::-1]
    r = row[i+1:]
    return (min(len(l), 1+sum(1 for _ in takewhile(lambda x: x < t, l))),
            min(len(r), 1+sum(1 for _ in takewhile(lambda x: x < t, r))))


def tree_distance_in_row(row):
    return [tree_distance(row, i) for i in range(len(row))]


def tree_distance_horiz(grid):
    return [tree_distance_in_row(row) for row in grid]


def scenic_scores(grid):
    return map(lambda a, b: a[0]*a[1]*b[0]*b[1],
               flatten(tree_distance_horiz(grid)),
               flatten(transpose(tree_distance_horiz(transpose(grid)))))


def max_scenic_score(grid):
    return max(scenic_scores(grid))


# Puzzle solutions

def part1(input):
    return trees_visible_count(input)


def part2(input):
    return max_scenic_score(input)


day08_soln = AoCSolution(parse, part1, part2)
