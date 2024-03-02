import aoc2015.day25 as d25
import utils.core as u

d25_s00_raw = ["...Enter the code at row 2981, column 3075."]
d25_s00 = [2981, 3075]

CODES = [d25.FIRST_CODE, 31916031, 18749137, 16080970, 21629792,
         17289845, 24592653, 8057251, 16929656, 30943339]


def test_parse():
    assert d25_s00 == d25.parse(d25_s00_raw)


def test_code_number():
    assert 1 == d25.code_number(1, 1)
    assert 2 == d25.code_number(2, 1)
    assert 3 == d25.code_number(1, 2)
    assert 4 == d25.code_number(3, 1)
    assert 5 == d25.code_number(2, 2)
    assert 6 == d25.code_number(1, 3)
    assert 12 == d25.code_number(4, 2)
    assert 15 == d25.code_number(1, 5)


def test_code():
    assert CODES[0] == d25.code(1, 1)
    assert CODES[1] == d25.code(2, 1)
    assert CODES[2] == d25.code(1, 2)
    assert CODES[3] == d25.code(3, 1)
    assert CODES[4] == d25.code(2, 2)
    assert CODES[5] == d25.code(1, 3)
    assert CODES[6] == d25.code(4, 1)
    assert CODES[7] == d25.code(3, 2)
    assert CODES[8] == d25.code(2, 3)
    assert CODES[9] == d25.code(1, 4)


day25_input = d25.parse(u.standard_puzzle_input(year=2015, day=25))


def test_part1():
    assert 9132360 == d25.part1(day25_input)
