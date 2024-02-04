import aoc2015.day15 as d15
import utils.core as u

d15_s00_raw = [
    "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
    "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"
]

d15_s00 = [[-1, -2, 6, 3, 8],
           [2, 3, -2, -1, 3]]


def test_parse():
    """Correctly parses the input"""
    assert d15_s00 == d15.parse(d15_s00_raw)


def test_score_vec():
    """Computes the score component vector"""
    assert [68, 80, 152, 76, 520] == d15.score_vec(d15_s00, [44, 56])
    assert [80, 100, 120, 60, 500] == d15.score_vec(d15_s00, [40, 60])


def test_score():
    """Computes the cookie score"""
    # The score component vector for the 44/56 split
    assert 62842880 == d15.score([68, 80, 152, 76, 520])
    # The score component vector for the 40/60 split
    assert 57600000 == d15.score([80, 100, 120, 60, 500])


def test_all_options():
    """Can generate all combinations of n vars that sum to a total"""
    assert d15.all_options(2, 2) == [[2, 0], [1, 1], [0, 2]]
    assert d15.all_options(5, 2) == \
        [[5, 0], [4, 1], [3, 2], [2, 3], [1, 4], [0, 5]]
    assert d15.all_options(2, 3) == \
        [[2, 0, 0],
         [1, 1, 0], [1, 0, 1],
         [0, 2, 0], [0, 1, 1], [0, 0, 2]]
    assert d15.all_options(2, 4) == \
        [[2, 0, 0, 0],
         [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1],
         [0, 2, 0, 0], [0, 1, 1, 0], [0, 1, 0, 1],
         [0, 0, 2, 0], [0, 0, 1, 1], [0, 0, 0, 2]]


def test_max_score():
    """Finds the maximum score across all possible combinations"""
    assert 62842880 == d15.max_score(d15_s00)
    assert 57600000 == d15.max_score(d15_s00, cal_constraint=True)


day15_input = d15.parse(u.standard_puzzle_input(year=2015, day=15))


def test_part1():
    assert 21367368 == d15.part1(day15_input)


def test_part2():
    assert 1766400 == d15.part2(day15_input)
