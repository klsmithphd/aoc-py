""" Solution to https://adventofcode.com/2023/day/2 """
from re import findall
from utils.core import AoCSolution


# Constants
PART1_TARGET = {'red': 12, 'green': 13, 'blue': 14}
COLORS = PART1_TARGET.keys()

# Input parsing


def parse_id(game_str):
    return int(findall(r'\d+', game_str)[0])


def parse_cube(cube_str: str):
    qty, color = cube_str.split(' ')
    return (color, int(qty))


def parse_cubes(cubes_str: str):
    return dict(parse_cube(cube_str) for cube_str in cubes_str.split(', '))


def parse_sets(sets_str: str):
    return [parse_cubes(cubest_str) for cubest_str in sets_str.split('; ')]


def parse_game(line: str):
    game_str, sets_str = line.split(': ')
    return {'id': parse_id(game_str), 'sets': parse_sets(sets_str)}


def parse(input):
    return [parse_game(line) for line in input]


# Puzzle logic
def set_compare(cubes):
    """"Given a target map of maximum cubes of any given color, return a 
    boolean indicating whether the set value is less than or equal to the 
    target"""
    k, v = cubes
    return v <= PART1_TARGET[k]


def possible_set(s):
    """Returns a boolean if the set is possible. A set is possible if the 
    number of cubes of a given color are less than or equal to the target 
    numbers for that color"""
    return all(set_compare(cubes) for cubes in s.items())


def possible_game(game):
    """Returns a boolean indicating whether the game is possible.
    A game is possible if every set in the game is possible."""
    return all(possible_set(s) for s in game['sets'])


def possible_game_id_sum(games):
    """Returns the sum of the ids of the games deemed possible"""
    return sum(game['id'] for game in filter(possible_game, games))


# Puzzle solutions
def part1(input):
    """"Determine which games would have been possible if the bag had been 
    loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
    What is the sum of the IDs of those games?"""
    return possible_game_id_sum(input)


def part2(input):
    """"""
    pass


day02_soln = AoCSolution(parse, part1, part2)
