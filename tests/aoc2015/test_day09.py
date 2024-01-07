import aoc2015.day09 as d09
import utils.core as u


d09_s00_raw = [
    "London to Dublin = 464",
    "London to Belfast = 518",
    "Dublin to Belfast = 141"
]

d09_s00 = {
    "London":  {"Dublin": 464, "Belfast": 518},
    "Dublin":  {"London": 464, "Belfast": 141},
    "Belfast": {"London": 518, "Dublin":  141}}


def test_parse():
    assert d09_s00 == d09.parse(d09_s00_raw)


def test_route_distance():
    assert 982 == d09.route_distance(d09_s00, ["Dublin", "London", "Belfast"])
    assert 605 == d09.route_distance(d09_s00, ["London", "Dublin", "Belfast"])
    assert 659 == d09.route_distance(d09_s00, ["London", "Belfast", "Dublin"])
    assert 659 == d09.route_distance(d09_s00, ["Dublin", "Belfast", "London"])
    assert 605 == d09.route_distance(d09_s00, ["Belfast", "Dublin", "London"])
    assert 982 == d09.route_distance(d09_s00, ["Belfast", "London", "Dublin"])


day09_input = d09.parse(u.standard_puzzle_input(year=2015, day=9))


def test_part1():
    assert 207 == d09.part1(day09_input)


def test_part2():
    assert 804 == d09.part2(day09_input)
