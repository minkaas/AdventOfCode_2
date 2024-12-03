import pathlib
from time import time
import re


def part1(data):
    all_muls = re.findall("mul\(\d+,\d+\)", data)
    result = 0
    for inst in all_muls:
        digits = re.findall('\d+', inst)
        result += int(digits[0]) * int(digits[1])
    return result


def part2(data):
    all_muls = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
    disable = False
    result = 0
    for inst in all_muls:
        if inst == "do()":
            disable = False
        elif inst == "don't()":
            disable = True
        elif not disable:
            digits = re.findall('\d+', inst)
            result += int(digits[0]) * int(digits[1])
    return result


def solve(data):
    sol1 = part1(data)
    sol2 = part2(data)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
