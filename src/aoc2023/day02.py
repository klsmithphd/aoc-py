""" Solution to https://adventofcode.com/2023/day/2 """
from functools import reduce
from operator import mul
from re import findall


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


def min_color(sets, color):
    """Returns the minimum number of cubes of a `color`, given the observed
    `sets`. The minimum number required is actually the maximum number of cubes
    of that color seen across any set."""
    return max(cubes.get(color, 0) for cubes in sets)


def fewest_cubes(game):
    """Returns a map of the cube colors and the minimum required number of 
    cubes of that color for a given game"""
    return dict(zip(COLORS,
                    (min_color(game['sets'], color) for color in COLORS)))


def power(cube):
    """The power of a set of cubes is equal to the numbers of red, green, 
    and blue cubes multiplied together."""
    return reduce(mul, cube.values())


def power_fewest_cubes(game):
    """Returns the power of the minimum set of cubes required in a game"""
    return power(fewest_cubes(game))


def power_fewest_cubes_sum(games):
    """Returns the sum of the powers of the minimum sets of cubes required
    across all games"""
    return sum(power_fewest_cubes(game) for game in games)


# Puzzle solutions
def part1(input):
    """"Determine which games would have been possible if the bag had been 
    loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
    What is the sum of the IDs of those games?"""
    return possible_game_id_sum(input)


def part2(input):
    """For each game, find the minimum set of cubes that must have been present. 
    What is the sum of the power of these sets?"""
    return power_fewest_cubes_sum(input)
