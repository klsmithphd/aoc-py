import aoc2015.day10 as d10
import utils.core as u


def test_look_and_say():
    assert "11" == d10.look_and_say("1")
    assert "21" == d10.look_and_say("11")
    assert "1211" == d10.look_and_say("21")
    assert "111221" == d10.look_and_say("1211")
    assert "312211" == d10.look_and_say("111221")


day10_input = d10.parse(u.standard_puzzle_input(year=2015, day=10))


def test_part1():
    assert 252594 == d10.part1(day10_input)


def test_part2():
    assert 3579328 == d10.part2(day10_input)
