"""Solution to https://adventofcode.com/2015/day/13"""
import itertools as it
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


def arrangements(prefs: dict):
    people = prefs.keys()
    p1 = toolz.first(people)
    return ((p1, *x) for x in it.permutations(it.islice(people, 1, None)))
