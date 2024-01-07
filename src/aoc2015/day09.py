"""Solution to https://adventofcode.com/2015/day/9"""
import itertools as it
import toolz


# Input parsing
def parse_line(line: str):
    a, _, b, _, c = line.split()
    return [(a, b, int(c)), (b, a, int(c))]


def parse(input):
    dists = sorted(it.chain.from_iterable(parse_line(line) for line in input))
    return {k: {b: c for _, b, c in g} for k, g in it.groupby(dists, toolz.first)}


# Puzzle logic
def route_distance(dists, route):
    """Computes the distance along a route denoted as a sequence of nodes"""
    return sum(dists[a][b] for a, b in it.pairwise(route))


def all_route_distances(dists):
    """Computes all possible route distances"""
    nodes = dists.keys()
    return (route_distance(dists, route) for route in it.permutations(nodes))


def shortest_route_distance(dists):
    """Returns the shortest possible route distance"""
    return min(all_route_distances(dists))


def longest_route_distance(dists):
    """Returns the longest possible route distance"""
    return max(all_route_distances(dists))


# Puzzle solutions
def part1(input):
    """Distance of shortest route visiting every location once"""
    return shortest_route_distance(input)


def part2(input):
    """Distance of longest route visiting every location once"""
    return longest_route_distance(input)
