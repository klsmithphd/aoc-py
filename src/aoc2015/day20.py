"""Solution to https://adventofcode.com/2015/day/20"""
import toolz

# Constants
HOUSE_LIMIT = 800000
ELF_LIMIT = 50


# Input parsing
def parse(input):
    return int(toolz.first(input))


# Puzzle logic
def presents(house_limit: int, elf_limit=0):
    """Returns a list of the number of presents delivered to each house from
    1 up to `house_limit`. If `elf-limit` is greater than zero, elves will
    stop after delivering `elf-limit` presents"""

    # We switch to an imperative versus functional approach here for the sake
    # of speed.
    pres = [0]*house_limit
    for elf in range(1, house_limit+1):
        for house in range(elf, house_limit+1, elf):
            if elf_limit > 0 and house // elf > elf_limit:
                continue
            pres[house-1] += elf
    return pres


def house_with_n_presents(n, house_limit, elf_limit=0):
    """The first house that receives at least `n` presents."""
    return toolz.first(i for i, p in enumerate(presents(house_limit, elf_limit))
                       if p >= n) + 1


# Puzzle solutions
def part1(input):
    """First house that receives at least input number of presents"""
    return house_with_n_presents(input // 10, HOUSE_LIMIT)


def part2(input):
    """First house that receives at least input number of presents, 
    using part2 distribution logic"""
    return house_with_n_presents(input // 11, HOUSE_LIMIT, ELF_LIMIT)
