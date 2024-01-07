import aoc2015.day09 as d09


d09_s00_raw = [
    "London to Dublin = 464",
    "London to Belfast = 518",
    "Dublin to Belfast = 141"
]

d09_s00 = {
    "London":  {"Dublin": 464, "Belfast": 518},
    "Dublin":  {"London": 464, "Belfast": 141},
    "Belfast": {"London": 518, "Dublin":  141}}


def test_parse():
    assert d09_s00 == d09.parse(d09_s00_raw)
