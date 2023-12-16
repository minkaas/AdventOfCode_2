import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for i in range(len(values[0])):
        line = values[i]
        char_list = []
        for j in range(len(line)):
            char_list.append(line[j])
        data.append(char_list)
    return data


def print_matrix(matrix, energized):
    energy = []
    for en in energized:
        i, j, dir = en
        energy.append((i, j))
    for i in range(len(matrix)):
        to_print = ""
        for j in range(len(matrix[i])):
            if (i, j) in energy:
                to_print += "#"
            else:
                to_print += "."
        print(to_print)

#0 = right, 1 = left, 2 = up, 3 = down
def go_beam(current, energized, matrix):
    updated = True
    while(updated):
        i, j, direct = current
        temp_updated = False
        if direct == 0:
            if j + 1 < len(matrix[0]):
                mirror = matrix[i][j+1]
                if mirror == "\\":
                    if (i, j+1, 3) not in energized:
                        temp_updated = True
                        energized.add((i, j+1, 3))
                        current = (i, j+1, 3)
                elif mirror == "/":
                    if (i, j+1, 2) not in energized:
                        temp_updated = True
                        energized.add((i, j+1, 2))
                        current = (i, j+1, 2)
                elif mirror == "|":
                    if (i, j+1, 3) not in energized:
                        temp_updated = True
                        energized.add((i, j+1, 3))
                        energized = go_beam((i, j+1, 3), energized, matrix)
                    if (i, j+1, 2) not in energized:
                        temp_updated = True
                        energized.add((i, j+1, 2))
                        current = (i, j+1, 2)
                elif (i, j+1, direct) not in energized:
                    temp_updated = True
                    energized.add((i, j + 1, direct))
                    current = (i, j+1, direct)
        elif direct == 1: # left
            if j - 1 >= 0:
                mirror = matrix[i][j-1]
                if mirror == "\\":
                    if (i, j-1, 2) not in energized:
                        temp_updated = True
                        energized.add((i, j-1, 2))
                        current = (i, j-1, 2)
                elif mirror == "/":
                    if (i, j-1, 3) not in energized:
                        temp_updated = True
                        energized.add((i, j-1, 3))
                        current = (i, j-1, 3)
                elif mirror == "|":
                    if (i, j-1, 2) not in energized:
                        temp_updated = True
                        energized.add((i, j-1, 2))
                        energized = go_beam((i, j-1, 2), energized, matrix)
                    if (i, j-1, 3) not in energized:
                        temp_updated = True
                        energized.add((i, j-1, 3))
                        current = (i, j-1, 3)
                elif (i, j-1, direct) not in energized:
                    temp_updated = True
                    energized.add((i, j - 1, direct))
                    current = (i, j - 1, direct)
        elif direct == 2: # up
            if i - 1 >= 0:
                mirror = matrix[i-1][j]
                if mirror == "\\":
                    if (i-1, j, 1) not in energized:
                        temp_updated = True
                        energized.add((i-1, j, 1))
                        current = (i-1, j, 1)
                elif mirror == "/":
                    if (i-1, j, 0) not in energized:
                        temp_updated = True
                        energized.add((i-1, j, 0))
                        current = (i-1, j, 0)
                elif mirror == "-":
                    if (i-1, j, 1) not in energized:
                        temp_updated = True
                        energized.add((i-1, j, 1))
                        energized = go_beam((i-1, j, 1), energized, matrix)
                    if (i-1, j, 0) not in energized:
                        temp_updated = True
                        energized.add((i-1, j, 0))
                        current = (i-1, j, 0)
                elif (i-1, j, 2) not in energized:
                    temp_updated = True
                    energized.add((i-1, j, 2))
                    current = (i-1, j, 2)
        elif direct == 3: # down
            if i + 1 < len(matrix):
                mirror = matrix[i+1][j]
                if mirror == "\\":
                    if (i+1, j, 0) not in energized:
                        temp_updated = True
                        energized.add((i+1, j, 0))
                        current = (i+1, j, 0)
                elif mirror == "/":
                    if (i+1, j, 1) not in energized:
                        temp_updated = True
                        energized.add((i+1, j, 1))
                        current = (i+1, j, 1)
                elif mirror == "-":
                    if (i+1, j, 1) not in energized:
                        temp_updated = True
                        energized.add((i+1, j, 1))
                        energized = go_beam((i+1, j, 1), energized, matrix)
                    if (i+1, j, 0) not in energized:
                        temp_updated = True
                        energized.add((i+1, j, 0))
                        current = (i+1, j, 0)
                elif (i+1, j, 3) not in energized:
                    temp_updated = True
                    energized.add((i+1, j, 3))
                    current = (i+1, j, 3)
        if not temp_updated:
            updated = False
    return energized


def part1(data):
    result = 0
    start_val = data[0][0]
    start = (0, 0, 0)
    energized = set()
    if start_val == "\\":
        start = (0, 0, 3)
    elif start_val == "/":
        start = (0, 0, 2)
    elif start_val == "|":
        energized.add((0, 0, 2))
        energized = go_beam(start, energized, data)
        start = (0, 0, 3)
    energized.add(start)
    energized = go_beam(start, energized, data)
    # print_matrix(data, energized)
    energy = set()
    for (i, j, dir) in energized:
        energy.add((i, j))
    return len(energy)

#0 = right, 1 = left, 2 = up, 3 = down
def part2(data):
    result = 0
    for j in range(len(data[0])):
        start_val = data[0][j]
        start = (0, j, 3)
        energized = set()
        if start_val == "\\":
            start = (0, j, 0)
        elif start_val == "/":
            start = (0, j, 1)
        elif start_val == "-":
            energized.add((0, j, 0))
            energized = go_beam((0, j, 0), energized, data)
            start = (0, j, 1)
        energized.add(start)
        energized = go_beam(start, energized, data)
        energy = set()
        for (i, a, dir) in energized:
            energy.add((i, a))
        result = max(result, len(energy))
    max_i = len(data) - 1
    for j in range(len(data[max_i])):
        start_val = data[max_i][j]
        start = (max_i, j, 2)
        energized = set()
        if start_val == "\\":
            start = (max_i, j, 1)
        elif start_val == "/":
            start = (max_i, j, 0)
        elif start_val == "-":
            energized.add((max_i, j, 0))
            energized = go_beam((max_i, j, 0), energized, data)
            start = (max_i, j, 1)
        energized.add(start)
        energized = go_beam(start, energized, data)
        energy = set()
        for (i, a, dir) in energized:
            energy.add((i, a))
        result = max(result, len(energy))
    for i in range(len(data)):
        start_val = data[i][0]
        start = (i, 0, 0)
        energized = set()
        if start_val == "\\":
            start = (i, 0, 3)
        elif start_val == "/":
            start = (i, 0, 2)
        elif start_val == "|":
            energized.add((i, 0, 2))
            energized = go_beam((i, 0, 2), energized, data)
            start = (i, 0, 3)
        energized.add(start)
        energized = go_beam(start, energized, data)
        energy = set()
        for (a, j, dir) in energized:
            energy.add((a, j))
        result = max(result, len(energy))
    max_j = len(data[0]) - 1
    for i in range(len(data)):
        start_val = data[i][max_j]
        start = (i, max_j, 1)
        energized = set()
        if start_val == "\\":
            start = (i, max_j, 2)
        elif start_val == "/":
            start = (i, max_j, 3)
        elif start_val == "|":
            energized.add((i, max_j, 2))
            energized = go_beam((i, max_j, 2), energized, data)
            start = (i, max_j, 3)
        energized.add(start)
        energized = go_beam(start, energized, data)
        energy = set()
        for (a, j, dir) in energized:
            energy.add((a, j))
        result = max(result, len(energy))
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
