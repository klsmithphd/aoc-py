import aoc2015.day21 as d21
import utils.core as u
import utils.vectors as v

d21_s00_raw = [
    "Hit Points: 104",
    "Damage: 8",
    "Armor: 1"
]

d21_s00 = d21.Stats(hit_points=104, damage=8, armor=1)


def test_parse():
    assert d21_s00 == d21.parse(d21_s00_raw)


def test_all_item_combos():
    # Weapon choices = 5
    # Armor choices = 6 (1 option for no armor plus 5 choices)
    # Rings choices = 22:
    #   1 option for no ring plus
    #   6 options for one ring plus
    #   15 options (combinations of six rings take 2)
    # 660 = 5 * 6 * 22
    assert 660 == len(list(d21.all_item_combos()))


def test_player_stats():
    combo = [d21.WEAPONS["Dagger"],
             d21.ARMOR["Platemail"],
             d21.RINGS["Damage +3"]]
    assert d21.Stats(hit_points=100, damage=7, armor=5, cost=210) == \
        d21.player_stats(combo)


def test_iswinning():
    player = d21.Stats(hit_points=8, damage=5, armor=5)
    boss = d21.Stats(hit_points=12, damage=7, armor=2)
    assert True == d21.iswinning(boss, player)


day21_input = d21.parse(u.standard_puzzle_input(year=2015, day=21))


def test_part1():
    assert 78 == d21.part1(day21_input)


def test_part2():
    assert 148 == d21.part2(day21_input)
