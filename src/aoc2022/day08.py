"""Solution to https://adventofcode.com/2022/day/8"""
from itertools import takewhile
from more_itertools import flatten
from utils.core import AoCSolution

# Input parsing


def parse(input):
    return [[int(x) for x in line] for line in input]


# Puzzle logic


def transpose(m):
    """
    Transpose a list of lists (swapping column and row indices)
    """
    return [list(col) for col in zip(*m)]


def greatest_so_far(row):
    """
    Yield 1 if the currently examined element in the sequence is the maximum
    seen thus far, else yield 0
    """
    mx = -1
    for x in row:
        if x > mx:
            mx = x
            yield 1
        else:
            yield 0


def trees_visible_from_left(row):
    """
    Return a list of 1s and 0s, where 1 indicates that the tree is visible from
    the left (i.e. there are no taller trees blocking the view of it) and
    0 indicates the tree is not visible
    """
    return list(greatest_so_far(row))


def trees_visible_in_row(row):
    """
    Return a list of 1s and 0s, where 1 indicates that the tree is visible
    from either the left or right.
    """
    return list(map(lambda a, b: a or b,
                    trees_visible_from_left(row),
                    reversed(trees_visible_from_left(reversed(row)))))


def trees_visible_horiz(grid):
    """
    Compute the horizontally visible trees for the entire tree grid
    """
    return [trees_visible_in_row(row) for row in grid]


def trees_visible_count(grid):
    """
    Count the number of trees that are visible from outside the grid
    from any direction
    """
    return sum(map(lambda a, b: a or b,
                   flatten(trees_visible_horiz(grid)),
                   flatten(transpose(trees_visible_horiz(transpose(grid))))))


def tree_distance(row, i):
    """
    Return a tuple indicating the number of trees visible to the left and right
    of the tree in the `i`th position in `row`
    """
    t = row[i]
    l = [] if i == 0 else row[i-1::-1]
    r = row[i+1:]
    return (min(len(l), 1+sum(1 for _ in takewhile(lambda x: x < t, l))),
            min(len(r), 1+sum(1 for _ in takewhile(lambda x: x < t, r))))


def tree_distance_in_row(row):
    """
    Computes the tree distance tuples for each element in a row
    """
    return [tree_distance(row, i) for i in range(len(row))]


def tree_distance_horiz(grid):
    """
    Computes the horizontal tree distance tuples for all elements in the grid
    """
    return [tree_distance_in_row(row) for row in grid]


def scenic_scores(grid):
    """
    Computes the *scenic score* for every position in the grid, where
    the scenic score is defined to be the product of the tree viewing distances
    in each of the four directions.
    """
    return map(lambda a, b: a[0]*a[1]*b[0]*b[1],
               flatten(tree_distance_horiz(grid)),
               flatten(transpose(tree_distance_horiz(transpose(grid)))))


def max_scenic_score(grid):
    """
    Returns the maximum scenic score of any tree in the grid
    """
    return max(scenic_scores(grid))


# Puzzle solutions


def part1(input):
    """
    Consider your map; how many trees are visible from outside the grid?
    """
    return trees_visible_count(input)


def part2(input):
    """
    Consider each tree on your map. What is the highest scenic score possible 
    for any tree?
    """
    return max_scenic_score(input)


day08_soln = AoCSolution(parse, part1, part2)
