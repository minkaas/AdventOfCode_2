import pathlib
from time import time
import re
import math
import scipy as sp


def parse(puzzle_input):
    values = puzzle_input.split("\n\n")
    data = []
    for value in values:
        temp = []
        for val in value.split("\n"):
            vs = re.findall("\d+", val)
            temp.append((int(vs[0]), int(vs[1])))
        data.append(temp)
    return data


def part1(data):
    result = 0
    i = 0
    for equation in data:
        i += 1
        button_A = equation[0]
        button_B = equation[1]
        prize = equation[2]
        a = [[button_A[0], button_B[0]], [button_A[1], button_B[1]]]
        b = [prize[0], prize[1]]
        s = sp.linalg.solve(a, b)
        if math.isclose(round(s[0]), s[0], rel_tol=0, abs_tol=1e-4) and math.isclose(round(s[1]), s[1], rel_tol=0, abs_tol=1e-4):
            result += int(round(s[0])) * 3 + int(round(s[1])) * 1
    return result


def part2(data):
    result = 0
    i = 0
    for equation in data:
        i += 1
        button_A = equation[0]
        button_B = equation[1]
        prize = equation[2]
        a = [[button_A[0], button_B[0]], [button_A[1], button_B[1]]]
        b = [prize[0] + 10000000000000, prize[1] + 10000000000000]
        s = sp.linalg.solve(a, b)
        if math.isclose(round(s[0]), s[0], rel_tol=0, abs_tol=1e-4) and math.isclose(round(s[1]), s[1], rel_tol=0, abs_tol=1e-4):
            result += int(round(s[0])) * 3 + int(round(s[1])) * 1
    return result


def solve(puzzle_input):
    data = parse(puzzle_input)
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
