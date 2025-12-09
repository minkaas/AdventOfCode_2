import pathlib
from time import time
import numpy as np
import cv2

def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        data.append((int(value.split(",")[0]), int(value.split(",")[1])))
    return data


def rectangle_size(pointa, pointb):
    return (abs(pointa[1] - pointb[1]) + 1) * (abs(pointa[0] - pointb[0]) + 1)


def part1(data):
    result = 0
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            result = max(result, rectangle_size(data[i], data[j]))
    return result


def part2(data):
    result = 0
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            if check_valid(data, data[i], data[j]):
                result = max(result, rectangle_size(data[i], data[j]))
    return result


def check_valid(data, tile1, tile2):
    # if the rectangle is intersected by a square it is extremely cap
    minx = min(tile1[0], tile2[0])
    maxx = max(tile1[0], tile2[0])
    miny = min(tile1[1], tile2[1])
    maxy = max(tile1[1], tile2[1])

    for i in range(0, len(data)):
        lineseg1 = data[i]
        lineseg2 = data[(i + 1) % len(data)]
        if not (max(lineseg1[0], lineseg2[0]) <= minx or maxx <= min(lineseg1[0], lineseg2[0]) or max(lineseg1[1], lineseg2[1]) <= miny or maxy <= min(lineseg1[1], lineseg2[1])):
            return False
    return True


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    data = parse(puzzle_input)
    sol2 = part22(data)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
