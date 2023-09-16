from aoc2022.day11 import parse, part1, Monkey, next_toss, items, turn, round, rounds, \
    counts, monkey_business
from toolz import nth, take
from utils.core import standard_puzzle_input

d11_s01_raw = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".splitlines()

d11_s01 = [
    Monkey(operation=['*',   19], divisor=23, t_dest=2, f_dest=3, counts=0,
           items=[79, 98]),
    Monkey(operation=['+',    6], divisor=19, t_dest=2, f_dest=0, counts=0,
           items=[54, 65, 75, 74]),
    Monkey(operation=['*', None], divisor=13, t_dest=1, f_dest=3, counts=0,
           items=[79, 60, 97]),
    Monkey(operation=['+',    3], divisor=17, t_dest=0, f_dest=1, counts=0,
           items=[74])
]


def test_parse():
    assert d11_s01 == parse(d11_s01_raw)


def test_turn():
    assert [[],
            [54, 65, 75, 74],
            [79, 60, 97],
            [74, 500, 620]] == items(turn(d11_s01, 0))
    # assert [[20, 23, 27, 26],
    #         [],
    #         [79, 60, 97],
    #         [74, 500, 620]] == \
    #     turn(d11_s01.monkeys,
    #          (1,
    #           [[],
    #            [54, 65, 75, 74],
    #               [79, 60, 97],
    #               [74, 500, 620]]))
#     assert (3,
#             [[20, 23, 27, 26],
#              [2080],
#              [],
#              [74, 500, 620, 1200, 3136]]) == \
#         turn(d11_s01.monkeys,
#              (2,
#               [[20, 23, 27, 26],
#                [],
#                   [79, 60, 97],
#                   [74, 500, 620]]))
#     assert (4,
#             [[20, 23, 27, 26],
#              [2080, 25, 167, 207, 401, 1046],
#              [],
#              []]) == \
#         turn(d11_s01.monkeys,
#              (3,
#               [[20, 23, 27, 26],
#                [2080],
#                   [],
#                   [74, 500, 620, 1200, 3136]]))


def test_round():
    assert [[20, 23, 27, 26],
            [2080, 25, 167, 207, 401, 1046],
            [],
            []] == items(round(d11_s01))
    assert [[695, 10, 71, 135, 350],
            [43, 49, 58, 55, 362],
            [],
            []] == items(round(round(d11_s01)))
    assert [[16, 18, 21, 20, 122],
            [1468, 22, 150, 286, 739],
            [],
            []] == items(round(round(round(d11_s01))))
    assert [[83, 44, 8, 184, 9, 20, 26, 102],
            [110, 36],
            [],
            []] == items(nth(15, rounds(d11_s01)))
    assert [[10, 12, 14, 26, 34],
            [245, 93, 53, 199, 115],
            [],
            []] == items(nth(20, rounds(d11_s01)))


def test_counts():
    assert [2, 4, 3, 5] == counts(round(d11_s01))
    assert [101, 95, 7, 105] == counts(nth(20, rounds(d11_s01)))


def test_monkey_business():
    assert 10605 == monkey_business(d11_s01, 20)


d11_input = parse(standard_puzzle_input(year=2022, day=11))


def test_day11_part1_soln():
    assert 112221 == part1(d11_input)


# # def test_day11_part2_soln():
# #     assert 1 == day11_soln.part2(d11_input)
