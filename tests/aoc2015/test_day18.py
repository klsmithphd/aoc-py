import aoc2015.day18 as d18
import utils.core as u

d18_s00_raw = [
    ".#.#.#",
    "...##.",
    "#....#",
    "..#...",
    "#.#..#",
    "####.."
]

d18_s00 = (6, {
    (1, 0), (3, 0), (5, 0),
    (3, 1), (4, 1),
    (0, 2), (5, 2),
    (2, 3),
    (0, 4), (2, 4), (5, 4),
    (0, 5), (1, 5), (2, 5), (3, 5)
})

d18_s00_step1 = (6, {
    (2, 0), (3, 0),
    (2, 1), (3, 1), (5, 1),
    (3, 2), (4, 2),
    (0, 4),
    (0, 5), (2, 5), (3, 5)
})

d18_s00_step2 = (6, {
    (2, 0), (3, 0), (4, 0),
    (2, 2), (3, 2), (4, 2),
    (1, 4),
    (1, 5)
})

d18_s00_step3 = (6, {
    (3, 0),
    (3, 2),
    (2, 3), (3, 3)
})

d18_s00_step4 = (6, {
    (2, 2), (3, 2),
    (2, 3), (3, 3)
})


def test_parse():
    assert d18_s00 == d18.parse(d18_s00_raw)


def test_neighbors():
    assert [(-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)] == list(d18.neighbors(0, 0))


def test_on_neighbors():
    assert 1 == d18.on_neighbors(d18_s00[1], 0, 0)
    assert 4 == d18.on_neighbors(d18_s00[1], 4, 0)
    assert 2 == d18.on_neighbors(d18_s00[1], 5, 3)


def test_step():
    assert d18_s00_step1 == d18.step(d18_s00)
    assert d18_s00_step2 == d18.step(d18_s00_step1)
    assert d18_s00_step3 == d18.step(d18_s00_step2)
    assert d18_s00_step4 == d18.step(d18_s00_step3)


def test_lights_at_n():
    assert 11 == d18.lights_at_n(d18_s00, 1)
    assert 8 == d18.lights_at_n(d18_s00, 2)
    assert 4 == d18.lights_at_n(d18_s00, 3)
    assert 4 == d18.lights_at_n(d18_s00, 4)


day18_input = d18.parse(u.standard_puzzle_input(year=2015, day=18))


def test_part1():
    assert 1061 == d18.part1(day18_input)


def test_part2():
    assert 1006 == d18.part2(day18_input)
