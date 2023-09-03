from aoc2022.day07 import parse, part1, part2, change_dir, list_dir, \
    dir_paths, node_size, dir_total_below_100k, smallest_dir_size_to_remove, \
    MemoizedTreeSizer
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
             "h.lst": 62596
             },
            "b.txt": 14848514,
            "c.dat": 8504156,
            "d":
            {"j": 4060174,
             "d.log": 8033020,
             "d.ext": 5626152,
             "k": 7214296}
            }
           }


def test_change_dir():
    # Going into a directory updates the tree and appends the dir to the path
    assert {'tree': {'/': {}}, 'path': ['/']} == \
        change_dir({'tree': {}, 'path': []}, '/')
    # Going into a directory updates the tree and appends the dir to the path
    assert {'tree': {'/': {'a': {}}}, 'path': ['/', 'a']} == \
        change_dir({'tree': {'/': {}}, 'path': ['/']}, 'a')
    # Going to the parent directory leaves the tree the same and drops a dir
    # from the path
    assert {'tree': {'/': {'a': {}}}, 'path': ['/']} == \
        change_dir({'tree': {'/': {'a': {}}}, 'path': ['/', 'a']}, '..')


def test_list_dir():
    assert {'tree': {'/': {'a': {}, 'b': 12}}, 'path': ['/']} == \
        list_dir({'tree': {'/': {}}, 'path': ['/']},
                 ['dir a', '12 b'])


def test_parse():
    assert d07_s01 == parse(d07_s01_raw)


def test_dir_paths():
    assert [['/'], ['/', 'a'], ['/', 'a', 'e'],
            ['/', 'd']] == list(dir_paths(d07_s01))


def test_node_size():
    assert 584 == node_size(d07_s01, ['/', 'a', 'e', 'i'])
    assert 584 == node_size(d07_s01, ['/', 'a', 'e'])
    assert 94853 == node_size(d07_s01, ['/', 'a'])
    assert 24933642 == node_size(d07_s01, ['/', 'd'])
    assert 48381165 == node_size(d07_s01, ['/'])


def test_MemoizedTreeSizer_size():
    sizer = MemoizedTreeSizer(d07_s01)
    assert 584 == sizer.size('/', 'a', 'e', 'i')
    assert 584 == sizer.size('/', 'a', 'e')
    assert 94853 == sizer.size('/', 'a')
    assert 24933642 == sizer.size('/', 'd')
    assert 48381165 == sizer.size('/')


def test_dir_total_below_100k():
    assert 95437 == dir_total_below_100k(d07_s01)


def test_smallest_dir_size_to_remove():
    assert 24933642 == smallest_dir_size_to_remove(d07_s01)


d07_input = parse(standard_puzzle_input(year=2022, day=7))


def test_day06_part1_soln():
    assert 1306611 == part1(d07_input)


def test_day07_part2_soln():
    assert 13210366 == part2(d07_input)
