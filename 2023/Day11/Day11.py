import pathlib
from time import time

import numpy

def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for i in range(len(values[0])):
        line = values[i]
        char_list = []
        for j in range(len(line)):
            if line[j] == ".":
                char_list.append(False)
            else:
                char_list.append(True)
        data.append(char_list)
    return data


def calc_rows(data):
    result = []
    for i in range(len(data)):
        if len(set(data[i])) == 1:
            result.append(i)
    return result


def add_rows_p2(data):
    rows = calc_rows(data)
    data = numpy.transpose(data)
    data = data.tolist()
    columns = calc_rows(data)
    return rows, columns


def get_galaxies(data):
    galaxies = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j]:
                galaxies.append((i, j))
    return galaxies


def part1(data):
    result = 0
    rows, columns = add_rows_p2(data)
    galaxies = get_galaxies(data)
    for i in range(len(galaxies)):
        (gal_i, gal_j) = galaxies[i]
        for j in range(i + 1, len(galaxies)):
            (to_i, to_j) = galaxies[j]
            distance = get_distance(gal_i, to_i, gal_j, to_j, rows, columns, 1)
            result += distance
    return result


def get_distance(x1, x2, y1, y2, rows, columns, to_add):
    result = 0
    for row in rows:
        if x1 < row < x2 or x2 < row < x1:
            result += to_add
    for col in columns:
        if y1 < col < y2 or y2 < col < y1:
            result += to_add
    result += abs(x1 - x2) + abs(y1 - y2)
    return result


def part2(data):
    result = 0
    rows, columns = add_rows_p2(data)
    galaxies = get_galaxies(data)
    for i in range(len(galaxies)):
        (gal_i, gal_j) = galaxies[i]
        for j in range(i + 1, len(galaxies)):
            (to_i, to_j) = galaxies[j]
            distance = get_distance(gal_i, to_i, gal_j, to_j, rows, columns, 999999)
            result += distance
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
