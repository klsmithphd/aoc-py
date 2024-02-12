import aoc2015.day22 as d22


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
