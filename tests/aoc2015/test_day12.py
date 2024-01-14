import aoc2015.day12 as d12
import utils.core as u

d12_s00 = '[1,2,3]'
d12_s01 = '{"a":2,"b":4}'
d12_s02 = '[[[3]]]'
d12_s03 = '{"a":{"b":4},"c":-1}'
d12_s04 = '{"a":[-1,1]}'
d12_s05 = '[-1,{"a":1}]'
d12_s06 = '[]'
d12_s07 = '{}'

d12_s08 = [1, 2, 3]
d12_s09 = [1, {'c': 'red', 'b': 2}, 3]
d12_s10 = {'d': 'red', 'e': [1, 2, 3, 4], 'f': 5}
d12_s11 = [1, 'red', 5]


def test_all_numbers_total():
    assert 6 == d12.all_numbers_total(d12_s00)
    assert 6 == d12.all_numbers_total(d12_s01)
    assert 3 == d12.all_numbers_total(d12_s02)
    assert 3 == d12.all_numbers_total(d12_s03)
    assert 0 == d12.all_numbers_total(d12_s04)
    assert 0 == d12.all_numbers_total(d12_s05)
    assert 0 == d12.all_numbers_total(d12_s06)
    assert 0 == d12.all_numbers_total(d12_s07)


def test_drop_red():
    assert [1, 2, 3] == d12.drop_red(d12_s08)
    assert [1, {}, 3] == d12.drop_red(d12_s09)
    assert {} == d12.drop_red(d12_s10)
    assert [1, 'red', 5] == d12.drop_red(d12_s11)


day12_input = d12.parse(u.standard_puzzle_input(year=2015, day=12))


def test_part1():
    assert 111754 == d12.part1(day12_input)


def test_part2():
    assert 65402 == d12.part2(day12_input)
