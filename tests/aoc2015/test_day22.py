import functools as ft
import aoc2015.day22 as d22
import utils.core as u


d22_s00_raw = [
    "Hit Points: 58",
    "Damage: 9"
]

d22_s00 = d22.GameState(boss_hit_points=58, boss_damage=9)


def test_parse():
    assert d22_s00 == d22.parse(d22_s00_raw)


def test_cast_spell():
    assert d22_s00._replace(player_mana=(500-53),
                            boss_hit_points=(58-4),
                            last_spell="magic_missile") == \
        d22.cast_spell(d22_s00, "magic_missile")

    assert d22_s00._replace(player_hit_points=(50+2),
                            player_mana=(500-73),
                            boss_hit_points=(58-2),
                            last_spell="drain") == \
        d22.cast_spell(d22_s00, "drain")

    assert d22_s00._replace(player_mana=(500-113),
                            effects={"shield": 6},
                            last_spell="shield") == \
        d22.cast_spell(d22_s00, "shield")

    assert d22_s00._replace(player_mana=(500-173),
                            effects={"poison": 6},
                            last_spell="poison") == \
        d22.cast_spell(d22_s00, "poison")

    assert d22_s00._replace(player_mana=(500-229),
                            effects={"recharge": 5},
                            last_spell="recharge") == \
        d22.cast_spell(d22_s00, "recharge")


def test_apply_effects():
    d22_s00_w_effects = d22_s00._replace(effects={"shield": 6,
                                                  "poison": 3,
                                                  "recharge": 1})
    assert d22_s00._replace(player_mana=(500+101),
                            player_armor=7,
                            boss_hit_points=(58-3),
                            effects={"shield": 5,
                                     "poison": 2}) == \
        d22.apply_effects(d22_s00_w_effects)


def test_short_sample_battle():
    d22_s01 = d22.GameState(player_hit_points=10,
                            player_mana=250,
                            boss_hit_points=13,
                            boss_damage=8)
    d22_s01_moves = ["poison", "magic_missile"]

    assert d22.GameState(player_hit_points=2,
                         player_mana=24,
                         player_armor=0,
                         boss_hit_points=0,
                         boss_damage=8,
                         effects={"poison": 3},
                         last_spell="magic_missile") == \
        ft.reduce(d22.combat_round, d22_s01_moves, d22_s01)


def test_longer_sample_battle():
    d22_s02 = d22.GameState(player_hit_points=10,
                            player_mana=250,
                            boss_hit_points=14,
                            boss_damage=8)
    d22_s02_moves = ["recharge", "shield", "drain", "poison", "magic_missile"]

    assert d22.GameState(player_hit_points=1,
                         player_mana=114,
                         player_armor=0,
                         boss_hit_points=-1,
                         boss_damage=8,
                         effects={"poison": 3},
                         last_spell="magic_missile") == \
        ft.reduce(d22.combat_round, d22_s02_moves, d22_s02)


def test_winning_spells():
    assert ['poison', 'recharge', 'magic_missile', 'poison',
            'recharge', 'shield', 'poison', 'drain', 'magic_missile'] == \
        d22.winning_spells(d22_s00)

    assert ['poison', 'recharge', 'shield', 'poison', 'recharge',
            'shield', 'poison', 'magic_missile', 'magic_missile'] == \
        d22.winning_spells(d22_s00, hard_mode=True)


day22_input = d22.parse(u.standard_puzzle_input(year=2015, day=22))


def test_part1():
    assert 1269 == d22.part1(day22_input)


def test_part2():
    assert 1309 == d22.part2(day22_input)
