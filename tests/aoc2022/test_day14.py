from aoc2022.day14 import parse, part1, part2, parse_line, next_grain_pos, grains_deposited
from utils.core import standard_puzzle_input

d14_s0_raw = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()

d14_s0_coords = [[(498, 4), (498, 6), (496, 6)],
                 [(503, 4), (502, 4), (502, 9), (494, 9)]]

d14_s0 = {  (498, 4),
            (498, 5),
            (498, 6),
            (497, 6),
            (496, 6),
            (503, 4),
            (502, 4),
            (502, 5),
            (502, 6),
            (502, 7),
            (502, 8),
            (502, 9),
            (501, 9),
            (500, 9),
            (499, 9),
            (498, 9),
            (497, 9),
            (496, 9),
            (495, 9),
            (494, 9)}


def test_parse_line():
    assert d14_s0_coords == [parse_line(x) for x in d14_s0_raw]


def test_parse():
    assert d14_s0 == parse(d14_s0_raw)

def test_next_grain_pos():
    the_rocks = set(d14_s0)
    next_grains = [(500, 8), (499, 8), (501, 8), (500, 7), (498, 8)]

    for next_grain in next_grains:
        assert next_grain == next_grain_pos(the_rocks, 9)
        the_rocks.add(next_grain)


def test_grains_until_stopped():
    assert 24 == grains_deposited(d14_s0)
    assert 93 == grains_deposited(d14_s0, False)


d14_input = parse(standard_puzzle_input(year=2022, day=14))


def test_day14_part1_soln():
    assert 913 == part1(d14_input)


def test_day14_part2_soln():
    assert 30762 == part2(d14_input)
