"""Solution to https://adventofcode.com/2015/day/18"""
import functools as ft
import itertools as it
import more_itertools as mit


# Constants
ITERATIONS = 100


# Input parsing
@ft.cache
def grid(size):
    """Returns a list of all N x N (x,y) tuples in a square grid of size N"""
    return [(x, y) for y in range(size) for x in range(size)]


def parse(input):
    contents = list(input)
    size = len(contents)
    return (size, {(x, y) for x, y in grid(size) if contents[y][x] == '#'})


# Puzzle logic
@ft.cache
def neighbors(x, y):
    """Generates a list of the 8 neighboring coordinates for position (x,y).

    This function is memoized (cached) because it's going to be called
    O(100) times for each cell in the grid, and the result is identical
    every time"""
    return [(nx, ny)
            for ny in range(y-1, y+2)
            for nx in range(x-1, x+2)
            if (nx, ny) != (x, y)]


def on_neighbors(lights, pos):
    """Counts the number of neighbors that are currently `on` by
    testing whether they are contained in the `lights` set."""
    return sum(1 for nx, ny in neighbors(*pos) if (nx, ny) in lights)


@ft.cache
def corners(size):
    """Returns a set of the four corner coordinates"""
    return {(0, 0), (size-1, 0), (0, size-1), (size-1, size-1)}


def corners_on(size, lights):
    """Updates the state to ensure that the corners are on"""
    return size, lights | corners(size)


def on_condition(lights, pos):
    """A predicate that returns true if the light should be on in the next step.

    A light which is on stays on when 2 or 3 neighbors are on; turns off otherwise.
    A light which is off turns on if 3 neighbors are on; stays off otherwise."""
    return pos in lights and 2 <= on_neighbors(lights, pos) <= 3 \
        or pos not in lights and on_neighbors(lights, pos) == 3


def step(state):
    """Given `state`, which is a tuple of `(size, lights)`, where `size`
    is the dimension of the square grid, and `lights` is a set of all the
    positions of currently on lights, compute the next state according to the
    neighbor rules."""
    size, lights = state
    new_lights = {(x, y) for x, y in grid(size)
                  if on_condition(lights, (x, y))}
    return size, new_lights


def step_corners(state):
    """Similar to `step` above, but ensure that corners are set to `on`"""
    return corners_on(*step(state))


def lights_at_n(state, n, corners=False):
    """Returns the number of lights that are on as of iteration `n`

    If `corners` is set to True, the four corners will be forced to be
    in an `on` state at all times."""
    seq = mit.iterate(step_corners if corners else step, state)
    return len(next(it.islice(seq, n, n+1))[1])


# Puzzle solutions
def part1(input):
    """How many lights are on after 100 iterations?"""
    return lights_at_n(input, ITERATIONS)


def part2(input):
    """How many lights are on after 100 iterations when the corners are kept
    always on"""
    return lights_at_n(corners_on(*input), ITERATIONS, corners=True)
