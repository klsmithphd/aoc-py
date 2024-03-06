"""Utility functions for working with data on a regular grid"""
import more_itertools as mit
import toolz
import utils.vectors as v

HEADINGS = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
"""Compass headings in clockwise order starting from `n`"""

BEARINGS = ["forward",
            "forward-right",
            "right",
            "backward-right",
            "backward",
            "backward-left",
            "left",
            "forward-left"]
"""Relative bearings in clockwise order starting from `n`"""

CARDINAL_OFFSETS = {
    'n':  (0, 1),
    'ne': (1, 1),
    'e':  (1, 0),
    'se': (1, -1),
    's':  (0, -1),
    'sw': (-1, -1),
    'w':  (-1, 0),
    'nw': (-1, 1)
}
"""The 2D positional offsets corresponding to one unit move in each of the
compass headings"""

REL_BEARINGS = dict(zip(HEADINGS,
                        [dict(zip(x, BEARINGS))
                         for x in mit.circular_shifts(HEADINGS)]))
"""A dict mapping from a given compass heading to a dict mapping other
compass headings to their relative bearing"""

REL_HEADINGS = dict(zip(HEADINGS,
                        [dict(zip(BEARINGS, x))
                         for x in mit.circular_shifts(HEADINGS)]))
"""A dict mapping from a given compass heading to a dict mapping relative
bearings to their respective compass headings."""


def turn(state, bearing):
    """Given a *walker* described by `state`, and a bearing, turn the walker
    to point in a new direction.
    """
    return toolz.assoc(state, 'heading', REL_HEADINGS[state['heading']][bearing])


def forward(state, dist):
    """Given a *walker* described by `state`, and a distance `dist`, update
    the walker's position to have moved `dist` units in whatever direction
    it was pointing."""
    delta = v.scalar_mul(CARDINAL_OFFSETS[state['heading']], dist)
    return toolz.update_in(state, ['pos'], lambda x: v.vec_add(x, delta))


def interpolated(v1, v2):
    """Given a start point and end point for a line segment
    (assumed to be either horizontal or vertical), return all
    the points along the line segment.

    The collection returned will include both the start and end points"""
    x1, y1 = v1
    x2, y2 = v2
    dy = 1 if y1 <= y2 else -1
    dx = 1 if x1 <= x2 else -1
    return [(x, y) for y in range(y1, y2+dy, dy) for x in range(x1, x2+dx, dx)]
