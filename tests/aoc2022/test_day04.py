from aoc2022.day04 import day04_soln, parse, isfully_contained, fully_contained_count
from utils.core import standard_puzzle_input

d04_sample = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()


def test_parse():
    assert [[[2, 4], [6, 8]],
            [[2, 3], [4, 5]],
            [[5, 7], [7, 9]],
            [[2, 8], [3, 7]],
            [[6, 6], [4, 6]],
            [[2, 6], [4, 8]]] == list(parse(d04_sample))


def test_isfully_contained():
    assert False == isfully_contained([2, 4], [6, 8])
    assert False == isfully_contained([2, 3], [4, 5])
    assert False == isfully_contained([5, 7], [7, 9])
    assert True == isfully_contained([2, 8], [3, 7])
    assert True == isfully_contained([6, 6], [4, 6])
    assert False == isfully_contained([2, 6], [4, 8])


def test_fully_contained_count():
    assert 2 == fully_contained_count(parse(d04_sample))


d04_input = standard_puzzle_input(year=2022, day=4)


def test_day04_part1_soln():
    assert 584 == day04_soln.part1(d04_input)


# def test_day04_part2_soln():
#     assert 1 == day04_soln.part2(d04_input)
