# aoc-py
Solutions to [Advent of Code](https://adventofcode.com) challenges implemented 
in Python

# Usage

## Pre-requisites
This project uses https://pdm-project.org/. Follow its 
[installation guidelines](https://pdm-project.org/latest/#installation).
Once installed, `cd` into `aoc-py` and issue
```
pdm install
```

## Running
You can execute any day's implemented solutions, either with my puzzle input 
files or you can provide your own.
```
pdm aoc   # (or pdm run aoc)
```

For example, to execute the solution for the
[2022 Day 1](https://adventofcode.com/2022/day/1) puzzle, just execute
```
pdm aoc 2022 1 -v
```
The `-v` is purely optional, but will help print what the values are supposed
to mean in the context of the puzzle narrative.

You can specify your own puzzle input file with the `-i` command-line option.


Full usage:
```
usage: aoc.py [-h] [-i INPUT] [-v] year day

positional arguments:
  year                  Puzzle year
  day                   Puzzle day

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        [Optional] puzzle input
  -v, --verbose         [Optional] verbose printing
```

# License
Copyright 2023 Ken Smith

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
