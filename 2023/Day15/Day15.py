import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split(",")
    data = []
    for value in values:
        data.append(value)
    return data


def mult_and_mod(current_value):
    return current_value * 17 % 256


def part1(data):
    result = 0
    for dat in data:
        current_value = 0
        for char in dat:
            current_value += ord(char)
            current_value = mult_and_mod(current_value)
        result += current_value
    return result


def part2(data):
    hashmap = {}
    for i in range(256):
        hashmap[i] = []
    for step in data:
        current_value = 0
        if "=" in step:
            label, focal = step.split("=")
            for chara in label:
                current_value += ord(chara)
                current_value = mult_and_mod(current_value)
            lenses = hashmap[current_value]
            replaced = False
            for i in range(len(lenses)):
                if lenses[i][0] == label:
                    lenses[i] = (label, focal)
                    replaced = True
            if not replaced:
                hashmap[current_value].append((label, focal))
        else:
            label = step.split("-")[0]
            for chara in label:
                current_value += ord(chara)
                current_value = mult_and_mod(current_value)
            lenses = hashmap[current_value]
            to_remove = -1
            for i in range(len(lenses)):
                if lenses[i][0] == label:
                    to_remove = i
            if to_remove != -1:
                lenses.pop(to_remove)
    return calc_focusingpower(hashmap)


def calc_focusingpower(hashmap):
    result = 0
    for i in range(len(hashmap)):
        lenses = hashmap[i]
        for j in range(len(lenses)):
            result += (i+1) * (j+1) * int(lenses[j][1])
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
