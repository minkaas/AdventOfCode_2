import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        temp = []
        for val in value:
            if val == ".":
                temp.append(0)
            elif val == "#":
                temp.append(1)
            else:
                temp.append(2)
        data.append(temp)
    return data


def find_start(data):
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if data[i][j] == 2:
                return i, j


def part1(data):
    current = find_start(data)
    data[current[0]][current[1]] = 0
    result = set()
    result.add(current)
    direction = 0       # 0 up, 1 right, 2 down, 3 left
    on_route = True
    while on_route:
        on_route = False
        if direction == 0 and current[0] > 0:
            on_route = True
            if data[current[0]-1][current[1]] == 0:
                current = (current[0]-1, current[1])
                result.add(current)
            else:
                direction = 1
        elif direction == 1 and current[1] < len(data[0]) - 1:
            on_route = True
            if data[current[0]][current[1]+1] == 0:
                current = (current[0], current[1]+1)
                result.add(current)
            else:
                direction = 2
        elif direction == 2 and current[0] < len(data) - 1:
            on_route = True
            if data[current[0]+1][current[1]] == 0:
                current = (current[0]+1, current[1])
                result.add(current)
            else:
                direction = 3
        elif direction == 3 and current[1] > 0:
            on_route = True
            if data[current[0]][current[1] - 1] == 0:
                current = (current[0], current[1] - 1)
                result.add(current)
            else:
                direction = 0
    return len(result), result


def print_matrix(data, visited):
    for i in range(0, len(data)):
        to_print = ""
        for j in range(0, len(data[i])):
            if (i, j) in visited:
                to_print += "X"
            elif data[i][j] == 1:
                to_print += "#"
            else:
                to_print += "."
        print(to_print)


def causes_loop(data, start, obstruction):
    current = (start[0], start[1], 0)
    result = set()
    on_route = True
    while on_route:
        on_route = False
        if current[2] == 0 and current[0] > 0:
            on_route = True
            if data[current[0]-1][current[1]] == 0 and (current[0]-1, current[1]) != obstruction:
                current = (current[0]-1, current[1], 0)
            else:
                current = (current[0], current[1], 1)
                if current in result:
                    return False
                result.add(current)
        elif current[2] == 1 and current[1] < len(data[0]) - 1:
            on_route = True
            if data[current[0]][current[1]+1] == 0 and (current[0], current[1]+1) != obstruction:
                current = (current[0], current[1]+1, 1)
            else:
                current = (current[0], current[1], 2)
                if current in result:
                    return False
                result.add(current)
        elif current[2] == 2 and current[0] < len(data) - 1:
            on_route = True
            if data[current[0]+1][current[1]] == 0 and (current[0]+1, current[1]) != obstruction:
                current = (current[0]+1, current[1], 2)
            else:
                current = (current[0], current[1], 3)
                if current in result:
                    return False
                result.add(current)
        elif current[2] == 3 and current[1] > 0:
            on_route = True
            if data[current[0]][current[1] - 1] == 0 and (current[0], current[1]-1) != obstruction:
                current = (current[0], current[1] - 1, 3)
            else:
                current = (current[0], current[1], 0)
                if current in result:
                    return False
                result.add(current)
    return True


def part2(data, path):
    result = 0
    current = find_start(data)
    data[current[0]][current[1]] = 0
    for coord in path:
        if not causes_loop(data, current, coord):
            result += 1
    return result


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1, path = part1(data)
    data = parse(puzzle_input)
    sol2 = part2(data, path)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)


run()
