"""Solution to https://adventofcode.com/2015/day/7"""
import frozendict
import functools as ft
import re


# Input parsing
def tokenize(s: str):
    return int(s) if s.isnumeric() else s


def parse_assign(s: str):
    return ("assign", tokenize(s))


def parse_unary(s: str):
    op, a = s.split(" ")
    return (op.lower(), (tokenize(a),))


def parse_binary(s: str):
    a, op, b = s.split(" ")
    return (op.lower(), (tokenize(a), tokenize(b)))


def parse_line(line: str):
    op, dest = line.split(" -> ")
    if re.search(r"AND|OR|SHIFT", op):
        inst = parse_binary(op)
    elif re.search(r"NOT", op):
        inst = parse_unary(op)
    else:
        inst = parse_assign(op)
    return (tokenize(dest), inst)


def parse(input):
    return frozendict.frozendict(parse_line(line) for line in input)


# Puzzle logic
@ft.cache
def wire_val(circuit, wire):
    """Determines the signal provided to the given wire by the circuit by
    recursively evaluating its connections in the circuit.

    This approach requires memoization provided by functools' cache decoration"""
    op, args = circuit[wire]
    match op:
        case "assign":
            return wire_val(circuit, args) if isinstance(args, str) else args
        case "or":
            return wire_val(circuit, args[0]) | wire_val(circuit, args[1])
        case "and":
            if isinstance(args[0], int):
                return args[0] & wire_val(circuit, args[1])
            else:
                return wire_val(circuit, args[0]) & wire_val(circuit, args[1])
        case "lshift":
            return wire_val(circuit, args[0]) << args[1]
        case "rshift":
            return wire_val(circuit, args[0]) >> args[1]
        case "not":
            # We need to AND with 2^16-1 (65535) in order to trim out the
            # higher order bits present after we bit-not the value
            # This wouldn't be necessary if we could guarantee we're working
            # with 2-byte (16-bit) unsigned integers
            return 65535 & ~wire_val(circuit, args[0])


# Puzzle solutions
def part1(input):
    """Determine the signal provided to wire a"""
    return wire_val(input, "a")


def part2(input):
    """Take the signal from a in part1, feed it to wire b, and recompute 
    a's signal"""
    a_val = wire_val(input, "a")
    new_circuit = input.set("b", ("assign", a_val))
    return wire_val(new_circuit, "a")
