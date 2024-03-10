import aoc2016.day04 as d04
import utils.core as u

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


def test_isrealroom():
    assert [True, True, True, False] == [d04.isrealroom(r) for r in d04_s00]


def test_real_room_sector_id_sum():
    assert 1514 == d04.real_room_sector_id_sum(d04_s00)


day04_input = d04.parse(u.standard_puzzle_input(year=2016, day=4))


def test_part1():
    assert 361724 == d04.part1(day04_input)
