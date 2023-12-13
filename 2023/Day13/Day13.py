import copy
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
    return list(map(list, zip(*matrix)))

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
        result += check_reflection(mirror) * 100
        mirror = transpose(mirror)
        result += check_reflection(mirror)
    return result


def check_if_off_by_one(pattern1, pattern2):
    count = 0
    new_pattern = copy.deepcopy(pattern1)
    for i in range(len(pattern1)):
        if pattern1[i] != pattern2[i]:
            new_pattern[i] = not pattern1[i]
            count += 1
    if count > 1:
        return (0, pattern1)
    if count == 0:
        return (1, pattern1)
    return (2, new_pattern)


def check_smudge(mirror):
    for i in range(1, len(mirror)):
        smudge_changed = False
        off_by_one, pat = check_if_off_by_one(mirror[i], mirror[i-1])
        if off_by_one:
            if off_by_one == 2:
                smudge_changed = True
            valid = True
            k = 2
            for j in range(i+1, len(mirror)):
                if i-k >= 0:
                    off_by_one, pat = check_if_off_by_one(mirror[j], mirror[i-k])
                    if valid and smudge_changed:
                        if off_by_one == 2 or not off_by_one:
                            valid = False
                    elif valid:
                        if not off_by_one:
                            valid = False
                    if off_by_one == 2:
                        smudge_changed = True
                k += 1
            if valid and smudge_changed:
                return i
    return 0

def part2(data):
    result = 0
    for mirror in data:
        hori = check_smudge(mirror)
        result += hori * 100
        mirror = transpose(mirror)
        vert = check_smudge(mirror)
        result += vert
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
