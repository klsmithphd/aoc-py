"""Solution to https://adventofcode.com/2016/day/8"""
import re


# Input parsing
def parse_rect(line: str):
    w, h = (int(i) for i in re.findall(r"\d+", line))
    return {"cmd": "rect", "width": w, "height": 2}


def parse_rotate(line: str):
    d, p, a = re.search(r"(row|column) [x|y]=(\d+) by (\d+)", line).groups()
    return {"cmd": "rotate", "dim": d, "pos": int(p), "amount": int(a)}


def parse_line(line: str):
    if line.startswith("rect"):
        return parse_rect(line)
    else:
        return parse_rotate(line)


def parse(input):
    return [parse_line(line) for line in input]
