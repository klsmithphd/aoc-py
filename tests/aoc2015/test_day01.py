import aoc2015.day01 as d01

d01_s00 = d01.parse(["(())"])
d01_s01 = d01.parse(["()()"])
d01_s02 = d01.parse(["((("])
d01_s03 = d01.parse(["(()(()("])
d01_s04 = d01.parse(["))((((("])
d01_s05 = d01.parse(["())"])
d01_s06 = d01.parse(["))("])
d01_s07 = d01.parse([")))"])
d01_s08 = d01.parse([")())())"])

d01_s09 = d01.parse([")"])
d01_s10 = d01.parse(["()())"])


def test_final_floor():
    assert 0 == d01.final_floor(d01_s00)
    assert 0 == d01.final_floor(d01_s01)
    assert 3 == d01.final_floor(d01_s02)
    assert 3 == d01.final_floor(d01_s03)
    assert 3 == d01.final_floor(d01_s04)
    assert -1 == d01.final_floor(d01_s05)
    assert -1 == d01.final_floor(d01_s06)
    assert -3 == d01.final_floor(d01_s07)
    assert -3 == d01.final_floor(d01_s08)


def test_first_time_in_basement():
    assert 1 == d01.first_time_in_basement(d01_s09)
    assert 5 == d01.first_time_in_basement(d01_s10)
