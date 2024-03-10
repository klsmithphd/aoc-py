import aoc2016.day04 as d04

d04_s00_raw = [
    "aaaaa-bbb-z-y-x-123[abxyz]",
    "a-b-c-d-e-f-g-h-987[abcde]",
    "not-a-real-room-404[oarel]",
    "totally-real-room-200[decoy]"
]

d04_s00 = [
    (["aaaaa", "bbb", "z", "y", "x"], 123, "abxyz"),
    (["a", "b", "c", "d", "e", "f", "g", "h"], 987, "abcde"),
    (["not", "a", "real", "room"], 404, "oarel"),
    (["totally", "real", "room"], 200, "decoy")
]


def test_parse():
    assert d04_s00 == d04.parse(d04_s00_raw)
