"""Solution to https://adventofcode.com/2022/day/10"""
from itertools import accumulate, islice, repeat
from more_itertools import chunked, flatten
from operator import add, mul

# Input parsing


def parse_line(line):
    if line == "noop":
        return "noop"
    else:
        _, value = line.split()
        return int(value)


def parse(input):
    return [parse_line(line) for line in input]

# Puzzle logic


def addends(op):
    """
    Returns a list that determines by how much the `X` register should change
    over the next one or two cycles

    addx V takes two cycles to complete. After two cycles, the X register is 
    increased by the value V. (V can be negative.)

    noop takes one cycle to complete. It has no other effect.
    """
    return [0] if op == "noop" else [0, op]


def changes(cmds):
    """
    Returns a sequence of the changes in the `X` register after each cycle
    """
    return flatten(addends(cmd) for cmd in cmds)


def register_values(input):
    """
    Return a sequence of the value of the `X` register at the end of each cycle
    """
    return accumulate(changes(input), add, initial=1)


def signal_samples(input):
    """
    Returns the value of the X register **during** the 20th cycle
    and every 40 cycles after that
    """
    return islice(register_values(input), 19, None, 40)


def signal_strength_sum(input):
    """
    The signal strength is the cycle number multipled by the value of the
    X register during that cycle
    """
    return sum(map(mul, signal_samples(input), [20, 60, 100, 140, 180, 220]))


def light(pixel, register):
    """
    Determine whether to light up the screen at the `pixel` location,
    given the value of the X `register`
    """
    return "#" if (abs(register - pixel) <= 1) else " "


def screen(input):
    """
    Return a string representation of the CRT screen based on the programmed
    instructions
    """
    lights = map(light, flatten(repeat(range(40), 6)), register_values(input))
    return '\n'.join(map(''.join, chunked(lights, 40)))


# Puzzle solutions


def part1(input):
    """
    Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 
    220th cycles. What is the sum of these six signal strengths?
    """
    return signal_strength_sum(input)


def part2(input):
    """
    Render the image given by your program. What eight capital letters 
    appear on your CRT?
    """
    return screen(input)
