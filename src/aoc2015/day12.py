"""Solution to https://adventofcode.com/2015/day/12"""
import json
import re
import toolz

# Input parsing
parse = toolz.first


# Puzzle logic
def all_numbers_total(s: str):
    """Total of all the numbers found in the JSON document string"""
    return sum(int(x) for x in re.findall(r"-?\d+", s))


def drop_red(obj):
    """Drops all objects that have 'red' as a value for any property"""
    if isinstance(obj, dict):
        if 'red' in obj.values():
            return dict()
        else:
            return {k: drop_red(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [drop_red(x) for x in obj]
    else:
        return obj


def json_without_red(s: str):
    """Parses the string as a JSON document, strips out the object with 
    red values, and the reencodes as a string"""
    return json.dumps(drop_red(json.loads(s)))


# Puzzle solutions
def part1(input):
    """Sum of all the values in the JSON document"""
    return all_numbers_total(input)


def part2(input):
    """Sum of all the values in the JSON document once objects with `red` values
    have been stripped"""
    return all_numbers_total(json_without_red(input))
