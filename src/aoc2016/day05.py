"""Solution to https://adventofcode.com/2016/day/5"""
import itertools as it
import functools as ft
import more_itertools as mit
import pipe as p
import utils.digest as dig

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
parse = mit.first


# Puzzle logic
def md5_digest(prefix: str):
    """For a given `prefix`, return a function that will return the MD5 digest
    (in bytes) given a value to append to the prefix"""
    return lambda num: dig.md5_digest(f"{prefix}{num}")


def five_zero_indices(prefix: str):
    """A (potentially infinite) sequence of the indices that, when
    appended to the string `prefix`, result in an MD5 hash that starts
    with five zeros"""
    digest = md5_digest(prefix)
    return it.count() | p.filter(lambda i: dig.isfivezerostart(digest(i)))


def indices_to_try(prefix):
    """A sequence of indices to try appending to the prefix. If the values are
    already cached (hardcoded), return those. Otherwise, just iterate from
    zero on up."""
    return CACHED_INDICES.get(prefix, it.count(0))


@p.Pipe
def str_join(iterable, separator=""):
    """A Pipe that emits a string joining all the values in `iterable`,
    separated by `separator`"""
    return separator.join(iterable)


def five_zero_digests(prefix: str):
    """A sequence of the MD5 digests (as bytes) for consecutive prefix-number
    strings that start with five zeroes."""
    return indices_to_try(prefix) \
        | p.map(md5_digest(prefix)) \
        | p.filter(dig.isfivezerostart)


def sixth_char(digest: bytes):
    """Returns the hex value (0-f) of the sixth character (in the string
    representation of) the MD5 digest"""
    return format(digest[2], "x")


def pos_char_pair(digest: bytes):
    """For a collection of bytes representing an MD5 hash, interpret the hash
    as having the sixth character represent a position and the seventh
    character represent the actual password character."""
    pos, ch = digest[2:4]
    return (pos, format(ch, "02x")[:1])


def password_chars(part: str) -> p.Pipe:
    """Apply the logic of part1 or part2 to emit pairs of position/character
    pairs in the deciphered password"""
    if part == 'part1':
        return p.Pipe(lambda digest: enumerate(map(sixth_char, digest)))
    if part == 'part2':
        return p.map(pos_char_pair)


def set_char(password, pair):
    """If the character at position `idx` in collection `s` is seen for the first
    time, update it to `ch`, else return `s` untouched."""
    idx, ch = pair
    if password[idx] == '*':
        return password[:idx] + ch + password[idx+1:]
    else:
        return password


@p.Pipe
def update_password(iterable):
    """Return an iterable (Pipe) of intermediate password guesses based
    on a sequence of new position-character pairs"""
    return it.accumulate(iterable, set_char, initial='********')


def password(part: str, prefix: str):
    """Using the puzzle logic given by `part` (either `part1` or `part2`),
    decipher the password for the door id (`prefix`)"""
    return five_zero_digests(prefix) \
        | password_chars(part) \
        | p.filter(lambda p: 0 <= p[0] <= 7) \
        | update_password \
        | p.skip_while(lambda x: '*' in x) \
        | p.take(1) \
        | str_join


password_part1 = ft.partial(password, 'part1')
password_part2 = ft.partial(password, 'part2')


# Puzzle solutions
def part1(input):
    """Given a door id (prefix), what is the password using the logic in part 1"""
    return password_part1(input)


def part2(input):
    """Given a door id (prefix), what is the password using the logic in part 2"""
    return password_part2(input)
