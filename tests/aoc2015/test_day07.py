import aoc2015.day07 as d07
import frozendict
import utils.core as u

d07_s00_raw = [
    "123 -> x",
    "456 -> y",
    "x AND y -> d",
    "x OR y -> e",
    "x LSHIFT 2 -> f",
    "y RSHIFT 2 -> g",
    "NOT x -> h",
    "NOT y -> i",
    # Added to the sample data to reflect what's in real puzzle input
    "f -> j"
]

d07_s00 = frozendict.frozendict({
    "x": ("assign", 123),
    "y": ("assign", 456),
    "d": ("and",    ("x", "y")),
    "e": ("or",     ("x", "y")),
    "f": ("lshift", ("x", 2)),
    "g": ("rshift", ("y", 2)),
    "h": ("not",    ("x",)),
    "i": ("not",    ("y",)),
    "j": ("assign", "f")
})


def test_parse():
    assert d07_s00 == d07.parse(d07_s00_raw)


def test_wire_val():
    assert 72 == d07.wire_val(d07_s00, "d")
    assert 507 == d07.wire_val(d07_s00, "e")
    assert 492 == d07.wire_val(d07_s00, "f")
    assert 114 == d07.wire_val(d07_s00, "g")
    assert 65412 == d07.wire_val(d07_s00, "h")
    assert 65079 == d07.wire_val(d07_s00, "i")
    assert 123 == d07.wire_val(d07_s00, "x")
    assert 456 == d07.wire_val(d07_s00, "y")
    assert 492 == d07.wire_val(d07_s00, "j")


day07_input = d07.parse(u.standard_puzzle_input(year=2015, day=7))


def test_part1():
    assert 3176 == d07.part1(day07_input)


def test_part2():
    assert 14710 == d07.part2(day07_input)
