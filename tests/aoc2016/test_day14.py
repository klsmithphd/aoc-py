import aoc2016.day14 as d14
import more_itertools as mit
import utils.core as u

d14_s00 = "abc"


def test_triple_char_key_candidates():
    assert [18, 39, 45, 64, 77, 79, 88, 91, 92] == \
        [idx for idx, _ in mit.take(
            9, d14.triple_char_key_candidates(d14.md5, d14_s00))]
    assert [5, 10] == \
        [idx for idx, _ in mit.take(
            2,  d14.triple_char_key_candidates(d14.smd5, d14_s00))]


def test_pad_keys():
    assert [39, 92] == mit.take(2, d14.pad_keys(d14.md5, d14_s00))


def test_last_pad_key():
    assert 22728 == d14.last_pad_key(d14.md5, d14_s00)


def test_last_stretched_pad_key():
    assert 22551 == d14.last_pad_key(d14.smd5, d14_s00)


day14_input = d14.parse(u.standard_puzzle_input(year=2016, day=14))


def test_part1():
    assert 15168 == d14.part1(day14_input)


def test_part2():
    assert 20864 == d14.part2(day14_input)
