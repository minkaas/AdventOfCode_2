import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        data.append(value)
    return data


def add_to_loop(loop, current, direction, size):
    i, j = current
    if direction == "R" or direction == "0":
        for k in range(size):
            current = (i, j + k + 1)
            loop.append(current)
    if direction == "L" or direction == "2":
        for k in range(size):
            current = (i, j - k - 1)
            loop.append(current)
    if direction == "U" or direction == "3":
        for k in range(size):
            current = (i - k - 1, j)
            loop.append(current)
    if direction == "D" or direction == "1":
        for k in range(size):
            current = (i + k + 1, j)
            loop.append(current)
    return loop, current


def draw_grid(i, j, loop):
    for x in range(i+1):
        print_line = ""
        for y in range(j+1):
            if (x, y) in loop:
                print_line += "#"
            else:
                print_line += "."
        print(print_line)


def flood_fill(loop):
    queue = [(1, 1)]
    while len(queue) > 0:
        (x, y) = queue.pop(0)
        if (x, y) not in loop:
            queue.append((x+1, y))
            queue.append((x-1, y))
            queue.append((x, y+1))
            queue.append((x, y-1))
        loop.add((x, y))
    return loop


def part1(data):
    loop = [(0, 0)]
    current = (0, 0)
    for instruction in data:
        direction, size, color = instruction.split(" ")
        loop, current = add_to_loop(loop, current, direction, int(size))
    loop = set(loop)
    loop = flood_fill(loop)
    return len(set(loop))


def part2(data):
    loop = [(0, 0)]
    current = (0, 0)
    for instruction in data:
        not_need, not_need, hex = instruction.split(" ")
        list(hex).pop(0)
        direction = list(hex).pop()
        hex = hex[2::]
        hex = hex[:-1]
        size = int(hex, 16)
        loop, current = add_to_loop(loop, current, direction, size)
    loop = set(loop)
    loop = flood_fill(loop)
    return len(set(loop))


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    sol2 = part2(data)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("test").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
