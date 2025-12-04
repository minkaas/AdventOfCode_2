import pathlib
from time import time


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
        data.append(temp)
    return data


def check_adjacents(data, row, col):
    result = 0
    adjacents = [(-1, -1), (1, -1), (-1, 1), (1, 1), (1, 0), (0, 1), (-1, 0), (0, - 1)]
    for adj in adjacents:
        coord1 = row + adj[0]
        coord2 = col + adj[1]
        if not (coord1 >= len(data) or coord1 < 0 or coord2 >= len(data[0]) or coord2 < 0):
            if data[coord1][coord2] == 1:
                result += 1
    return result < 4


def prettyprint(data, touched):
    for i in range(0, len(data)):
        to_print = ""
        for j in range(0, len(data[i])):
            if (i, j) in touched:
                to_print += 'X'
            elif data[i][j] == 1:
                to_print += '@'
            else:
                to_print += '.'
        print(to_print)


def part1(data):
    result = 0
    touched = []
    for row in range(0, len(data)):
        for col in range(0, len(data[row])):
            if data[row][col] == 1:
                if check_adjacents(data, row, col):
                    result += 1
                    touched.append((row, col))
    return result


def part2(data):
    result = 0
    removed = 1
    while removed != 0:
        removed = 0
        touched = []
        for row in range(0, len(data)):
            for col in range(0, len(data[row])):
                if data[row][col] == 1:
                    if check_adjacents(data, row, col):
                        result += 1
                        touched.append((row, col))
        for touch in touched:
            data[touch[0]][touch[1]] = 0
            removed += 1
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