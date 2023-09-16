"""Solution to https://adventofcode.com/2022/day/11"""
from collections import defaultdict, namedtuple
from functools import partial
from itertools import takewhile
from toolz import drop, first, iterate
from utils.core import AoCSolution, split_at_blanklines

# Input parsing

Monkey = namedtuple('Monkey', ['operation', 'divisor', 't_dest', 'f_dest'])
State = namedtuple('State', ['monkeys', 'items'])

L2_START = len("  Starting items: ")
L3_START = len("  Operation: new = ")
L4_START = len("  Test: divisible by ")
L5_START = len("    If true: throw to monkey ")
L6_START = len("    If false: throw to monkey ")


def parse_operation(opstr):
    _, operand, arg = opstr.split()
    return [operand, None if arg == "old" else int(arg)]


def parse_monkey(monkey_spec):
    _, l2, l3, l4, l5, l6 = monkey_spec
    return (Monkey(
        parse_operation(l3[L3_START:]),
        int(l4[L4_START:]),
        int(l5[L5_START:]),
        int(l6[L6_START:])
    ),
        [int(item) for item in l2[L2_START:].split(", ")])


def parse(input):
    monkey_data = [parse_monkey(x) for x in split_at_blanklines(input)]
    return State(monkeys=[monkey[0] for monkey in monkey_data],
                 items=[monkey[1] for monkey in monkey_data])

# Puzzle logic


def dict_of_lists(tuples):
    result = defaultdict(list)
    for k, v in tuples:
        result[k].append(v)
    return result


def operate(operation, item):
    op, arg = operation
    if op == '+':
        return item + arg
    else:
        return item * (arg if arg else item)


def worry(operation, item):
    return operate(operation, item) // 3


def division_test(worry, divisor):
    return worry % divisor == 0


def next_toss(monkey, item):
    operation, divisor, t_dest, f_dest = monkey
    wry = worry(operation, item)
    divides = division_test(wry, divisor)
    dest = t_dest if divides else f_dest
    return (dest, wry)


def next_tosses(monkey, items):
    return dict_of_lists(next_toss(monkey, item) for item in items)


# def turn(monkeys, items, monkey_id):
#     tosses = next_tosses(monkeys[monkey_id], items[monkey_id])
#     new_items = [items[i] + tosses[i] for i in range(len(items))]
#     new_items[monkey_id] = []
#     return new_items

def turn(monkeys, monkey_turn):
    id, items = monkey_turn
    try:
        tosses = next_tosses(monkeys[id], items[id])
        new_items = [items[i] + tosses[i] for i in range(len(items))]
        new_items[id] = []
        return (id+1, new_items)
    except:
        raise IndexError


def round(monkeys, items):
    return first(drop(len(monkeys),
                      iterate(partial(turn, monkeys), (0, items))))[1]


def rounds(monkeys, items):
    return iterate(partial(round, monkeys), items)

# Puzzle solutions

# day11_soln = \
#     AoCSolution(parse,
#                 p1=
#                 p2=)
