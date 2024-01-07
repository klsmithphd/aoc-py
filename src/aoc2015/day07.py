"""Solution to https://adventofcode.com/2015/day/7"""
import re


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
    return dict(parse_line(line) for line in input)
