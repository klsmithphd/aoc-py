from aoc2022.day13 import parse, part1, isinorder, inorder_packet_id_sum
from utils.core import standard_puzzle_input

d13_s0_raw = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".splitlines()


d13_s0 = [[[1, 1, 3, 1, 1],
          [1, 1, 5, 1, 1]],

          [[[1], [2, 3, 4]],
           [[1], 4]],

          [[9],
           [[8, 7, 6]]],

          [[[4, 4], 4, 4],
           [[4, 4], 4, 4, 4]],

          [[7, 7, 7, 7],
           [7, 7, 7]],

          [[],
           [3]],

          [[[[]]],
           [[]]],

          [[1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
           [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]]]


def test_parse():
    assert d13_s0 == parse(d13_s0_raw)


def test_isinorder():
    assert True == isinorder([1, 2], [2])
    assert True == isinorder(*d13_s0[0])
    assert True == isinorder(*d13_s0[1])
    assert False == isinorder(*d13_s0[2])
    assert True == isinorder(*d13_s0[3])
    assert False == isinorder(*d13_s0[4])
    assert True == isinorder(*d13_s0[5])
    assert False == isinorder(*d13_s0[6])
    assert False == isinorder(*d13_s0[7])


def test_inorder_packet_id_sum():
    assert 13 == inorder_packet_id_sum(d13_s0)


d13_input = parse(standard_puzzle_input(year=2022, day=13))


def test_day13_part1_soln():
    assert 5503 == part1(d13_input)


# def test_day13_part2_soln():
#     assert 1 == day13_soln.part2(d13_input)
