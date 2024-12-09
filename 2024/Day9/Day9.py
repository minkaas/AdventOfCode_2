import copy
import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    counter = 0
    duo = (0, 0)
    for value in values[0]:
        if counter % 2 == 0:
            duo = (int(value), duo[1])
            counter += 1
        else:
            duo = (duo[0], int(value))
            counter += 1
            data.append(duo)
    data.append((int(values[0][-1]), 0))
    return data


def part1(data):
    result = 0
    placement = 0
    i = 0
    while i < len(data):
        for j in range(0, data[i][0]):
            result += placement * i
            placement += 1
        last_id = len(data) - 1
        done = False
        if last_id == i:
            done = True
        while not done:
            if data[last_id][0] > data[i][1]:
                for j in range(0, data[i][1]):
                    result += placement * last_id
                    placement += 1
                data[last_id] = (data[last_id][0] - data[i][1], data[last_id][1])
                done = True
            elif data[last_id][0] == data[i][1]:
                data.pop()
                for j in range(0, data[i][1]):
                    result += placement * last_id
                    placement += 1
                last_id -= 1
                done = True
            elif data[last_id][0] < data[i][1]:
                last_value = data.pop()
                for j in range(0, last_value[0]):
                    result += placement * last_id
                    placement += 1
                last_id -= 1
                data[i] = (data[i][0], data[i][1] - last_value[0])
        i += 1
    return result


def part2(data):
    result = 0
    placement = 0
    change = True
    for i in range(0, len(data)):
        data[i] = (data[i][0], data[i][1], i)
    last_changed = data[-1][2]
    first_room = 0
    while change:
        change = False
        for i in range(last_changed, -1, -1):
            for j in range(first_room, i):
                if data[j][1] >= data[i][0]:
                    data[i-1] = (data[i-1][0], data[i-1][1] + data[i][0] + data[i][1], data[i-1][2])
                    data.insert(j+1, (data[i][0], data[j][1] - data[i][0], data[i][2]))
                    data[j] = (data[j][0], 0, data[j][2])
                    data.pop(i+1)
                    change = True
                    break
            while data[first_room][1] == 0:
                first_room += 1
            if not change:
                last_changed -= 1
            if change:
                break
    for i in data:
        for j in range(0, i[0]):
            result += i[2] * placement
            placement += 1
        for j in range(0, i[1]):
            placement += 1
    return result


def solve(puzzle_input):
    data = parse(puzzle_input)
    data_again = copy.deepcopy(data)
    sol1 = part1(data)
    sol2 = part2(data_again)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
