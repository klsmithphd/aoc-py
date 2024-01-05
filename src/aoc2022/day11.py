"""Solution to https://adventofcode.com/2022/day/11"""
from collections import defaultdict, namedtuple
from functools import partial, reduce
from operator import add, mul
from toolz import iterate, nth, take
from utils.core import split_at_blanklines

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
    return (add if operand == '+' else mul,
            None if arg == "old" else int(arg))


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
    """Returns the items held by each of the monkeys"""
    return [monkey.items for monkey in monkeys]


def counts(monkeys):
    """Returns the counts of the numbef of items inspected by each of 
    the monkeys"""
    return [monkey.counts for monkey in monkeys]


def dict_of_lists(tuples):  # Candidate for util function
    """Returns a dict where the keys are the unique first elements of
    `tuples`, and the values are a list of the second elements
    that co-occur with the first values. Order will be preserved.

    Example: dict_of_lists( (1, 2), (1, 4), (3, 5), (1, 2))
    returns:
    {1: [2, 4, 2], 3: [5]}"""
    result = defaultdict(list)
    for k, v in tuples:
        result[k].append(v)
    return result


def mod_add(m, x, y):  # Candidate for util function
    """Returns `x` + `y` mod `m`"""
    return (x + y) % m


def mod_mul(m, x, y):  # Candidate for util function
    """Returns `x` * `y` mod `m`"""
    return (x * y) % m


def operate(part, operation, item):
    """Calculate new "worry" levels given the instructions in `operation`
    for the given `item`. `part` should be set to 1 or 2 to use the
    puzzle logic defined for part 1 or 2."""
    op, arg = operation

    match part:
        case 1:
            arg = arg if arg else item
            return op(item, arg)
        case 2:
            mod, rem = item
            arg = arg if arg else rem
            return (mod, op(rem, arg) % mod)


def worry(part, operation, item):
    """Calculate the new worry values, using the logic for each `part` of the
    puzzle. `part` should be set to 1 or 2. Uses each monkey's logic
    defined in `operation` and the current worry value of `item` to
    determine the new worry value."""
    match part:
        case 1:
            return operate(part, operation, item) // 3
        case 2:
            # return dict(map(partial(operate, part, operation), item.items()))
            return dict(map(lambda x: operate(part, operation, x), item.items()))


def division_test(part, worry, divisor):
    """Returns a boolean indicating whether the current worry value is
    divisible by divisor, using the logic in `part` 1 or 2"""
    match part:
        case 1:
            return worry % divisor == 0
        case 2:
            return worry.get(divisor) == 0


def toss_to(part, monkey):
    """Determine the new worry value of the `monkey`s next item
    and the destination monkey to whom it should be tossed. `part` should be 
    set to 1 or 2 to use the logic defined for that part of the puzzle."""
    operation, divisor, t_dest, f_dest, _, items = monkey
    wry = worry(part, operation, items[0])
    divides = division_test(part, wry, divisor)
    dest = t_dest if divides else f_dest
    return (wry, dest)


def next_toss(part, id, monkeys):
    """Returns a new state of all the monkeys after tossing the next
    item held by the monkey indicated by `id`. `part` should be set to 1
    or 2 to use the logic defined for that part of the puzzle."""
    monkey = monkeys[id]
    wry, dest = toss_to(part, monkey)

    new_monkeys = monkeys[:]
    new_monkeys[id] = monkey._replace(items=monkey.items[1:],
                                      counts=monkey.counts+1)
    new_monkeys[dest] = \
        monkeys[dest]._replace(items=monkeys[dest].items + [wry])
    return new_monkeys


def turn(part, monkeys, id):
    """Returns the new state of all monkeys after the monkey indicated
    by `id` has inspected and tossed all of its items. `part` should be
    set to 1 or 2 to use the logic defined for that part of the puzzle."""
    next_monkeys = monkeys
    while len(next_monkeys[id].items) > 0:
        next_monkeys = next_toss(part, id, next_monkeys)
    return next_monkeys


def round(part, monkeys):
    """Returns the new state of all monkeys after each monkey in turn
    (starting with 0) has taken a turn at inspecting and passing 
    all of its items. `part` should be set to 1 or 2 to use the logic
    defined for that part of the puzzle."""
    return reduce(partial(turn, part), range(len(monkeys)), monkeys)


round_1 = partial(round, 1)
round_2 = partial(round, 2)


def rounds(part, monkeys):
    """Returns a (potentially infinite) sequence of each of the rounds
    taken by the monkeys. `part` should be set to 1 or 2 to use the logic
    defined for that part of the puzzle."""
    return iterate(partial(round, part), monkeys)


rounds_1 = partial(rounds, 1)
rounds_2 = partial(rounds, 2)


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
    """In part 2, working with the actual result of applying the operations
    becomes too prohibitively expensive. All we actually need to know is
    whether the worry value is divisible by one of the first ten prime
    numbers (the monkeys' divisors are all prime numbers in this range). 
    As such, we can make the problem tractable by only keeping
    track of the mods of the worry values and applying mod arithmetic
    appropriately. This function will replace the numeric items worry value
    with a map, where the keys are the first ten prime numbers and the
    values are the mods of the worry value relative to those primes. This
    bootstraps the rest of the changes for part 2."""
    return [remainderize(monkey) for monkey in monkeys]


def monkey_business(part, monkeys, n):
    """The monkey business after any given number rounds is defined
    to be the product of the number of items inspected by the two 
    most active monkeys (i.e. the two highest counts of items inspected).
    `n` defines the number of rounds to simulate. `part` should be 1 or 2
    to use the logic defined for that part of the puzzle.
    """
    if part == 2:
        monkeys = part2_augment(monkeys)
    a, b = take(2, sorted(counts(nth(n, rounds(part, monkeys))), reverse=True))
    return a * b


# Puzzle solutions

def part1(input):
    """Figure out which monkeys to chase by counting how many items they 
    inspect over 20 rounds. What is the level of monkey business after 20 
    rounds of stuff-slinging simian shenanigans?"""
    return monkey_business(1, input, 20)


def part2(input):
    """Worry levels are no longer divided by three after each item is 
    inspected; you'll need to find another way to keep your worry levels 
    manageable. Starting again from the initial state in your puzzle input, 
    what is the level of monkey business after 10000 rounds?"""
    return monkey_business(2, input, 10000)
