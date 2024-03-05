"""Utility functions for working with data on a regular grid"""
import more_itertools as mit
import toolz
import utils.vectors as v

HEADINGS = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
BEARINGS = ["forward",
            "forward-right",
            "right",
            "backward-right",
            "backward",
            "backward-left",
            "left",
            "forward-left"]

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

REL_BEARINGS = dict(zip(HEADINGS,
                        [dict(zip(x, BEARINGS))
                         for x in mit.circular_shifts(HEADINGS)]))

REL_HEADINGS = dict(zip(HEADINGS,
                        [dict(zip(BEARINGS, x))
                         for x in mit.circular_shifts(HEADINGS)]))


def turn(state, bearing):
    return toolz.assoc(state, 'heading', REL_HEADINGS[state['heading']][bearing])


def forward(state, dist):
    delta = v.scalar_mul(CARDINAL_OFFSETS[state['heading']], dist)
    return toolz.update_in(state, ['pos'], lambda x: v.vec_add(x, delta))
