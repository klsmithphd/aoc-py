import aoc2015.day13 as d13
import utils.core as u

d13_s00_raw = [
    "Alice would gain 54 happiness units by sitting next to Bob.",
    "Alice would lose 79 happiness units by sitting next to Carol.",
    "Alice would lose 2 happiness units by sitting next to David.",
    "Bob would gain 83 happiness units by sitting next to Alice.",
    "Bob would lose 7 happiness units by sitting next to Carol.",
    "Bob would lose 63 happiness units by sitting next to David.",
    "Carol would lose 62 happiness units by sitting next to Alice.",
    "Carol would gain 60 happiness units by sitting next to Bob.",
    "Carol would gain 55 happiness units by sitting next to David.",
    "David would gain 46 happiness units by sitting next to Alice.",
    "David would lose 7 happiness units by sitting next to Bob.",
    "David would gain 41 happiness units by sitting next to Carol.",
]

d13_s00 = {
    "Alice": {"Bob": 54,    "Carol": -79, "David": -2},
    "Bob":   {"Alice": 83,  "Carol": -7,  "David": -63},
    "Carol": {"Alice": -62, "Bob": 60,    "David": 55},
    "David": {"Alice": 46,  "Bob": -7,    "Carol": 41}
}

d13_s00_with_me = {
    "Alice": {"Bob": 54,    "Carol": -79, "David": -2,  "Me": 0},
    "Bob":   {"Alice": 83,  "Carol": -7,  "David": -63, "Me": 0},
    "Carol": {"Alice": -62, "Bob": 60,    "David": 55,  "Me": 0},
    "David": {"Alice": 46,  "Bob": -7,    "Carol": 41,  "Me": 0},
    "Me":    {"Alice": 0,   "Bob": 0,     "Carol": 0,  "David": 0}
}


def test_parse():
    assert d13_s00 == d13.parse(d13_s00_raw)


def test_arrangements():
    assert [("Alice", "Bob", "Carol", "David"),
            ("Alice", "Bob", "David", "Carol"),
            ("Alice", "Carol", "Bob", "David"),
            ("Alice", "Carol", "David", "Bob"),
            ("Alice", "David", "Bob", "Carol"),
            ("Alice", "David", "Carol", "Bob")] == \
        list(d13.arrangements(d13_s00))


def test_max_happiness():
    assert 330 == d13.max_happiness(d13_s00)


def test_add_me():
    assert d13_s00_with_me == d13.add_me(d13_s00)


day13_input = d13.parse(u.standard_puzzle_input(year=2015, day=13))


def test_part1():
    assert 709 == d13.part1(day13_input)


def test_part2():
    assert 668 == d13.part2(day13_input)
