import aoc2015.day14 as d14
import utils.core as u

d14_s00_raw = [
    "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
    "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."
]

d14_s00 = [
    d14.Reindeer(speed=14, fly=10, span=137),
    d14.Reindeer(speed=16, fly=11, span=173)
]


def test_parse():
    """Correctly parses the input"""
    assert d14_s00 == d14.parse(d14_s00_raw)


def test_position():
    """Finds the distance traveled by each reindeer after 1000 seconds"""
    assert 1120 == d14.position(1000, d14_s00[0])
    assert 1056 == d14.position(1000, d14_s00[1])


def test_cumulative_points():
    """Finds the cumulative points for each reindeer after 1000 seconds"""
    assert [312, 689] == list(d14.cumulative_points(1000, d14_s00))


day14_input = d14.parse(u.standard_puzzle_input(year=2015, day=14))


def test_part1():
    assert 2660 == d14.part1(day14_input)


def test_part2():
    assert 1256 == d14.part2(day14_input)
