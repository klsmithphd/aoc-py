"""Solution to https://adventofcode.com/2015/day/14"""
import collections as c
import re


# Input parsing
Reindeer = c.namedtuple("Reindeer", ["speed", "fly", "span"])


def parse_line(line: str):
    speed, fly_time, rest_time = (int(x) for x in re.findall(r"\d+", line))
    return Reindeer(speed, fly_time, fly_time+rest_time)


def parse(input):
    return [parse_line(line) for line in input]


# Puzzle logic
def position(time, reindeer: Reindeer):
    """Computes the position of a reindeer at a given time"""
    speed, fly, span = reindeer
    intervals = time // span
    remainder = min(fly, time % span)
    return intervals * fly * speed + remainder * speed


def positions(time, reindeers):
    """Computes the positions of all reindeer at a given time"""
    return [position(time, r) for r in reindeers]


def points(positions):
    """Computes the score for all reindeer where any reindeer in the lead gets 
    1 point"""
    lead = max(positions)
    return (1 if p == lead else 0 for p in positions)


def cumulative_points(time, reindeers):
    times = range(1, time+1)
    # "Rows" are times, "Columns" are points-per-reindeer
    points_at_times = (points(positions(t, reindeers)) for t in times)
    # "Rows" are reindeer, "Columns" are points-at-time
    reindeer_points = zip(*points_at_times)
    # Sum up the points ("columns") for each reindeer
    return (sum(r) for r in reindeer_points)


# Puzzle solutions
def part1(input):
    """Distance that the winning reinder traveled after exactly 2503 seconds"""
    return max(position(2503, r) for r in input)


def part2(input):
    """Maximum number of points any reindeer has accumulated after 2503 seconds"""
    return max(cumulative_points(2503, input))
