""" Solution to https://adventofcode.com/2022/day/2"""
from pipe import map, filter

# Input parsing


def parse(input):
    return [str.split(x) for x in input]

# Puzzle logic


permutations = [['rock',     'rock',     'draw'],
                ['rock',     'paper',    'win'],
                ['rock',     'scissors', 'lose'],
                ['paper',    'rock',     'lose'],
                ['paper',    'paper',    'draw'],
                ['paper',    'scissors', 'win'],
                ['scissors', 'rock',     'win'],
                ['scissors', 'paper',    'lose'],
                ['scissors', 'scissors', 'draw']]

outcomes = {(p1, p2): outcome for p1, p2, outcome in permutations}

moves = {(p1, outcome): p2 for p1, p2, outcome in permutations}


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


def guide_p2outcome(code):
    """
    Anyway, the second column says how the round needs to end: 
    X means you need to lose, Y means you need to end the round in a draw, and 
    Z means you need to win.
    """
    codes = {'X': 'lose',
             'Y': 'draw',
             'Z': 'win'}
    return codes[code]


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


def interpret1(round):
    l, r = round
    return [guide_p1move(l), guide_p2move(r), None]


def interpret2(round):
    l, r = round
    return [guide_p1move(l), None, guide_p2outcome(r)]


def fill_in(round):
    p1, p2, o = round
    if o == None:
        return [p1, p2, outcomes[(p1, p2)]]
    else:
        return [p1, moves[(p1, o)], o]


def round_score(round):
    _, p2, o = round
    return outcome_score(o) + shape_score(p2)


def total_score(input, interpret):
    return sum(input | map(interpret) | map(fill_in) | map(round_score))


# Puzzle solutions


def day02_part1(input):
    """
    What would your total score be if everything goes exactly according to your 
    strategy guide?
    """
    return total_score(input, interpret1)


def day02_part2(input):
    """
    Following the Elf's instructions for the second column, what would your 
    total score be if everything goes exactly according to your strategy guide?
    """
    return total_score(input, interpret2)
