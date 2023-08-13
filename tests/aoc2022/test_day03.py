from aoc2022.day03 import split_in_half, overlap, priority, \
    overlap_priority_sum, day03_soln
from utils.core import standard_puzzle_input
from pipe import map

d03_sample = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()


def test_split_in_half():
    assert ["vJrwpWtwJgWr", "hcsFMMfFFhFp"] == \
        list(split_in_half(d03_sample[0]))


def test_overlap():
    assert "p" == overlap(["vJrwpWtwJgWr", "hcsFMMfFFhFp"])


def test_overlaps():
    assert ["p", "L", "P", "v", "t", "s"] == \
        list(d03_sample | map(split_in_half) | map(overlap))


def test_priority():
    assert 1 == priority("a")
    assert 26 == priority("z")
    assert 27 == priority("A")
    assert 52 == priority("Z")


def test_overlap_priority_sum():
    assert 157 == overlap_priority_sum(d03_sample)


d03_input = standard_puzzle_input(year=2022, day=3)


def test_day03_part1_soln():
    assert 7597 == day03_soln.part1(d03_input)


# def test_day03_part2_soln():
#     assert 1 == day03_soln.part2(d03_input)
