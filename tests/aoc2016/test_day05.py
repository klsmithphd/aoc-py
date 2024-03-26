import aoc2016.day05 as d05
import more_itertools as mit
import utils.core as u


d05_s00 = "abc"


def test_five_zero_indices():
    assert 3231929 == mit.first(d05.five_zero_indices(d05_s00))


def test_password_part1():
    assert "18f47a30" == d05.password_part1(d05_s00)
