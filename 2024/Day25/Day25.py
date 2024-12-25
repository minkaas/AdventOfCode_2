import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n\n")
    keys = []
    locks = []
    for value in values:
        value = value.split("\n")
        key = False
        lock = False
        this_key = []
        this_lock = []
        for val in value:
            if not key and not lock:
                if val == '#####':
                    key = True
                else:
                    lock = True
            else:
                temp = []
                for v in val:
                    if v == '#':
                        temp.append(1)
                    else:
                        temp.append(0)
                if key:
                    this_key.append(temp)
                else:
                    this_lock.append(temp)
        if key:
            keys.append(transpose(this_key))
        else:
            locks.append(transpose(this_lock))
    return keys, locks


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def part1(keys, locks):
    result = 0
    for lock in locks:
        for key in keys:
            fit = True
            for i in range(0, len(lock)):
                if sum(lock[i]) + sum(key[i]) > 6:
                    fit = False
            if fit:
                result += 1
    return result


def part2(data):
    result = 0
    return result


def solve(puzzle_input):
    keys, locks = parse(puzzle_input)
    sol1 = part1(locks, keys)
    sol2 = part2(keys)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
