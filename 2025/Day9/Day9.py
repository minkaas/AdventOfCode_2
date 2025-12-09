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
    data.append(data[0])
    boundaries = {}
    for i in range(0, len(data) - 1):
        tile1 = data[i]
        tile2 = data[i + 1]
        x1, y1 = tile1
        x2, y2 = tile2
        if x1 == x2:
            for y in range(min(y1,y2), max(y1, y2) + 1):
                if y not in boundaries:
                    boundaries[y] = [x1, x1]
                else:
                    boundaries[y][0] = min(boundaries[y][0], x1)
                    boundaries[y][1] = max(boundaries[y][1], x1)
        elif y1 == y2:
            if y1 not in boundaries:
                boundaries[y1] = [min(x1, x2), max(x1, x2)]
            else:
                boundaries[y1][0] = min(boundaries[y1][0], x1, x2)
                boundaries[y1][1] = max(boundaries[y1][1], x1, x2)
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            valid = True
            tile1 = data[i]
            tile2 = data[j]
            x1, y1 = tile1
            x2, y2 = tile2
            minx = min(x1, x2)
            maxx = max(x1, x2)
            miny = min(y1, y2)
            maxy = max(y1, y2)
            for y in range(miny, maxy + 1):
                if y not in boundaries:
                    valid = False
                    break
                boundminx, boundmaxx = boundaries[y]
                if minx < boundminx or maxx > boundmaxx:
                    valid = False
                    break
            if valid:
                result = max(result, rectangle_size(tile1, tile2))
    return result

def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    data = parse(puzzle_input)
    sol2 = part2(data)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
