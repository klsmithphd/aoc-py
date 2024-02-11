"""Solution to https://adventofcode.com/2015/day/21"""
import collections as c


# Constants
Stats = c.namedtuple("Stats",
                     ["hit_points", "damage", "armor", "cost"],
                     defaults=[0]*4)

PLAYER = Stats(hit_points=100)

WEAPONS = {
    "Dagger":     Stats(cost=8,  damage=4, armor=4),
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


# Puzzle solutions
