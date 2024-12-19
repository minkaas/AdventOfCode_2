import math
import pathlib
from time import time

max_x = 71
max_y = 71


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        val = value.split(',')
        data.append((int(val[0]), int(val[1])))
    return data


def make_grid(data, kilobytes):
    new_data = data[:kilobytes]
    result = []
    padding = ['#'] * (max_x + 2)
    result.append(padding)
    for i in range(0, max_y):
        to_add = ['#'] + ['.'] * max_x + ['#']
        result.append(to_add)
    result.append(padding)
    for dat in new_data:
        result[dat[1]+1][dat[0]+1] = '#'
    return result


def print_grid(data):
    for i in range(1, max_x + 1):
        to_print = ""
        for j in range(1, max_y + 1):
            to_print += data[i][j]
        print(to_print)


def reconstruct_path(cameFrom, current):
    result_path = []
    while current in cameFrom.keys():
        result_path.insert(0, current)
        current = cameFrom[current]
    return len(result_path)


def get_neighbours(current, data):
    look_around = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 0 north 1 east 2 south 3 west
    bours = []
    for look in look_around:
        new = tuple(map(sum, zip(current, look)))
        if data[new[0]][new[1]] != '#':
            bours.append(new)
    return bours


def path_find(grid, start, goal):
    to_explore = [start]
    cameFrom = {}
    best_score = {}
    best_score[start] = 0
    best_score[(-1, -1)] = math.inf
    while len(to_explore):
        current = (-1, -1)
        for i in range(0, len(to_explore)):
            if best_score[to_explore[i]] < best_score[current]:
                current = to_explore[i]
        to_explore.remove(current)
        if current == goal:
            return reconstruct_path(cameFrom, current)
        neighbours = get_neighbours(current, grid)
        for bour in neighbours:
            if bour not in best_score:
                cameFrom[bour] = current
                best_score[bour] = best_score[current] + 1
                to_explore.append(bour)
            elif best_score[bour] >= best_score[current] + 1:
                cameFrom[bour] = current
                best_score[bour] = best_score[current] + 1
                if bour not in to_explore:
                    to_explore.append(bour)


def part1(data):
    grid = make_grid(data, 1024)
    start = (1, 1)
    end = (max_x, max_y)
    result = path_find(grid, start, end)
    return result


def part2(data):
    start = (1, 1)
    end = (max_x, max_y)
    for i in range(1025, len(data)):
        grid = make_grid(data, i)
        result = path_find(grid, start, end)
        if result is None:
            return data[i-1]
    return 0


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
