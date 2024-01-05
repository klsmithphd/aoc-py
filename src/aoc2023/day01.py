""" Solution to https://adventofcode.com/2023/day/1 """
from re import compile, findall

# Constants
SPELLED = {
    'one':   1,
    'two':   2,
    'three': 3,
    'four':  4,
    'five':  5,
    'six':   6,
    'seven': 7,
    'eight': 8,
    'nine':  9
}

# "A zero-width with positive-lookahead pattern to find spelled out
# words or individual digits. The complexity of the zero-width
# positive-lookahead is necessary to handle cases like `eightwo`,
# which should match both `eight` and `two`"
#
# Evaluates to r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'
SPELLED_REGEX = compile(f"(?=(\\d|{'|'.join(SPELLED.keys())}))")


# Input parsing
def parse(input):
    return list(input)


# Puzzle logic
def asint(s: str):
    """Return the supplied string `s` as an int. If `s` is a single character,
    convert directly to an int. If longer, convert the spelled-out string
    to its numerical equivalent."""
    return SPELLED[s] if len(s) > 1 else int(s)


def digits(s: str, spelled=False):
    """Returns a list of all the digits found in the string `s`. If
    `spelled` is `True`, spelled-out digits are included."""
    if not spelled:
        return [asint(x) for x in findall(r'\d', s)]
    else:
        return [asint(x) for x in SPELLED_REGEX.findall(s)]


def calibration_value(s: str, spelled=False):
    """The calibration value can be found by combining the first digit and the
    last digit (in that order) to form a single two-digit number. If `spelled`
    is `True`, spelled-out digits are included.s"""
    digs = digits(s, spelled)
    return digs[0]*10 + digs[-1]


def calibration_value_sum(input, spelled=False):
    """Returns the sum of the calibration values for each line of the
    input. If `spelled` = True, spelled-out digits are included."""
    return sum(calibration_value(line, spelled) for line in input)


# Puzzle solutions
def part1(input):
    """Consider your entire calibration document. 
    What is the sum of all of the calibration values?"""
    return calibration_value_sum(input)


def part2(input):
    """It looks like some of the digits are actually spelled out with letters: 
    one, two, three, four, five, six, seven, eight, and nine also count 
    as valid "digits".

    What is the sum of all of the calibration values?"""
    return calibration_value_sum(input, spelled=True)
