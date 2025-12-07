import pathlib
from time import time
import numpy as np


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        temp = []
        for val in value:
            if val == '.':
                temp.append(0)
            else:
                temp.append(1)
            if val == 'S':
                start = (0, len(temp)-1)
        data.append(temp)
    return data, start


def part1(data, start):
    splits = 0
    beams = [start]
    while len(beams):
        new_beams = []
        for beam in beams:
            row, col = beam
            if row + 1 < len(data) and data[row + 1][col] == 1:
                new_beams.append((row + 1, col - 1))
                new_beams.append((row + 1, col + 1))
                splits += 1
            elif row + 1 < len(data):
                new_beams.append((row + 1, col))
        beams = list(set(new_beams))
    return splits


def part2(data, start):
    timelines = 0
    beams = [start]
    all_beams = {start: 1}
    while len(beams):
        new_beams = []
        for beam in beams:
            row, col = beam
            if row + 1 < len(data) and data[row + 1][col] == 1:
                new_beams.append((row + 1, col - 1))
                new_beams.append((row + 1, col + 1))
                if (row + 1, col + 1) in all_beams:
                    all_beams[(row + 1, col + 1)] += all_beams[beam]
                else:
                    all_beams[(row + 1, col + 1)] = all_beams[beam]
                if (row + 1, col - 1) in all_beams:
                    all_beams[(row + 1, col - 1)] += all_beams[beam]
                else:
                    all_beams[(row + 1, col - 1)] = all_beams[beam]
            elif row + 1 < len(data):
                new_beams.append((row + 1, col))
                if (row + 1, col) in all_beams:
                    all_beams[(row + 1, col)] += all_beams[beam]
                else:
                    all_beams[(row + 1, col)] = all_beams[beam]
        beams = list(set(new_beams))
    for beam in all_beams:
        if beam[0] == len(data) - 1:
            timelines += all_beams[beam]
    return timelines


def solve(puzzle_input):
    data, start = parse(puzzle_input)
    sol1 = part1(data, start)
    data, start = parse(puzzle_input)
    sol2 = part2(data, start)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()