import aoc2015.day11 as d11
import utils.core as u

d11_s00 = d11.string_as_ints("hijklmmn")
d11_s01 = d11.string_as_ints("abbceffg")
d11_s02 = d11.string_as_ints("abbcegjk")

d11_s03 = "abcdefgh"
d11_s03_next = "abcdffaa"

d11_s04 = "ghijklmn"
d11_s04_next = "ghjaabcc"


def test_rules():
    "Tests all the password rules"
    assert True == d11.increasing_straight(d11_s00)
    assert False == d11.no_disallowed(d11_s00)
    assert False == d11.two_distinct_pairs(d11_s00)
    assert False == d11.valid_password(d11_s00)

    assert False == d11.increasing_straight(d11_s01)
    assert True == d11.no_disallowed(d11_s01)
    assert True == d11.two_distinct_pairs(d11_s01)
    assert False == d11.valid_password(d11_s01)

    assert False == d11.increasing_straight(d11_s02)
    assert True == d11.no_disallowed(d11_s02)
    assert False == d11.two_distinct_pairs(d11_s02)
    assert False == d11.valid_password(d11_s02)

    assert True == d11.valid_password(d11.string_as_ints(d11_s03_next))
    assert True == d11.valid_password(d11.string_as_ints(d11_s04_next))


def test_increment():
    assert [0, 0, 0, 0, 0, 0, 0, 1] == \
        d11.increment([0, 0, 0, 0, 0, 0, 0, 0])
    assert [0, 0, 0, 0, 0, 0, 0, 25] == \
        d11.increment([0, 0, 0, 0, 0, 0, 0, 24])
    assert [0, 0, 0, 0, 0, 0, 1, 0] == \
        d11.increment([0, 0, 0, 0, 0, 0, 0, 25])
    assert [1, 0, 0, 0, 0, 0, 0, 0] == \
        d11.increment([0, 25, 25, 25, 25, 25, 25, 25])


def test_next_wo_disallowed_chars():
    assert "hjaaaaaa" == d11.nums_fn(d11.next_wo_disallowed_chars, "hijklmmn")
    assert "jaaaaaaa" == d11.nums_fn(d11.next_wo_disallowed_chars, "ijklmnop")
    assert "abcdefgh" == d11.nums_fn(d11.next_wo_disallowed_chars, "abcdefgh")
    assert "ghjaaaaa" == d11.nums_fn(d11.next_wo_disallowed_chars, "ghijklmn")


def test_next_aabcc():
    assert "hacaabcc" == d11.nums_fn(d11.next_aabcc, "habxxzzz")
    assert "habxxyzz" == d11.nums_fn(d11.next_aabcc, "habxxyzz")
    assert "habbbcdd" == d11.nums_fn(d11.next_aabcc, "habaabcd")
    assert "ghjaabcc" == d11.nums_fn(d11.next_aabcc, "ghjaaaaa")


def test_next_valid_password():
    assert d11_s03_next == d11.next_valid_password(d11_s03)
    assert d11_s04_next == d11.next_valid_password(d11_s04)


day11_input = d11.parse(u.standard_puzzle_input(year=2015, day=11))


def test_part1():
    assert "hxbxxyzz" == d11.part1(day11_input)


def test_part2():
    assert "hxcaabcc" == d11.part2(day11_input)
