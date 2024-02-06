"""Solution to https://adventofcode.com/2015/day/18"""


def parse(input):
    return {(x, y)
            for y in range(len(input))
            for x in range(len(input[0]))
            if input[y][x] == '#'}
