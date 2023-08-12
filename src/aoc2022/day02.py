""" Solution to https://adventofcode.com/2022/day/2"""

# from utils.core import split_at_blanklines, parse_puzzle_input
from pipe import map

# Input parsing


def parse(input):
    return [str.split(x) for x in input]

# Puzzle logic


def guide_p1move(code):
    """
    The first column is what your opponent is going to play: A for Rock, 
    B for Paper, and C for Scissors.
    """
    codes = {'A': 'rock',
             'B': 'paper',
             'C': 'scissors'}
    return codes[code]


def guide_p2move(code):
    """
    The second column, you reason, must be what you should play in response: 
    X for Rock, Y for Paper, and Z for Scissors.
    """
    codes = {'X': 'rock',
             'Y': 'paper',
             'Z': 'scissors'}
    return codes[code]


def outcomes(pair):
    p1, p2 = pair
    outcomes = {('rock', 'rock'): 'draw',
                ('rock', 'paper'): 'win',
                ('rock', 'scissors'): 'lose',
                ('paper', 'rock'): 'lose',
                ('paper', 'paper'): 'draw',
                ('paper', 'scissors'): 'win',
                ('scissors', 'rock'): 'win',
                ('scissors', 'paper'): 'lose',
                ('scissors', 'scissors'): 'draw'}
    return outcomes[(p1, p2)]


def shape_score(shape):
    """
    The score for a single round is the score for the shape you selected 
    (1 for Rock, 2 for Paper, and 3 for Scissors)
    """
    scores = {'rock':     1,
              'paper':    2,
              'scissors': 3}
    return scores[shape]


def outcome_score(outcome):
    """
    Score for the outcome of the round (0 if you lost, 3 if the round was a 
    draw, and 6 if you won).
    """
    scores = {'lose': 0,
              'draw': 3,
              'win':  6}
    return scores[outcome]


def interpret(round):
    l, r = round
    return [guide_p1move(l), guide_p2move(r)]


def round_score(pair):
    _, p2 = pair
    outcome = outcomes(pair)
    return outcome_score(outcome) + shape_score(p2)


def total_score(input):
    return sum(input | map(interpret) | map(round_score))


# Puzzle solutions


def day02_part1(input):
    return total_score(input)


# def day02_part2(input):
#     return 2
