import math
import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n\n")
    data = {}
    instructions = values[0]
    values = values[1].split("\n")
    for value in values:
        start, next = value.split(" = ")[0], value.split(" = ")[1]
        left, right = next.split(", ")[0], next.split(", ")[1]
        data[start] = (left[1:], right[:3])
    return instructions, data


def get_next(ins, data, current):
    left, right = data[current]
    if ins == "R":
        return right
    else:
        return left


def part1(instructions, data):
    result = 0
    current = "AAA"
    i = 0
    while current != "ZZZ":
        inst = instructions[i]
        current = get_next(inst, data, current)
        result += 1
        i = (i + 1) % len(instructions)
    return result


def part2(instructions, data):
    current_nodes = get_all(data)
    node_loops = []
    for node in current_nodes:
        node_loops.append(get_steps(node, data, instructions))
    # calculate how many steps it takes for them to get into a 'Z' state
    # then get the lowest common multiple of those steps
    # no I totally did not get the lcm code from a random stackoverflow page
    lcm = 1
    for i in node_loops:
        lcm = lcm*i//math.gcd(lcm, i)
    return lcm


def get_steps(node, data, instructions):
    result = 0
    i = 0
    while node[-1] != "Z":
        inst = instructions[i]
        node = get_next(inst, data, node)
        result += 1
        i = (i + 1) % len(instructions)
    return result


def get_all(data):
    result = []
    for keys in data:
        if keys[2] == "A":
            result.append(keys)
    return result


def solve(puzzle_input):
    instructions, data = parse(puzzle_input)
    sol1 = part1(instructions, data)
    sol2 = part2(instructions, data)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)


run()
