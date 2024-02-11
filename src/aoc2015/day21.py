"""Solution to https://adventofcode.com/2015/day/21"""
import collections as c
import itertools as it
import math
import utils.vectors as v


# Constants
Stats = c.namedtuple("Stats",
                     ["hit_points", "damage", "armor", "cost"],
                     defaults=[0]*4)

PLAYER = Stats(hit_points=100)

WEAPONS = {
    "Dagger":     Stats(cost=8,  damage=4, armor=0),
    "Shortsword": Stats(cost=10, damage=5, armor=0),
    "Warhammer":  Stats(cost=25, damage=6, armor=0),
    "Longsword":  Stats(cost=40, damage=7, armor=0),
    "Greataxe":   Stats(cost=74, damage=8, armor=0)
}

ARMOR = {
    "Leather":    Stats(cost=13,  damage=0, armor=1),
    "Chainmail":  Stats(cost=31,  damage=0, armor=2),
    "Splintmail": Stats(cost=53,  damage=0, armor=3),
    "Bandedmail": Stats(cost=75,  damage=0, armor=4),
    "Platemail":  Stats(cost=102, damage=0, armor=5)
}

RINGS = {
    "Damage +1":  Stats(cost=25,  damage=1, armor=0),
    "Damage +2":  Stats(cost=50,  damage=2, armor=0),
    "Damage +3":  Stats(cost=100, damage=3, armor=0),
    "Defense +1": Stats(cost=20,  damage=0, armor=1),
    "Defense +2": Stats(cost=40,  damage=0, armor=2),
    "Defense +3": Stats(cost=80,  damage=0, armor=3)
}


# Input parsing
def parse_line(line: str):
    attr, qty = line.split(": ")
    return "_".join(attr.lower().split(" ")), int(qty)


def parse(input):
    return Stats(**{k: v for k, v in (parse_line(line) for line in input)})


# Puzzle logic
def all_item_combos():
    """Returns a collection of all possible weapon/armor/ring combos."""
    # There must be exactly one weapon
    weapons = WEAPONS.values()
    # There can be 0 or 1 armor, with five choices.
    armor = it.chain([Stats()], ARMOR.values())
    # There can be 0 to 2 rings
    rings = it.chain([[Stats()]],
                     [[ring] for ring in RINGS.values()],
                     it.combinations(RINGS.values(), 2))
    return ((w, a, *r) for w, a, r, in it.product(weapons, armor, rings))


def player_stats(combo):
    """Given a combination of items, determine the player's starting stats"""
    return Stats(*v.vec_sum(it.chain([PLAYER], combo)))


def all_players():
    """A collection of all possible player stats"""
    return (player_stats(combo) for combo in all_item_combos())


def iswinning(b, p):
    """Boolean function indicating whether the player will win"""
    b_rounds = math.ceil(b.hit_points / max(1, (p.damage - b.armor)))
    p_rounds = math.ceil(p.hit_points / max(1, (b.damage - p.armor)))
    return p_rounds >= b_rounds


def cheapest_winning_combo(boss):
    """Of all the item combos a player could have, return the winning scenario
    with the cheapest cost"""
    return min(p.cost for p in all_players() if iswinning(boss, p))


def priciest_losing_combo(boss):
    """Of all the item combos a player could have, return the losing scenario
    that costs the most"""
    return max(p.cost for p in all_players() if not iswinning(boss, p))


# Puzzle solutions
def part1(input):
    """Least amount of gold to spend and still win the fights"""
    return cheapest_winning_combo(input)


def part2(input):
    """Most amount of gold to spend and still lose the fight"""
    return priciest_losing_combo(input)
