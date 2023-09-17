from aoc2022.day11 import parse, part1, part2, Monkey,\
    items, turn, counts, round_1, round_2, rounds_1, rounds_2, \
    monkey_business, part2_augment
from toolz import nth
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
    Monkey(operation=('*',   19), divisor=23, t_dest=2, f_dest=3, counts=0,
           items=[79, 98]),
    Monkey(operation=('+',    6), divisor=19, t_dest=2, f_dest=0, counts=0,
           items=[54, 65, 75, 74]),
    Monkey(operation=('*', None), divisor=13, t_dest=1, f_dest=3, counts=0,
           items=[79, 60, 97]),
    Monkey(operation=('+',    3), divisor=17, t_dest=0, f_dest=1, counts=0,
           items=[74])
]


def test_parse():
    assert d11_s01 == parse(d11_s01_raw)


def test_turn():
    items_after_monkey_0 = [[],
                            [54, 65, 75, 74],
                            [79, 60, 97],
                            [74, 500, 620]]
    assert items_after_monkey_0 == items(turn(1, d11_s01, 0))

    items_after_monkey_1 = [[20, 23, 27, 26],
                            [],
                            [79, 60, 97],
                            [74, 500, 620]]
    assert items_after_monkey_1 == items(turn(1, turn(1, d11_s01, 0), 1))

    items_after_monkey_2 = [[20, 23, 27, 26],
                            [2080],
                            [],
                            [74, 500, 620, 1200, 3136]]
    assert items_after_monkey_2 == \
        items(turn(1, turn(1, turn(1, d11_s01, 0), 1), 2))

    items_after_monkey_3 = [[20, 23, 27, 26],
                            [2080, 25, 167, 207, 401, 1046],
                            [],
                            []]
    assert items_after_monkey_3 == \
        items(turn(1, turn(1, turn(1, turn(1, d11_s01, 0), 1), 2), 3))


def test_round_1():
    assert [[20, 23, 27, 26],
            [2080, 25, 167, 207, 401, 1046],
            [],
            []] == items(round_1(d11_s01))
    assert [[695, 10, 71, 135, 350],
            [43, 49, 58, 55, 362],
            [],
            []] == items(round_1(round_1(d11_s01)))
    assert [[16, 18, 21, 20, 122],
            [1468, 22, 150, 286, 739],
            [],
            []] == items(round_1(round_1(round_1(d11_s01))))
    assert [[83, 44, 8, 184, 9, 20, 26, 102],
            [110, 36],
            [],
            []] == items(nth(15, rounds_1(d11_s01)))
    assert [[10, 12, 14, 26, 34],
            [245, 93, 53, 199, 115],
            [],
            []] == items(nth(20, rounds_1(d11_s01)))


def test_counts():
    assert [2, 4, 3, 5] == counts(round_1(d11_s01))
    assert [101, 95, 7, 105] == counts(nth(20, rounds_1(d11_s01)))


def test_counts_part2():
    d11_s01_part2 = part2_augment(d11_s01)
    assert [2, 4, 3, 6] == counts(round_2(d11_s01_part2))
    assert [99, 97, 8, 103] == counts(nth(20, rounds_2(d11_s01_part2)))
    assert [5204, 4792, 199, 5192] == \
        counts(nth(1000, rounds_2(d11_s01_part2)))
    assert [52166, 47830, 1938, 52013] == \
        counts(nth(10000, rounds_2(d11_s01_part2)))


def test_part2_augment():
    assert [[{2: 1, 3: 1, 5: 4, 7: 2, 9: 7, 11: 2, 13: 1, 17: 11, 19: 3, 23: 10},
             {2: 0, 3: 2, 5: 3, 7: 0, 9: 8, 11: 10, 13: 7, 17: 13, 19: 3, 23: 6}],

            [{2: 0, 3: 0, 5: 4, 7: 5, 9: 0, 11: 10, 13: 2, 17: 3, 19: 16, 23: 8},
             {2: 1, 3: 2, 5: 0, 7: 2, 9: 2, 11: 10, 13: 0, 17: 14, 19: 8, 23: 19},
             {2: 1, 3: 0, 5: 0, 7: 5, 9: 3, 11: 9, 13: 10, 17: 7, 19: 18, 23: 6},
             {2: 0, 3: 2, 5: 4, 7: 4, 9: 2, 11: 8, 13: 9, 17: 6, 19: 17, 23: 5}],

            [{2: 1, 3: 1, 5: 4, 7: 2, 9: 7, 11: 2, 13: 1, 17: 11, 19: 3, 23: 10},
             {2: 0, 3: 0, 5: 0, 7: 4, 9: 6, 11: 5, 13: 8, 17: 9, 19: 3, 23: 14},
             {2: 1, 3: 1, 5: 2, 7: 6, 9: 7, 11: 9, 13: 6, 17: 12, 19: 2, 23: 5}],

            [{2: 0, 3: 2, 5: 4, 7: 4, 9: 2, 11: 8, 13: 9, 17: 6, 19: 17, 23: 5}]] == \
        items(part2_augment(d11_s01))


def test_monkey_business():
    assert 10605 == monkey_business(1, d11_s01, 20)
    assert 2713310158 == monkey_business(2, d11_s01, 10000)


d11_input = parse(standard_puzzle_input(year=2022, day=11))


def test_day11_part1_soln():
    assert 112221 == part1(d11_input)


def test_day11_part2_soln():
    assert 25272176808 == part2(d11_input)
