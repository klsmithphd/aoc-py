import aoc2016.day07 as d07
import utils.core as u


d07_s00_raw = [
    "abba[mnop]qrst",
    "abcd[bddb]xyyx",
    "aaaa[qwer]tyui",
    "ioxxoj[asdfgh]zxcvbn"
]

d07_s01_raw = [
    "aba[bab]xyz",
    "xyx[xyx]xyx",
    "aaa[kek]eke",
    "zazbz[bzb]cdb"
]

d07_s00 = [
    (["abba", "qrst"], ["mnop"]),
    (["abcd", "xyyx"], ["bddb"]),
    (["aaaa", "tyui"], ["qwer"]),
    (["ioxxoj", "zxcvbn"], ["asdfgh"])
]

d07_s01 = [
    (["aba", "xyz"], ["bab"]),
    (["xyx", "xyx"], ["xyx"]),
    (["aaa", "eke"], ["kek"]),
    (["zazbz", "cdb"], ["bzb"])
]


def test_parse():
    assert d07_s00 == d07.parse(d07_s00_raw)
    assert d07_s01 == d07.parse(d07_s01_raw)


def test_hasabba():
    assert False == d07.hasabba("abbc")
    assert False == d07.hasabba("aaaa")
    assert True == d07.hasabba("abba")
    assert True == d07.hasabba("aaaaxyyx")


def test_hastlssupport():
    assert [True, False, False, True] == [
        d07.hastlssupport(ip) for ip in d07_s00]


day07_input = d07.parse(u.standard_puzzle_input(year=2016, day=7))


def test_part1():
    assert 110 == d07.part1(day07_input)
