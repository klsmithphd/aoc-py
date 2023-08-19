from aoc2022.day05 import parse_input
from utils.core import standard_puzzle_input

d05_s01_raw = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".splitlines()

d05_s01 = parse_input(d05_s01_raw)


def test_parse_input():
    assert d05_s01 == {"stacks": {1: ["Z", "N"],
                                  2: ["M", "C", "D"],
                                  3: ["P"]},
                       "moves": [{"qty": 1, "from": 2, "to": 1},
                                 {"qty": 3, "from": 1, "to": 3},
                                 {"qty": 2, "from": 2, "to": 1},
                                 {"qty": 1, "from": 1, "to": 2}]}

# d05_input = standard_puzzle_input(year=2022, day=5)


# def test_day05_part1_soln():
#     assert 1 == day05_soln.part1(d05_input)


# def test_day05_part2_soln():
#     assert 1 == day05_soln.part2(d05_input)
