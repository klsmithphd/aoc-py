"""Solution to https://adventofcode.com/2015/day/13"""
import itertools as it
import more_itertools as mit
import toolz


# Input parsing
def parse_line(line: str):
    pieces = line.split()
    person1 = pieces[0]
    gain_or_loss = 1 if pieces[2] == 'gain' else -1
    amount = int(pieces[3])
    person2 = pieces[10][:-1]
    return (person1, person2, gain_or_loss * amount)


def parse(input):
    groups = it.groupby((parse_line(x) for x in input), lambda x: x[0])
    return {p1: {p2: h for _, p2, h in v} for p1, v in groups}


# Puzzle logic
def arrangements(prefs: dict):
    """Returns the (n-1)! possible arrangements of the guests around the table.

    Technically there should be only half of that number to account because
    the clockwise/counter-clockwise orderings around the table are equivalent"""
    people = prefs.keys()
    p1 = toolz.first(people)
    return ((p1, *x) for x in it.permutations(it.islice(people, 1, None)))


def table_circle(coll: list):
    """Takes a collection of n elements and makes it into a collection 2 items
    longer, wrapping around the first and second elements to the end, i.e.,
    it take [1, 2, 3, 4] and turns it into [1, 2, 3, 4, 1, 2]. This can
    then be used to take 3 elements at a time and compute the happiness
    of the center person"""
    return it.chain(coll, coll[:2])


def happiness(prefs, triad):
    """Computes a happiness score for a given guest based on who their 
    neighbors are and their known preferences"""
    n1, guest, n2 = triad
    return prefs[guest][n1] + prefs[guest][n2]


def happiness_total(prefs: dict, order: list):
    """Compute the total happiness score for the given ordering of guests"""
    triads = mit.windowed(table_circle(order), 3, 1)
    return sum(happiness(prefs, triad) for triad in triads)


def max_happiness(prefs):
    """Finds the maximum happiness of any possible configuration of guests"""
    return max(happiness_total(prefs, order) for order in arrangements(prefs))


def add_me(prefs: dict):
    """Insert a new node (me) into the mix, whose happiness scores all all zero"""
    def with_me(v: dict):
        v.update({'Me': 0})
        return v
    new_prefs = {k: with_me(v) for k, v in prefs.items()}
    new_prefs.update({"Me": {g: 0 for g in prefs.keys()}})
    return new_prefs


# Puzzle solutions
def part1(input):
    """Find the maximum happiness score possible for all guests."""
    return max_happiness(input)


def part2(input):
    """Find the maximum happiness score including me in the seating plan"""
    return max_happiness(add_me(input))
