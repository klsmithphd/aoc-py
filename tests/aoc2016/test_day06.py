import aoc2016.day06 as d06
import utils.core as u

d06_s00 = [
    "eedadn",
    "drvtee",
    "eandsr",
    "raavrd",
    "atevrs",
    "tsrnev",
    "sdttsa",
    "rasrtv",
    "nssdts",
    "ntnada",
    "svetve",
    "tesnvt",
    "vntsnd",
    "vrdear",
    "dvrsen",
    "enarar"
]


def test_most_frequent_chars():
    assert "easter" == d06.most_frequent_chars(d06_s00)


def test_least_frequent_chars():
    assert "advent" == d06.least_frequent_chars(d06_s00)


day06_input = d06.parse(u.standard_puzzle_input(year=2016, day=6))


def test_part1():
    assert "agmwzecr" == d06.part1(day06_input)


def test_part2():
    assert "owlaxqvq" == d06.part2(day06_input)
