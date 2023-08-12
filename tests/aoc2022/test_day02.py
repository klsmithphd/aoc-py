from aoc2022.day02 import parse, interpret1, interpret2, fill_in, \
    round_score, total_score, day02_part1, day02_part2
from utils.core import parse_puzzle_input
from pipe import map

d02_s01_raw = """A Y
B X
C Z
""".splitlines()

d02_s01 = parse(d02_s01_raw)


def test_parse():
    assert d02_s01 == [['A', 'Y'], ['B', 'X'], ['C', 'Z']]


part1_interpretation = [["rock", "paper", None],
                        ["paper", "rock", None],
                        ["scissors", "scissors", None]]

part2_interpretation = [["rock", None, "draw"],
                        ["paper", None, "lose"],
                        ["scissors", None, "win"]]


def test_interpret1():
    assert part1_interpretation == list(d02_s01 | map(interpret1))


def test_interpret2():
    assert part2_interpretation == list(d02_s01 | map(interpret2))


part1_filled_in = [["rock", "paper", "win"],
                   ["paper", "rock", "lose"],
                   ["scissors", "scissors", "draw"]]

part2_filled_in = [["rock", "rock", "draw"],
                   ["paper", "rock", "lose"],
                   ["scissors", "rock", "win"]]


def test_fill_in():
    assert part1_filled_in == list(part1_interpretation | map(fill_in))
    assert part2_filled_in == list(part2_interpretation | map(fill_in))


def test_round_score():
    assert [8, 1, 6] == list(part1_filled_in | map(round_score))
    assert [4, 1, 7] == list(part2_filled_in | map(round_score))


def test_total_score():
    assert 15 == total_score(d02_s01, interpret1)
    assert 12 == total_score(d02_s01, interpret2)


d02_input = parse_puzzle_input(parse, year=2022, day=2)


def test_day02_part1_soln():
    assert 11906 == day02_part1(d02_input)


def test_day02_part2_soln():
    assert 11186 == day02_part2(d02_input)
