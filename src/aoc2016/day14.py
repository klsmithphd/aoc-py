"""Solution to https://adventofcode.com/2016/day/14"""
import re
import toolz
import itertools as it
import more_itertools as mit
import utils.digest as dig


# Constants
STRETCH = 2017

CACHED_INDICES = {
    "abc":      [10, 25, 1471, 1596, 1610, 1715, 1778, 1951, 1994, 2023,
                 2288, 4249, 4340, 4352, 4533, 4829, 4878, 5014, 5226, 5803,
                 6878, 7087, 7120, 7137, 7182, 7229, 7280, 7317, 7460, 7841,
                 8058, 8277, 8472, 8473, 8487, 8550, 8574, 17372, 17438,
                 17506, 17737, 17768, 18105, 18175, 18210, 18302, 19212,
                 19236, 19270, 19334, 19346, 19366, 19369, 19471, 19498,
                 19799, 19880, 19915, 19947, 19950, 20212, 22097, 22122,
                 22551],
    "qzyelonm": [2773, 3030, 3168, 3244, 3399, 3428, 3503, 3523, 3681, 3738,
                 3818, 3837, 3868, 3982, 4029, 4038, 4201, 4221, 4606, 4641,
                 4763, 5045, 5174, 5262, 5283, 5394, 5436, 5484, 5499, 5643,
                 5790, 5869, 10535, 10700, 10736, 10802, 10983, 11049, 11060,
                 11182, 11254, 12801, 12817, 13203, 13245, 13309, 13348, 16243,
                 16405, 16456, 16457, 16500, 16540, 16729, 16803, 16849, 17033,
                 17060, 20035, 20316, 20409, 20779, 20822, 20864]
}

# Input parsing
parse = mit.first


# Puzzle logic
def stretched_md5_str(s: str):
    return mit.first(toolz.drop(STRETCH, mit.iterate(dig.md5_str, s)))


md5 = dig.md5_str
smd5 = stretched_md5_str


def hastriplechars(s: str):
    """Returns true if the string contains a sequence of at least three
    repeated characters"""
    return re.findall(r"(.)\1{2}", s)


def triple_char_key_candidates(hash_fn, salt: str):
    """Returns an (infinite) sequence of index, hash tuples that
    are potential key candidates based on the hash containing a sequence
    of a character repeated at least three times consecutively"""
    pairs = enumerate(hash_fn(f"{salt}{x}") for x in it.count())
    return ((idx, h) for idx, h in pairs if hastriplechars(h))


def fivepeat_in_thousand(windowed_candidates):
    """Predicate that tests whether any of the next thousand indices
    produces a hash that contains the tripled-character repeated five
    times"""
    idx, hsh = mit.first(windowed_candidates)
    match_str = "".join(re.findall(r"(.)\1{2}", hsh)[0] * 5)
    return any(i for i, h in windowed_candidates
               if idx < i <= idx + 1000 and
               re.findall(match_str, h))


def pad_keys(hash_fn, salt):
    """Returns an infinite sequence of all the indices that produce valid
    one-time pad keys for the given salt"""
    tests = mit.windowed(triple_char_key_candidates(hash_fn, salt), 1001, 1)
    return (test[0][0] for test in tests if fivepeat_in_thousand(test))


def last_pad_key(hash_fn, salt):
    """Returns the last (64th) one-time pad key for the given salt"""
    if hash_fn == smd5:
        seq = CACHED_INDICES.get(salt, pad_keys(hash_fn, salt))
    else:
        seq = pad_keys(hash_fn, salt)
    return mit.first(it.islice(seq, 63, 64))


# Puzzle solutions
def part1(input):
    """What index produces the 64th one-time pad key"""
    return last_pad_key(md5, input)


def part2(input):
    """What index produces the 64th one-time pad key with key stretching"""
    return last_pad_key(smd5, input)
