from aoc2022.day07 import parse
from utils.core import standard_puzzle_input

d07_s01_raw = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()

d07_s01 = {"/":
           {"a":
            {"e":
             {"i": 584},
                "f": 29116,
                "g": 2557,
                "h.lst": 62596},
               "b.txt": 14848514,
               "c.dat": 8504156,
               "d":
               {"j": 4060174,
                "d.log": 8033020,
                "d.ext": 5626152,
                "k": 7214296}}}


def test_parse():
    assert d07_s01 == parse(d07_s01_raw)


# d03_input = standard_puzzle_input(year=2022, day=7)


# def test_day07_part1_soln():
#     assert 1 == day07_soln.part1(d07_input)


# def test_day07_part2_soln():
#     assert 1 == day07_soln.part2(d07_input)
