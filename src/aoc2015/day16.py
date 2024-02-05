"""Solution to https://adventofcode.com/2015/day/16"""


# Constants
CRITERIA = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


# Input parsing
def parse_line(line: str):
    aunt, props = line.split(": ", 1)
    return (int(aunt[4:]),
            {k: int(v) for k, v in (prop.split(": ")
                                    for prop in props.split(", "))})


def parse(input):
    return {k: v for k, v in (parse_line(line) for line in input)}


# Puzzle logic
def exact_match(props):
    """Checks if the given aunt's properties exactly match thos of the criteria"""
    return props == {k: CRITERIA[k] for k in props}


def attr_compare(attr, val):
    """For four properties (cats, trees, pomerians, and goldfish), the value
    must be greater than or less than, not equal to the expected value. 
    For all others, we're looking for an exact match"""
    expected = CRITERIA[attr]
    match attr:
        case "cats": return val > expected
        case "trees": return val > expected
        case "pomerians": return val < expected
        case "goldfish": return val < expected
        case _: return val == expected


def range_match(props):
    """Use the logic of part 2 where some attributes need to be greater
    than or less than, not just equal, to determine whether an aunt
    matches the criteria"""
    return all(attr_compare(k, v) for k, v in props.items())


def matching_aunt(condition, aunts: dict):
    """Use the supplied condition filter to find the correct aunt"""
    return [k for k, v in aunts.items() if condition(v)][0]


# Puzzle solutions
def part1(input):
    """Find the aunt whose properties exactly match the search criteria"""
    return matching_aunt(exact_match, input)


def part2(input):
    """Find the aunt whose properties satisfied the range comparisons"""
    return matching_aunt(range_match, input)
