"""Solution to https://adventofcode.com/2015/day/21"""
import collections as c
import functools as ft
from frozendict import frozendict
from utils.graph import Graph, dijkstra


# Constants
SPELL_COST = {
    "magic_missile": 53,
    "drain": 73,
    "shield": 113,
    "poison": 173,
    "recharge": 229
}

SPELL_PROPS = {
    "magic_missile": {
        "cost": 53,
        "changes": {"boss_hit_points": -4}
    },
    "drain": {
        "cost": 73,
        "changes": {"boss_hit_points": -2,
                    "player_hit_points": 2}
    },
    "shield": {
        "cost": 113,
        "duration": 6,
        "changes": {"player_armor": 7}
    },
    "poison": {
        "cost": 173,
        "duration": 6,
        "changes": {"boss_hit_points": -3}
    },
    "recharge": {
        "cost": 229,
        "duration": 5,
        "changes": {"player_mana": 101}
    }
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
    defaults=[50, 500, 0, 0, 0, frozendict(), None]
)


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


def start_effect(state, effect, timer):
    return state._replace(effects=frozendict(state.effects | {effect: timer}))


def update_effect_timer(state: GameState, effect):
    effects = state.effects
    timer = effects[effect]
    if timer == 1:
        return state._replace(
            effects=frozendict({k: v for k, v in effects.items()
                                if k != effect}))
    else:
        return state._replace(
            effects=frozendict(effects | {effect: timer-1}))


def cast_helper(state: GameState, spell: str):
    if "duration" in SPELL_PROPS["drain"].keys():
        return start_effect(state, spell, SPELL_PROPS[spell]["duration"])
    else:
        return update_state(state, SPELL_PROPS[spell]["changes"])


def cast_magic_missile(state: GameState):
    return cast_helper(state, "magic_missile")


def cast_drain(state: GameState):
    return cast_helper(state, "drain")


def effect_helper(state: GameState, spell: str):
    return start_effect(state, spell, SPELL_PROPS[spell]["duration"])


def cast_shield(state: GameState):
    return effect_helper(state, "shield")


def cast_poison(state: GameState):
    return effect_helper(state, "poison")


def cast_recharge(state: GameState):
    return effect_helper(state, "recharge")


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
    """Update the game state according to the spell being cast."""
    new_state = update_state(
        state, {"player_mana": -SPELL_PROPS[spell]["cost"]})
    return set_state(SPELLS[spell](new_state), {"last_spell": spell})


def apply_effect(state: GameState, effect: str):
    """For a given effect, update the state and decrement the
    effect's timer."""
    return update_effect_timer(EFFECTS[effect](state), effect)


def apply_effects(state: GameState):
    """For all currently active effects, update the state."""
    return ft.reduce(apply_effect, state.effects.keys(), state)


def player_round(state: GameState, spell: str, hard_mode):
    """In the player's round, effects will happen first and then
    the player will cast a spell.

    If `hard_mode` is set, the player will lose one hit point
    before anything else happens."""
    new_state = update_state(
        state, {"player_hit_points": -1}) if hard_mode else state

    if (new_state.player_hit_points > 0):
        return cast_spell(apply_effects(new_state), spell)
    else:
        return new_state


def boss_attack(state: GameState):
    """The boss's attack will reduce the player's hit points by the 
    boss's damage value, less any armor buff the player has."""
    attack = max(1, (state.boss_damage - state.player_armor))
    return update_state(state, {"player_hit_points": -attack})


def boss_round(state: GameState):
    """In the boss' round, effects will happen first and then the
    boss, if still alive, will attack the player."""
    new_state = apply_effects(state)
    if (new_state.boss_hit_points > 0):
        return boss_attack(new_state)
    else:
        return new_state


def combat_round(state: GameState, spell: str, hard_mode=False):
    """A combat round consists of the player going first by casting
    the given spell, and then the boss taking their turn. 

    If `hard_mode` is `True`, the player automatically loses one
    hit point at the beginning of their round before anything else."""
    return boss_round(player_round(state, spell, hard_mode))


def iswinning(state: GameState):
    """Whether the game is in a winning state."""
    return state.boss_hit_points <= 0 and state.player_hit_points > 0


def available_spells(state: GameState):
    """The collection of spells that the player can cast given the
    current game state."""
    active_effects = set(k for k, v in state.effects.items() if v > 1)
    return (spell for spell in SPELL_COST.keys()
            if spell not in active_effects and
            SPELL_COST[spell] <= state.player_mana)


class GameGraph(Graph):
    """Limited implementation of the `Graph` protocol, where each
    vertex in the graph is a game state, and transitions between game
    states serve as our edges. The distance in our graph is the amount
    of mana spent by the player to cast a spell."""

    def __init__(self, hard_mode):
        self.__mode = hard_mode

    def edges(self, state: GameState):
        return (combat_round(state, spell, self.__mode)
                for spell in available_spells(state))

    def distance(self, _, state: GameState):
        return SPELL_COST[state.last_spell]


def winning_spells(start: GameState, hard_mode=False):
    """A sequence of spells that allows the player to win with the
    least amount of mana spent."""
    states = dijkstra(GameGraph(hard_mode), start, iswinning)
    return [state.last_spell for state in states][1:]


# Puzzle solutions
def part1(input: GameState):
    """Least amount of mana to spend to win the game"""
    return sum(SPELL_COST[spell] for spell in winning_spells(input))


def part2(input: GameState):
    """Least amount of mana to spend to win the game in hard mode"""
    return sum(SPELL_COST[spell]
               for spell in winning_spells(input, hard_mode=True))
