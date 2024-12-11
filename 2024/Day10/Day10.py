import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    padding = [-1] * (len(values[0]) + 2)
    data.append(padding)
    for value in values:
        temp = [-1] + [int(x) for x in value] + [-1]
        data.append(temp)
    data.append(padding)
    return data


def find_starts(data):
    starts = []
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            if data[i][j] == 0:
                starts.append((i, j))
    return starts


def has_next(data, current):
    look_around = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    results = []
    for look in look_around:
        new = tuple(map(sum,zip(current, look)))
        if data[new[0]][new[1]] - data[current[0]][current[1]] == 1:
            results.append(new)
    return results


def part1(data):
    starts = find_starts(data)
    result = 0
    for start in starts:
        to_check = [start]
        nines = []
        while len(to_check) > 0:
            curr = to_check.pop()
            if data[curr[0]][curr[1]] == 9:
                nines.append(curr)
            else:
                next_coords = has_next(data, curr)
                to_check.extend(next_coords)
        result += len(list(set(nines)))
    return result


def part2(data):
    starts = find_starts(data)
    result = 0
    for start in starts:
        to_check = [start]
        difficulty = 1
        while len(to_check) > 0:
            curr = to_check.pop()
            if data[curr[0]][curr[1]] != 9:
                next_coords = has_next(data, curr)
                difficulty += len(next_coords) - 1
                to_check.extend(next_coords)
        result += difficulty
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
