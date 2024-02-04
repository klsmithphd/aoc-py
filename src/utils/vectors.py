"""Utility functions for vector arithmetic"""
import utils.core as u


def scalar_mul(vec, scale):
    """Multiplies a vector by a scalar.

    Returns an object of the same type (list, tuple, or generator) as vec"""
    scaled = (i * scale for i in vec)
    match vec:
        case tuple():
            return tuple(scaled)
        case list():
            return list(scaled)
        case _:
            return scaled


def vec_sum(vecs):
    """Computes the sum of an iterable collection of vectors.

    Returns an object of the same type (list, tuple, or generator) as the first
    element"""
    first, vs = u.iter_peek(iter(vecs))
    sums = map(sum, zip(*vs))
    match first:
        case tuple():
            return tuple(sums)
        case list():
            return list(sums)
        case _:
            return sums
