"""Solution to https://adventofcode.com/2022/day/11"""
from collections import defaultdict, namedtuple
from functools import partial, reduce
from itertools import accumulate, takewhile
from operator import add
from toolz import drop, first, iterate, nth, take
from utils.core import AoCSolution, split_at_blanklines

# Input parsing

Monkey = namedtuple('Monkey', ['operation',
                               'divisor',
                               't_dest',
                               'f_dest',
                               'counts',
                               'items'])

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
    return Monkey(
        operation=parse_operation(l3[L3_START:]),
        divisor=int(l4[L4_START:]),
        t_dest=int(l5[L5_START:]),
        f_dest=int(l6[L6_START:]),
        counts=0,
        items=[int(item) for item in l2[L2_START:].split(", ")]
    )


def parse(input):
    return [parse_monkey(x) for x in split_at_blanklines(input)]

# Puzzle logic


def items(monkeys):
    return [monkey.items for monkey in monkeys]


def counts(monkeys):
    return [monkey.counts for monkey in monkeys]


# Candidate for util function
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


def mod_add(mod, x, y):
    return (x + y) % mod


def mod_mul(mod, x, y):
    return (x * y) % mod


def mod_operate(operation, item):
    op, arg = operation
    mod, rem = item
    if op == '+':
        return (mod, mod_add(mod, rem, arg))
    else:
        return (mod, mod_mul(mod, rem, (arg if arg else rem)))


def worry(operation, item):
    return operate(operation, item) // 3


def mod_worry(operation, item):
    return dict(map(lambda x: mod_operate(operation, x), item.items()))


def division_test(worry, divisor):
    return worry % divisor == 0


def mod_division_test(worry, divisor):
    return worry.get(divisor) == 0


def next_toss(id, monkeys):
    monkey = monkeys[id]
    operation, divisor, t_dest, f_dest, counts, items = monkey
    wry = worry(operation, items[0])
    divides = division_test(wry, divisor)
    dest = t_dest if divides else f_dest
    new_monkeys = [x for x in monkeys]
    new_monkeys[id] = monkey._replace(items=items[1:],
                                      counts=counts+1)
    new_monkeys[dest] = \
        monkeys[dest]._replace(items=monkeys[dest].items + [wry])
    return new_monkeys


def next_toss_part2(id, monkeys):
    monkey = monkeys[id]
    operation, divisor, t_dest, f_dest, counts, items = monkey
    wry = mod_worry(operation, items[0])
    divides = mod_division_test(wry, divisor)
    dest = t_dest if divides else f_dest
    new_monkeys = [x for x in monkeys]
    new_monkeys[id] = monkey._replace(items=items[1:],
                                      counts=counts+1)
    new_monkeys[dest] = \
        monkeys[dest]._replace(items=monkeys[dest].items + [wry])
    return new_monkeys


def turn(monkeys, id):
    next_monkeys = monkeys
    while len(next_monkeys[id].items) > 0:
        next_monkeys = next_toss(id, next_monkeys)
    return next_monkeys


def turn_part2(monkeys, id):
    next_monkeys = monkeys
    while len(next_monkeys[id].items) > 0:
        next_monkeys = next_toss_part2(id, next_monkeys)
    return next_monkeys


def round(monkeys):
    return reduce(turn, range(len(monkeys)), monkeys)


def round_part2(monkeys):
    return reduce(turn_part2, range(len(monkeys)), monkeys)


def rounds(monkeys):
    return iterate(round, monkeys)


def rounds_part2(monkeys):
    return iterate(round_part2, monkeys)


def monkey_business(monkeys, n):
    a, b = take(2, sorted(counts(nth(n, rounds(monkeys))), reverse=True))
    return a * b


def remainders(item):
    """
    Returns a dict, where the keys are the first ten prime numbers
    and the values are the mods (remainders) of `item` relative to each
    of those prime numbers
    """
    primes = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23]
    return dict(zip(primes, map(lambda x: item % x, primes)))


def remainderize(monkey):
    """
    For a given monkey, replaces each monkey's items with a dict of 
    the first ten prime numbers and the mod of the item value with those
    primes.
    """
    return monkey._replace(items=[remainders(item) for item in monkey.items])


def part2_augment(monkeys):
    return [remainderize(monkey) for monkey in monkeys]


def monkey_business_part2(monkeys, n):
    a, b = take(2, sorted(counts(nth(n, rounds_part2(part2_augment(monkeys)))),
                          reverse=True))
    return a * b


# Puzzle solutions

def part1(input):
    return monkey_business(input, 20)


def part2(input):
    return monkey_business_part2(input, 10000)

# day11_soln = \
#     AoCSolution(parse,
#                 p1=
#                 p2=)
