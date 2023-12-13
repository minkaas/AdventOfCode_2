import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n\n")
    data = []
    for value in values:
        value = value.split("\n")
        mirror = []
        for val in value:
            char_list = []
            for character in val:
                if character == ".":
                    char_list.append(False)
                else:
                    char_list.append(True)
            mirror.append(char_list)
        data.append(mirror)
    return data


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def check_reflection(mirror):
    for i in range(1, len(mirror)):
        if mirror[i] == mirror[i - 1]:
            valid = True
            k = 1
            for j in range(i, len(mirror)):
                if i-k >= 0:
                    if valid and mirror[j] != mirror[i-k]:
                        valid = False
                k += 1
            if valid:
                return i
    return 0


def part1(data):
    result = 0
    for mirror in data:
        horizontal_ref = check_reflection(mirror)
        print(horizontal_ref)
        result += horizontal_ref * 100
        mirror = transpose(mirror)
        vert_ref = check_reflection(mirror)
        print(vert_ref)
        result += vert_ref
    return result


def part2(data):
    result = 0
    return result


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
