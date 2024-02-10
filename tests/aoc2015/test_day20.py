import aoc2015.day20 as d20
import utils.core as u


def test_parse():
    assert 10 == d20.parse(["10"])


def test_presents():
    assert [1, 3, 4, 7, 6, 12, 8, 15, 13, 18] == d20.presents(10)


def test_house_with_n_presents():
    assert 4 == d20.house_with_n_presents(5, 10)
    assert 8 == d20.house_with_n_presents(14, 10)


day20_input = d20.parse(u.standard_puzzle_input(year=2015, day=20))
print(day20_input)


def test_part1():
    assert 776160 == d20.part1(day20_input)


def test_part2():
    assert 786240 == d20.part2(day20_input)
