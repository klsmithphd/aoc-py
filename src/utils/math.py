"""Mathematical utility functions"""
import functools as ft


def mod_mul(m, a, b):
    """Computes a*b mod m"""
    return (a * b) % m


def mod_square(m, a):
    """Computes a^2 mod m"""
    return (a * a) % m


def mod_pow(m, a, n):
    """Computes a^n mod m"""
    if n == 0:
        return 1
    else:
        # Applies the square-and-multiply method to perform fast
        # exponentiation of an integer `a` to the power `n` modulo `m`.

        # If the next bit is a zero, return the square of `last` (modulo `m`)
        # If the next bit is a one, return the square of `last` # times `a`
        # (modulo `m`)
        def sq_and_mul(last, bit):
            if bit == '0':
                return mod_square(m, last)
            else:
                return mod_mul(m, a, mod_square(m, last))

        return ft.reduce(sq_and_mul, format(n, 'b'), 1)
