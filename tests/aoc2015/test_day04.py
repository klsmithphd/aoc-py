import aoc2015.day04 as d04
import utils.core as u


d04_s00 = "abcdef"
d04_s01 = "pqrstuv"


def test_decimal():
    assert 609043 == d04.decimal(d04_s00, d04.five_zero_start)
    assert 1048970 == d04.decimal(d04_s01, d04.five_zero_start)


day04_input = d04.parse(u.standard_puzzle_input(year=2015, day=4))


def test_part1():
    assert 282749 == d04.part1(day04_input)


def test_part2():
    assert 9962624 == d04.part2(day04_input)
