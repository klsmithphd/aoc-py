from aoc2022.day02 import parse, interpret, outcomes, round_score, \
    total_score, day02_part1
from utils.core import parse_puzzle_input
from pipe import map

d02_s01_raw = """A Y
B X
C Z
""".splitlines()

d02_s01 = parse(d02_s01_raw)


def test_parse():
    assert d02_s01 == [['A', 'Y'], ['B', 'X'], ['C', 'Z']]


part1_pairs = [["rock", "paper"],
               ["paper", "rock"],
               ["scissors", "scissors"]]


def test_interpret():
    assert part1_pairs == list(d02_s01 | map(interpret))


def test_outcomes():
    assert ["win", "lose", "draw"] == list(part1_pairs | map(outcomes))


def test_round_score():
    assert [8, 1, 6] == list(part1_pairs | map(round_score))


def test_total_score():
    assert 15 == total_score(d02_s01)


d02_input = parse_puzzle_input(parse, year=2022, day=2)


def test_day02_part1_soln():
    assert 11906 == day02_part1(d02_input)
