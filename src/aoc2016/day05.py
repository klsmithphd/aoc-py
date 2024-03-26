"""Solution to https://adventofcode.com/2016/day/5"""
import hashlib
import itertools as it
import more_itertools as mit

# Constants
CACHED_INDICES = {
    "abc":      [3231929, 5017308, 5278568, 5357525, 5708769,
                 6082117, 8036669, 8605828, 8609554, 8760605,
                 9495334, 10767910, 11039607, 12763908, 13666005,
                 13753421, 14810753, 15274776, 15819744, 18455182,
                 20014135, 23595234, 25025007, 25162359, 26439072,
                 30594017, 31051866, 33050215, 33841441, 34415073],
    "reyedfim": [797564, 938629, 1617991, 2104453, 2564359,
                 2834991, 3605750, 7183955, 7292419, 7668370,
                 8059094, 9738948, 10098451, 10105659, 11395933,
                 12187005, 13432325, 17274562, 18101341, 19897122,
                 21475898, 21671457, 21679503, 21842490, 23036372,
                 23090544, 25067104, 26815976, 27230372, 27410373]
}
"""The first 30 indices that, when concatenated with the prefix (key),
   result in an md5-hash that begins with five zeros. These values
   where computed using `mit.take(30, five-zero-indices(x))` where `x` is
   the prefix either in the sample problem or my actual input. 
   
   Caching (hard-coding) these values saves a lot of time for the unit tests."""

# Input parsing


def parse(input):
    return mit.first(input)


# Puzzle logic
def md5_bytes(s: str):
    return hashlib.md5(s.encode()).digest()


def isfivezerostart(bytes):
    return bytes[:3] < b'\x00\x00\x10'


def five_zero_indices(prefix: str):
    return (x for x in it.count(0) if isfivezerostart(md5_bytes(f"{prefix}{x}")))


def indices_to_try(prefix):
    return CACHED_INDICES.get(prefix, it.count(0))


def five_zero_hashes(prefix: str):
    indices = indices_to_try(prefix)
    bytes = (md5_bytes(f"{prefix}{idx}") for idx in indices)
    return (hash for hash in bytes if isfivezerostart(hash))


def password_part1(prefix: str):
    return "".join(hex(b[2])[2:] for b in mit.take(8, five_zero_hashes(prefix)))


def pos_char_pair(bytes):
    pos, ch = bytes[2:4]
    return (pos, format(ch, "02x")[:1])


def set_char(password, pair):
    idx, ch = pair
    if password[idx] == '*':
        return password[:idx] + ch + password[idx+1:]
    else:
        return password


def password_part2(prefix: str):
    pairs = (pos_char_pair(x) for x in five_zero_hashes(prefix))
    valid_pairs = (p for p in pairs if 0 <= p[0] <= 7)
    pwds = it.accumulate(valid_pairs, set_char, initial='********')
    return "".join(mit.first(it.dropwhile(lambda x: '*' in x, pwds)))


# Puzzle solutions
def part1(input):
    return password_part1(input)


def part2(input):
    return password_part2(input)
