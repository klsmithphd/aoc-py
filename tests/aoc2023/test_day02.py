from aoc2023.day02 import parse, part1, part2, possible_game, \
    possible_game_id_sum
from utils.core import standard_puzzle_input

d02_s01_raw = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()

d02_s01 = [{'id': 1, 'sets': [{'blue': 3, 'red': 4},
                              {'red': 1, 'green': 2, 'blue': 6},
                              {'green': 2}]},
           {'id': 2, 'sets': [{'blue': 1, 'green': 2},
                              {'green': 3, 'blue': 4, 'red': 1},
                              {'green': 1, 'blue': 1}]},
           {'id': 3, 'sets': [{'green': 8, 'blue': 6, 'red': 20},
                              {'blue': 5, 'red': 4, 'green': 13},
                              {'green': 5, 'red': 1}]},
           {'id': 4, 'sets': [{'green': 1, 'red': 3, 'blue': 6},
                              {'green': 3, 'red': 6},
                              {'green': 3, 'blue': 15, 'red': 14}]},
           {'id': 5, 'sets': [{'red': 6, 'blue': 1, 'green': 3},
                              {'blue': 2, 'red': 1, 'green': 2}]}]


def test_parse():
    assert d02_s01 == parse(d02_s01_raw)


def test_possible_game():
    assert True == possible_game(d02_s01[0])
    assert True == possible_game(d02_s01[1])
    assert False == possible_game(d02_s01[2])
    assert False == possible_game(d02_s01[3])
    assert True == possible_game(d02_s01[4])


def test_possible_game_id_sum():
    assert 8 == possible_game_id_sum(d02_s01)


d02_input = parse(standard_puzzle_input(year=2023, day=2))


def test_day01_part1_soln():
    assert 2162 == part1(d02_input)


# def test_day01_part2_soln():
#     assert 72513 == part2(d02_input)
