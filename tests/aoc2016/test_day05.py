import aoc2016.day05 as d05
import more_itertools as mit
import utils.core as u


d05_s00 = "abc"


def test_five_zero_indices():
    assert 3231929 == mit.first(d05.five_zero_indices(d05_s00))


def test_password_part1():
    assert "18f47a30" == d05.password_part1(d05_s00)


def test_password_part2():
    assert "05ace8e3" == d05.password_part2(d05_s00)


day05_input = d05.parse(u.standard_puzzle_input(year=2016, day=5))


def test_part1():
    assert "f97c354d" == d05.part1(day05_input)


def test_part2():
    assert "863dde27" == d05.part2(day05_input)
