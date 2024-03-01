import aoc2015.day24 as d24
import utils.core as u


d24_s00_raw = ["1", "2", "3", "4", "5",
               "7", "8", "9", "10", "11"]

d24_s00 = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]


def test_parse():
    assert d24_s00 == d24.parse(d24_s00_raw)


def test_smallest_passenger_packages():
    assert [(9, 11)] == d24.smallest_passenger_packages(3, d24_s00)
    assert [(4, 11),
            (5, 10),
            (7, 8)] == d24.smallest_passenger_packages(4, d24_s00)


def test_ideal_quantum_entanglement():
    assert 99 == d24.ideal_quantum_entanglement(3, d24_s00)
    assert 44 == d24.ideal_quantum_entanglement(4, d24_s00)


day24_input = d24.parse(u.standard_puzzle_input(year=2015, day=24))


def test_part1():
    assert 11846773891 == d24.part1(day24_input)


def test_part2():
    assert 80393059 == d24.part2(day24_input)
