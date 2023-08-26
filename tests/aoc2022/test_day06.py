from aoc2022.day06 import parse, part1, part2, chars_to_distinct_run
from utils.core import standard_puzzle_input

d06_s01 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
d06_s02 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
d06_s03 = "nppdvjthqldpwncqszvftbrmjlhg"
d06_s04 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
d06_s05 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

d06_s06 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
d06_s07 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
d06_s08 = "nppdvjthqldpwncqszvftbrmjlhg"
d06_s09 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
d06_s10 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

d06_input = parse(standard_puzzle_input(year=2022, day=6))


def test_chars_to_distinct_run():
    assert 7 == chars_to_distinct_run(4, d06_s01)
    assert 5 == chars_to_distinct_run(4, d06_s02)
    assert 6 == chars_to_distinct_run(4, d06_s03)
    assert 10 == chars_to_distinct_run(4, d06_s04)
    assert 11 == chars_to_distinct_run(4, d06_s05)

    assert 19 == chars_to_distinct_run(14, d06_s06)
    assert 23 == chars_to_distinct_run(14, d06_s07)
    assert 23 == chars_to_distinct_run(14, d06_s08)
    assert 29 == chars_to_distinct_run(14, d06_s09)
    assert 26 == chars_to_distinct_run(14, d06_s10)


def test_day06_part1_soln():
    assert 1855 == part1(d06_input)


def test_day06_part2_soln():
    assert 3256 == part2(d06_input)
