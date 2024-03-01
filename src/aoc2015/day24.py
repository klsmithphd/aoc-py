"""Solution to https://adventofcode.com/2015/day/24"""
import itertools as it
import functools as ft
import operator as op


# Input parsing
def parse(input):
    return [int(x) for x in input]


# Puzzle logic
def smallest_passenger_packages(n: int, weights):
    """Returns the valid combination of package `weights` in the passenger 
    compartment that will balance the weight across all `n` compartments but 
    results in the smallest number of packages in the passenger compartment."""

    # We don't need to actually work out the distribution of packages across
    # the other compartments --- every compartment needs an equal weight, so
    # we just take the total weight, divide by the number of compartments,
    # and return the combination of items for the first (passenger) compartment
    # that add up to that target weight, returning whatever combinations
    # use the smallest number of items
    target = sum(weights) / n
    size = 1
    partitions = []
    while not partitions:
        partitions = [p for p in it.combinations(weights, size)
                      if sum(p) == target]
        size += 1
    return partitions


def product(coll):
    return ft.reduce(op.mul, coll)


def best_quantum_entanglement(partitions):
    """Finds the best (minimum) quantum entanglement, which is just the product
    of the packages' weights"""
    return min(product(p) for p in partitions)


def ideal_quantum_entanglement(n: int, weights):
    """Returns the ideal quantum entanglement value for the packages divided
    into `n` compartments"""
    return best_quantum_entanglement(smallest_passenger_packages(n, weights))


# Puzzle solutions
def part1(input):
    """Quantum entanglement of the packages in the passenger compartment for
    packages divided among 3 compartments"""
    return ideal_quantum_entanglement(3, input)


def part2(input):
    """Quantum entanglement of the packages in the passenger compartment for
    packages divided among 4 compartments"""
    return ideal_quantum_entanglement(4, input)
