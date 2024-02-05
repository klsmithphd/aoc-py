"""Solution to https://adventofcode.com/2015/day/16"""
import itertools as it


# Constants
TARGET_QTY = 150


# Input parsing
def parse(input):
    return sorted((int(line) for line in input), reverse=True)


# Puzzle logic
def combinations(total, containers, used=[]):
    """Returns a collection of the different container combinations that sum
    to `total`. `containers` is assumed to be pre-sorted in decscending
    order. The values in `containers` need not be unique, but each 
    occurrence will treated independently."""
    # If we get down to zero for the target total, we've succeeded, so
    # return the containers we used to get to this point
    if (total == 0):
        return [used]
    elif (total < 0 or sum(containers) < total):
        # If the total is negative, we've gone too far.
        # If the rest of the containers can't add up to the total, we've
        # reached a dead end. In both cases, just stop
        return []
    else:
        # First, we filter to only the remaining containers that are less
        # than or equal to our target
        ctrs = [c for c in containers if c <= total]
        # Then, we explore the sub-problem of considering each remaining
        # container, subtracting its size from the total, and computing
        # the possible combinations of the new smaller target total with
        # the remaining containers
        sub_combos = (combinations(total - ctrs[i], ctrs[i+1:], used+[ctrs[i]])
                      for i in range(len(ctrs)))
        return list(it.chain(*sub_combos))


def combination_count(total, containers):
    """Counts the number of combinations of `containers` that sum to `total`"""
    return len(combinations(total, containers))


def min_container_combination_count(total, containers):
    """Counts the number of combinations of `containers` that sum to `total`
    using the minimum number of containers."""
    counts = [len(x) for x in combinations(total, containers)]
    min_count = min(counts)
    return sum(1 for x in counts if x == min_count)


# Puzzle solutions
def part1(input):
    """Counts the number of combinations of `containers` that sum to `total`"""
    return combination_count(TARGET_QTY, input)


def part2(input):
    """Counts the number of combinations of `containers` that sum to `total`
    using the minimum number of containers."""
    return min_container_combination_count(TARGET_QTY, input)
