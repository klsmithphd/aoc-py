"""Solution to https://adventofcode.com/2015/day/21"""
import collections as c
import functools as ft


# Constants
GameState = c.namedtuple(
    "GameState",
    ["player_hit_points",
     "player_mana",
     "player_armor",
     "boss_hit_points",
     "boss_damage",
     "effects",
     "last_spell"],
    defaults=[50, 500, 0, 0, 0, dict(), None]
)

Spell = c.namedtuple("Spell", ["cost", "cast"])


# Input parsing
def parse_line(line: str):
    attr, qty = line.split(": ")
    return "boss_"+"_".join(attr.lower().split(" ")), int(qty)


def parse(input):
    return GameState(**{k: v for k, v in (parse_line(line) for line in input)})


# Puzzle logic
def set_state(state, kwargs):
    return state._replace(**kwargs)


def update_state(state: GameState, kwargs):
    return state._replace(**{k: getattr(state, k) + v
                             for k, v in kwargs.items()})


def start_effect(state, effect, timer, cost):
    return state._replace(effects=state.effects | {effect: timer},
                          last_spell=effect,
                          player_mana=state.player_mana-cost)


def update_effect_timer(state: GameState, effect):
    effects = state.effects
    timer = effects[effect]
    if timer == 1:
        return state._replace(effects={k: v for k, v in effects.items()
                                       if k != effect})
    else:
        return state._replace(effects=effects | {effect: timer-1})


def cast_magic_missile(state: GameState):
    new_state = set_state(state, {"last_spell": "magic_missile"})
    return update_state(new_state, {"player_mana": -53,
                                    "boss_hit_points": -4})


def cast_drain(state: GameState):
    new_state = set_state(state, {"last_spell": "drain"})
    return update_state(new_state, {"player_mana": -73,
                                    "boss_hit_points": -2,
                                    "player_hit_points": 2})


def cast_shield(state: GameState):
    return start_effect(state, "shield", 6, 113)


def cast_poison(state: GameState):
    return start_effect(state, "poison", 6, 173)


def cast_recharge(state: GameState):
    return start_effect(state, "recharge", 5, 229)


def shield_effect(state: GameState):
    shield_timer = state.effects['shield']
    match shield_timer:
        case 6: return state._replace(player_armor=7)
        case 1: return state._replace(player_armor=0)
        case _: return state


def poison_effect(state: GameState):
    return update_state(state, {"boss_hit_points": -3})


def recharge_effect(state: GameState):
    return update_state(state, {"player_mana": 101})


SPELLS = {
    "magic_missile": cast_magic_missile,
    "drain":         cast_drain,
    "shield":        cast_shield,
    "poison":        cast_poison,
    "recharge":      cast_recharge
}

EFFECTS = {
    "shield":   shield_effect,
    "poison":   poison_effect,
    "recharge": recharge_effect
}


def cast_spell(state: GameState, spell: str):
    return SPELLS[spell](state)


def apply_effect(state: GameState, effect: str):
    return update_effect_timer(EFFECTS[effect](state), effect)


def apply_effects(state: GameState):
    return ft.reduce(apply_effect, state.effects.keys(), state)

# Puzzle solutions
