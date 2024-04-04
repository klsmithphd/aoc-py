import aoc2016.day08 as d08
import utils.core as u

d08_s00_raw = [
    "rect 3x2",
    "rotate column x=1 by 1",
    "rotate row y=0 by 4",
    "rotate column x=1 by 1"
]

d08_s00 = [
    {"cmd": "rect", "width": 3, "height": 2},
    {"cmd": "rotate", "dim": "column", "pos": 1, "amount": 1},
    {"cmd": "rotate", "dim": "row", "pos": 0, "amount": 4},
    {"cmd": "rotate", "dim": "column", "pos": 1, "amount": 1}
]


def test_parse():
    assert d08_s00 == d08.parse(d08_s00_raw)


d08_s00_screen_0 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

d08_s00_screen_1 = [
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

d08_s00_screen_2 = [
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0]
]

d08_s00_screen_3 = [
    [0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0]
]

d08_s00_screen_4 = [
    [0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0]
]


def test_step():
    assert d08_s00_screen_1 == d08.step(d08_s00_screen_0, d08_s00[0])
    assert d08_s00_screen_2 == d08.step(d08_s00_screen_1, d08_s00[1])
    assert d08_s00_screen_3 == d08.step(d08_s00_screen_2, d08_s00[2])
    assert d08_s00_screen_4 == d08.step(d08_s00_screen_3, d08_s00[3])


def test_final_state():
    assert d08_s00_screen_4 == d08.final_state(7, 3, d08_s00)


def test_lit_pixels():
    assert 6 == d08.lit_pixels(d08_s00_screen_4)


day08_input = d08.parse(u.standard_puzzle_input(year=2016, day=8))


def test_part1():
    assert 128 == d08.part1(day08_input)


def test_part2():
    assert "EOARGPHYAO" == d08.part2(day08_input)
