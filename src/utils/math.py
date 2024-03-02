"""Mathematical utility functions"""
import functools as ft


def mod_mul(m, a, b):
    """Computes a*b mod m"""
    return (a * b) % m


def mod_square(m, a):
    """Computes a^2 mod m"""
    return (a * a) % m


def _mod_sq_and_mul(m, a, last, bit: str):
    """Applies the square-and-multiply method to perform fast 
    exponentiation of an integer `a` to the power `n` modulo `m`.

    If the next bit is a zero, return the square of `last` (modulo `m`)
    If the next bit is a one, return the square of `last` times `a` (mod `m`)"""
    if bit == '0':
        return mod_square(m, last)
    else:
        return mod_mul(m, a, mod_square(m, last))


def mod_pow(m, a, n):
    """Computes a^n mod m"""
    if n == 0:
        return 1
    else:
        return ft.reduce(ft.partial(_mod_sq_and_mul, m, a), format(n, 'b'), 1)
