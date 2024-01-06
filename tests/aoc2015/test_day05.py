import aoc2015.day05 as d05
import utils.core as u

d05_s00 = "ugknbfddgicrmopn"
d05_s01 = "aaa"
d05_s02 = "jchzalrnumimnmhp"
d05_s03 = "haegwjzuvuyypxyu"
d05_s04 = "dvszwmarrgswjxmb"

d05_s05 = "qjhvhtzxzqqjkmpb"
d05_s06 = "xxyxx"
d05_s07 = "uurcxstgmygtbstg"
d05_s08 = "ieodomkazucvgmuy"


def test_part1_nice():
    assert True == d05.part1_nice(d05_s00)
    assert True == d05.part1_nice(d05_s01)
    # No repeated character
    assert False == d05.repeated_char(d05_s02)
    assert False == d05.part1_nice(d05_s02)
    # Has one of the banned pairs (xy)
    assert False == d05.no_invalid_pairs(d05_s03)
    assert False == d05.part1_nice(d05_s03)
    # Not enough vowels
    assert False == d05.three_vowels(d05_s04)
    assert False == d05.part1_nice(d05_s03)


def test_part2_nice():
    assert True == d05.part2_nice(d05_s05)
    assert True == d05.part2_nice(d05_s06)
    # Missing repeating character with intervening letter
    assert False == d05.repeat_with_letter_between(d05_s07)
    assert False == d05.part2_nice(d05_s07)
    # Missing repeated pair
    assert False == d05.non_overlapping_pair(d05_s08)
    assert False == d05.part2_nice(d05_s08)


day05_input = d05.parse(u.standard_puzzle_input(year=2015, day=5))


def test_part1():
    assert 255 == d05.part1(day05_input)


def test_part2():
    assert 55 == d05.part2(day05_input)
