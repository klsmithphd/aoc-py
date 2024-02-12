"""Solution to https://adventofcode.com/2015/day/21"""
import collections as c
import frozendict
import functools as ft
import utils.graph as graph


# Constants
SPELL_COST = {
    "magic_missile": 53,
    "drain": 73,
    "shield": 113,
    "poison": 173,
    "recharge": 229
}

GameState = c.namedtuple(
    "GameState",
    ["player_hit_points",
     "player_mana",
     "player_armor",
     "boss_hit_points",
     "boss_damage",
     "effects",
     "last_spell"],
    defaults=[50, 500, 0, 0, 0, frozendict.frozendict(), None]
)

# Spell = c.namedtuple("Spell", ["cost", "cast"])


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
    return state._replace(
        effects=frozendict.frozendict(state.effects | {effect: timer}),
        last_spell=effect,
        player_mana=state.player_mana-cost)


def update_effect_timer(state: GameState, effect):
    effects = state.effects
    timer = effects[effect]
    if timer == 1:
        return state._replace(
            effects=frozendict.frozendict({k: v for k, v in effects.items()
                                           if k != effect}))
    else:
        return state._replace(
            effects=frozendict.frozendict(effects | {effect: timer-1}))


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


def player_round(state: GameState, spell: str, hard_mode):
    new_state = update_state(
        state, {"player_hit_points": -1}) if hard_mode else state

    if (new_state.player_hit_points > 0):
        return cast_spell(apply_effects(new_state), spell)
    else:
        return new_state


def boss_attack(state: GameState):
    attack = max(1, (state.boss_damage - state.player_armor))
    return update_state(state, {"player_hit_points": -attack})


def boss_round(state: GameState):
    new_state = apply_effects(state)
    if (new_state.boss_hit_points > 0):
        return boss_attack(new_state)
    else:
        return new_state


def combat_round(state: GameState, spell: str, hard_mode=False):
    return boss_round(player_round(state, spell, hard_mode))


def iswinning(state: GameState):
    return state.boss_hit_points <= 0 and state.player_hit_points > 0


def available_spells(state: GameState):
    active_effects = set(k for k, v in state.effects.items() if v > 1)
    return (spell for spell in SPELL_COST.keys()
            if spell not in active_effects and
            SPELL_COST[spell] <= state.player_mana)


class GameGraph(graph.Graph):
    def __init__(self, hard_mode):
        self.__mode = hard_mode

    def edges(self, state: GameState):
        return (combat_round(state, spell, self.__mode)
                for spell in available_spells(state))

    def distance(self, _, state: GameState):
        return SPELL_COST[state.last_spell]


def winning_spells(state: GameState, hard_mode=False):
    states = graph.dijkstra(GameGraph(hard_mode), state, iswinning)
    return [state.last_spell for state in states][1:]


# Puzzle solutions
def part1(input: GameState):
    return sum(SPELL_COST[spell] for spell in winning_spells(input))


def part2(input: GameState):
    return sum(SPELL_COST[spell]
               for spell in winning_spells(input, hard_mode=True))
