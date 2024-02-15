import aoc2015.day23 as d23
import utils.core as u

d23_s00_raw = [
    "inc a",
    "jio a, +2",
    "tpl a",
    "inc a"
]

d23_s00 = [
    d23.Inst("inc", "a"),
    d23.Inst("jio", "a", 2),
    d23.Inst("tpl", "a"),
    d23.Inst("inc", "a")
]


def test_parse():
    assert d23_s00 == d23.parse(d23_s00_raw)


def test_run_program():
    assert d23.State(2, 0, 4) == d23.run_program(d23_s00, d23.INIT_STATE)


day23_input = d23.parse(u.standard_puzzle_input(year=2015, day=23))


def test_part1():
    assert 184 == d23.part1(day23_input)


def test_part2():
    assert 231 == d23.part2(day23_input)
