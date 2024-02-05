import aoc2015.day17 as d17
import utils.core as u

d17_s00_raw = ["15", "20", "5", "10", "5"]
d17_s00 = [20, 15, 10, 5, 5]


def test_parse():
    assert d17_s00 == d17.parse(d17_s00_raw)


def test_combinations():
    assert [] == d17.combinations(10, [5])
    assert [[8]] == d17.combinations(8, [8])
    assert [[5]] == d17.combinations(0, [1, 2, 3, 4,], [5])
    assert [[3, 2]] == d17.combinations(5, [3, 2])
    assert [[3, 2], [3, 2]] == d17.combinations(5, [3, 2, 2])

    assert [[20, 5], [20, 5], [15, 10], [15, 5, 5]] == \
        d17.combinations(25, d17_s00)


def test_combination_count():
    assert 0 == d17.combination_count(10, [5])
    assert 1 == d17.combination_count(8, [8])
    assert 1 == d17.combination_count(0, [1, 2, 3, 4])
    assert 1 == d17.combination_count(5, [3, 2])
    assert 2 == d17.combination_count(5, [3, 2, 2])

    assert 4 == d17.combination_count(25, d17_s00)


def test_min_container_combination_count():
    assert 3 == d17.min_container_combination_count(25, d17_s00)


day17_input = d17.parse(u.standard_puzzle_input(year=2015, day=17))


def test_part1():
    assert 654 == d17.part1(day17_input)


def test_part2():
    assert 57 == d17.part2(day17_input)
