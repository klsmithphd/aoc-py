import aoc2015.day07 as d07


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

d07_s00 = {
    "x": ("assign", 123),
    "y": ("assign", 456),
    "d": ("and",    ("x", "y")),
    "e": ("or",     ("x", "y")),
    "f": ("lshift", ("x", 2)),
    "g": ("rshift", ("y", 2)),
    "h": ("not",    ("x",)),
    "i": ("not",    ("y",)),
    "j": ("assign", "f")
}


def test_parse():
    assert d07_s00 == d07.parse(d07_s00_raw)
