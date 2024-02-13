"""Solution to https://adventofcode.com/2015/day/21"""
import collections as c
import functools as ft
import utils.core as u
from frozendict import frozendict
from utils.graph import Graph, dijkstra


# Constants
SPELLS = {
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
        "on_start": {"player_armor": 7},
        "on_turn": {},
        "on_end": {"player_armor": -7}
    },
    "poison": {
        "cost": 173,
        "duration": 6,
        "on_start": {},
        "on_turn": {"boss_hit_points": -3},
        "on_end": {}
    },
    "recharge": {
        "cost": 229,
        "duration": 5,
        "on_start": {},
        "on_turn": {"player_mana": 101},
        "on_end": {}
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
def state_update(state: GameState, spell: str, key: str):
    """Update the state according to the expected changes recorded
    for the given spell/effect under `key` in the SPELLS constant"""
    return u.nt_update(state,
                       {k: u.add(v) for k, v in SPELLS[spell][key].items()})


def state_key_update(state: GameState, key: str, val: int):
    """Update the state's key by adding `val` to the current value"""
    return u.nt_update(state, {key: u.add(val)})


def set_effect_timer(state: GameState, effect: str, timer: int):
    """Set the effect's timer to the provided value"""
    return state._replace(effects=frozendict(state.effects | {effect: timer}))


def set_effects(state: GameState, new_effects: dict):
    """Replace the state's effects value with the provided dict"""
    return state._replace(effects=frozendict(new_effects))


def iseffect(spell: str):
    """Boolean function that returns true if the spell is an effect"""
    return "duration" in SPELLS[spell].keys()


def cast_spell(state: GameState, spell: str):
    """Update the game state according to the spell being cast, 
    including decrementing the player's mana by the cost of the spell
    and recording the spell cast in the `last_spell` variable."""
    if iseffect(spell):
        s1 = set_effect_timer(state, spell, SPELLS[spell]["duration"])
    else:
        s1 = state_update(state, spell, "changes")
    s2 = state_key_update(s1, "player_mana", -SPELLS[spell]["cost"])
    return u.nt_set(s2, {"last_spell": spell})


def apply_effect(state: GameState, effect: str):
    """For a given effect, update the state and decrement the
    effect's timer."""
    effects = state.effects
    timer = effects[effect]
    state = state_update(state, effect, "on_turn")
    if timer == SPELLS[effect]["duration"]:
        state = state_update(state, effect, "on_start")
    if timer > 1:
        return set_effect_timer(state, effect, timer-1)
    else:
        return set_effects(state_update(state, effect, "on_end"),
                           u.without_keys(effects, [effect]))


def apply_effects(state: GameState):
    """For all currently active effects, update the state."""
    return ft.reduce(apply_effect, state.effects.keys(), state)


def player_round(state: GameState, spell: str, hard_mode):
    """In the player's round, effects will happen first and then
    the player will cast a spell.

    If `hard_mode` is set, the player will lose one hit point
    before anything else happens."""
    new_state = state_key_update(state, "player_hit_points", -1) \
        if hard_mode else state

    if (new_state.player_hit_points > 0):
        return cast_spell(apply_effects(new_state), spell)
    else:
        return new_state


def boss_attack(state: GameState):
    """The boss's attack will reduce the player's hit points by the 
    boss's damage value, less any armor buff the player has."""
    attack = max(1, (state.boss_damage - state.player_armor))
    return state_key_update(state, "player_hit_points", -attack)


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
    return (spell for spell in SPELLS.keys()
            if spell not in active_effects and
            SPELLS[spell]["cost"] <= state.player_mana)


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
        return SPELLS[state.last_spell]["cost"]


def winning_spells(start: GameState, hard_mode=False):
    """A sequence of spells that allows the player to win with the
    least amount of mana spent."""
    states = dijkstra(GameGraph(hard_mode), start, iswinning)
    return [state.last_spell for state in states][1:]


# Puzzle solutions
def part1(input: GameState):
    """Least amount of mana to spend to win the game"""
    return sum(SPELLS[spell]["cost"] for spell in winning_spells(input))


def part2(input: GameState):
    """Least amount of mana to spend to win the game in hard mode"""
    return sum(SPELLS[spell]["cost"]
               for spell in winning_spells(input, hard_mode=True))
