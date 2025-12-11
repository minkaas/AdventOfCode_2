import pathlib
from time import time
from types import new_class


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = {}
    for value in values:
        devices, outputs = value.split(":")
        data[devices] = outputs.split()
    return data


def find_all_paths(data, path, start, end):
    path.append(start)
    result = 0
    if start == end:
        return 1
    else:
        for i in data[start]:
            result += find_all_paths(data, path, i, end)
    return result


def part1(data):
    result = find_all_paths(data, [], "you", "out")
    return result


def find_all_paths_visited(data, path, start, end, visited):
    path.append(start)
    visited.add(start)
    result = 0
    if start == end:
        result += 1
    else:
        if start not in data:
            path.pop()
            return 0, visited
        for i in data[start]:
            result += find_all_paths_visited(data, path, i, end, visited)[0]
    path.pop()
    return result, visited


def part2(data):
    result, visited = find_all_paths_visited(data, [], "dac", "out", set())
    for node in visited:
        if node in data:
            data.pop(node)
    print("done with dac to out")
    print(result)
    extra_result, visited = find_all_paths_visited(data, [], "fft", "dac", set())
    for node in visited:
        if node in data:
            data.pop(node)
    result *= extra_result
    print("done with fft to dac")
    print(result)
    extra_result, visited = find_all_paths_visited(data, [], "svr", "fft", set())
    result *= extra_result
    print("done with svr to fft")
    return result

def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    data = parse(puzzle_input)
    sol2 = part2(data)
    return sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
