from aoc2022.day03 import part1, part2, split_in_half, chunked_in_thirds, \
    overlap, priority, overlap_priority_sum
from utils.core import standard_puzzle_input
from pipe import map

d03_s01 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()

d03_input = standard_puzzle_input(year=2022, day=3)


def test_split_in_half():
    assert ["vJrwpWtwJgWr", "hcsFMMfFFhFp"] == \
        list(split_in_half(d03_s01[0]))


def test_chunked_in_thirds():
    assert [d03_s01[:3], d03_s01[3:]] == \
        list(chunked_in_thirds(d03_s01))


def test_overlap():
    assert "p" == overlap(["vJrwpWtwJgWr", "hcsFMMfFFhFp"])
    assert "r" == overlap(["vJrwpWtwJgWrhcsFMMfFFhFp",
                           "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                           "PmmdzqPrVvPwwTWBwg"])


def test_overlaps():
    assert ["p", "L", "P", "v", "t", "s"] == \
        list(d03_s01 | map(split_in_half) | map(overlap))
    assert ["r", "Z"] == \
        list(chunked_in_thirds(d03_s01) | map(overlap))


def test_priority():
    assert 1 == priority("a")
    assert 26 == priority("z")
    assert 27 == priority("A")
    assert 52 == priority("Z")


def test_overlap_priority_sum():
    assert 157 == overlap_priority_sum(d03_s01, part1=True)
    assert 70 == overlap_priority_sum(d03_s01, part1=False)


def test_day03_part1_soln():
    assert 7597 == part1(d03_input)


def test_day03_part2_soln():
    assert 2607 == part2(d03_input)
