from aoc2022.day05 import parse_input, part1, part2, step, stack_tops
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
d05_input = parse_input(standard_puzzle_input(year=2022, day=5))


def test_parse_input():
    assert d05_s01 == {"stacks": {1: ['Z', 'N'],
                                  2: ['M', 'C', 'D'],
                                  3: ['P']},
                       "moves": [(1, 2, 1),
                                 (3, 1, 3),
                                 (2, 2, 1),
                                 (1, 1, 2)]}


d05_s01_part1_step0 = d05_s01['stacks']
d05_s01_part1_step1 = {1: ['Z', 'N', 'D'],
                       2: ['M', 'C'],
                       3: ['P']}
d05_s01_part1_step2 = {1: [],
                       2: ['M', 'C'],
                       3: ['P', 'D', 'N', 'Z']}
d05_s01_part1_step3 = {1: ['C', 'M'],
                       2: [],
                       3: ['P', 'D', 'N', 'Z']}
d05_s01_part1_step4 = {1: ['C'],
                       2: ['M'],
                       3: ['P', 'D', 'N', 'Z']}

d05_s01_part2_step2 = {1: [],
                       2: ['M', 'C'],
                       3: ['P', 'Z', 'N', 'D']}
d05_s01_part2_step3 = {1: ['M', 'C'],
                       2: [],
                       3: ['P', 'Z', 'N', 'D']}
d05_s01_part2_step4 = {1: ['M'],
                       2: ['C'],
                       3: ['P', 'Z', 'N', 'D']}


def test_step():
    assert d05_s01_part1_step1 == step(d05_s01_part1_step0, (1, 2, 1))
    assert d05_s01_part1_step2 == step(d05_s01_part1_step1, (3, 1, 3))
    assert d05_s01_part1_step3 == step(d05_s01_part1_step2, (2, 2, 1))
    assert d05_s01_part1_step4 == step(d05_s01_part1_step3, (1, 1, 2))

    assert d05_s01_part1_step1 == step(d05_s01_part1_step0, (1, 2, 1), False)
    assert d05_s01_part2_step2 == step(d05_s01_part1_step1, (3, 1, 3), False)
    assert d05_s01_part2_step3 == step(d05_s01_part2_step2, (2, 2, 1), False)
    assert d05_s01_part2_step4 == step(d05_s01_part2_step3, (1, 1, 2), False)


def test_stack_tops():
    assert 'CMZ' == stack_tops(d05_s01_part1_step4)
    assert 'MCD' == stack_tops(d05_s01_part2_step4)


def test_day05_part1_soln():
    assert 'CNSZFDVLJ' == part1(d05_input)


def test_day05_part2_soln():
    assert 'QNDWLMGNS' == part2(d05_input)


# def test_day05_part1_soln():
#     assert 1 == day05_soln.part1(d05_input)


# def test_day05_part2_soln():
#     assert 1 == day05_soln.part2(d05_input)
