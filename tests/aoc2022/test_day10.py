from aoc2022.day10 import parse, part1, part2,\
    register_values, signal_samples, signal_strength_sum, screen
from utils.core import standard_puzzle_input

d10_s01_raw = """noop
addx 3
addx -5""".splitlines()

d10_s02_raw = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines()

d10_s01 = ["noop", 3, -5]
d10_s02 = parse(d10_s02_raw)

d10_s02_screen = """##  ##  ##  ##  ##  ##  ##  ##  ##  ##  
###   ###   ###   ###   ###   ###   ### 
####    ####    ####    ####    ####    
#####     #####     #####     #####     
######      ######      ######      ####
#######       #######       #######     """


def test_parse():
    assert d10_s01 == parse(d10_s01_raw)


def test_register_values():
    assert [1, 1, 1, 4, 4, -1] == list(register_values(d10_s01))


def test_signal_samples():
    assert [21, 19, 18, 21, 16, 18] == list(signal_samples(d10_s02))


def test_signal_strength_sum():
    assert 13140 == signal_strength_sum(d10_s02)


def test_screen():
    assert d10_s02_screen == screen(d10_s02)


d10_input = parse(standard_puzzle_input(year=2022, day=10))
# ECZUZALR
d10_input_screen = """####  ##  #### #  # ####  ##  #    ###  
#    #  #    # #  #    # #  # #    #  # 
###  #      #  #  #   #  #  # #    #  # 
#    #     #   #  #  #   #### #    ###  
#    #  # #    #  # #    #  # #    # #  
####  ##  ####  ##  #### #  # #### #  # """


def test_day10_part1_soln():
    assert 16020 == part1(d10_input)


def test_day10_part2_soln():
    assert d10_input_screen == part2(d10_input)
