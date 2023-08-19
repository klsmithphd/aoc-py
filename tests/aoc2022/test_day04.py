from aoc2022.day04 import parse, part1, part2, isfully_contained, \
    isoverlapping, fully_contained_count, overlapping_count
from utils.core import standard_puzzle_input

d04_s01_raw = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()

d04_s01 = parse(d04_s01_raw)
d04_input = parse(standard_puzzle_input(year=2022, day=4))


def test_parse():
    assert [[[2, 4], [6, 8]],
            [[2, 3], [4, 5]],
            [[5, 7], [7, 9]],
            [[2, 8], [3, 7]],
            [[6, 6], [4, 6]],
            [[2, 6], [4, 8]]] == d04_s01


def test_isfully_contained():
    assert False == isfully_contained([2, 4], [6, 8])
    assert False == isfully_contained([2, 3], [4, 5])
    assert False == isfully_contained([5, 7], [7, 9])
    assert True == isfully_contained([2, 8], [3, 7])
    assert True == isfully_contained([6, 6], [4, 6])
    assert False == isfully_contained([2, 6], [4, 8])


def test_isoverlapping():
    assert False == isoverlapping([2, 4], [6, 8])
    assert False == isoverlapping([2, 3], [4, 5])
    assert True == isoverlapping([5, 7], [7, 9])
    assert True == isoverlapping([2, 8], [3, 7])
    assert True == isoverlapping([6, 6], [4, 6])
    assert True == isoverlapping([2, 6], [4, 8])


def test_fully_contained_count():
    assert 2 == fully_contained_count(d04_s01)


def test_overlapping_count():
    assert 4 == overlapping_count(d04_s01)


def test_day04_part1_soln():
    assert 584 == part1(d04_input)


def test_day04_part2_soln():
    assert 933 == part2(d04_input)
