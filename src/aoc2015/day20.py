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
    pres = [1]*house_limit
    for elf in range(2, house_limit+1):
        for house in range(elf, house_limit+1, elf):
            if elf_limit > 0 and house // elf > elf_limit:
                continue
            pres[house-1] += elf
    return pres


def house_with_n_presents(n, house_limit, elf_limit=0):
    return [i for i, p in enumerate(presents(house_limit, elf_limit))
            if p >= n][0] + 1


# Puzzle solutions
def part1(input):
    return house_with_n_presents(input // 10, HOUSE_LIMIT)


def part2(input):
    return house_with_n_presents(input // 11, HOUSE_LIMIT, ELF_LIMIT)
