import aoc2016.day07 as d07


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
