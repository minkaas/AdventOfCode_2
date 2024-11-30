import math
import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    data.append([9] * (len(values[0]) + 2))
    for value in values:
        new_line = [9]
        for val in value:
            new_line.append(int(val))
        new_line.append(9)
        data.append(new_line)
    data.append([9] * (len(values[0]) + 2))
    return data


def print_matrix(matrix):
    for m in matrix:
        print(m)



def get_neighbours(node, data):
    x = node[1]
    y = node[2]
    neighbours = []
    if x != 1:
        neighbours.append((data[x-1][y], x-1, y))
    if x != (len(data) - 2):
        neighbours.append((data[x+1][y], x+1, y))
    if y != 1:
        neighbours.append((data[x][y-1], x, y-1))
    if y != (len(data[0]) - 2):
        neighbours.append((data[x][y+1], x, y+1))
    return neighbours


def find_shortest(matrix, openList):
    closedList = []
    while len(openList):
        currentNode = sorted(openList).pop(0)
        closedList.append(currentNode)
        (heat, i, j) = currentNode
        if i == len(matrix) - 2 and j == len(matrix[0]) - 2:
            return closedList
        children = get_neighbours(currentNode, matrix)


def same_dir(bour, current, now_dir):
    (ha, i, j) = current
    (ah, k, l) = bour
    if i == k:
        if j < l:
            return now_dir == 0
        else:
            return now_dir == 1
    if j == l:
        if i < k:
            return now_dir == 3
        else:
            return now_dir == 2


def do_search(data, start, goal):
    to_explore = [start]
    cameFrom = {}
    best_score = {}
    best_score[start] = 0
    best_score[(-1, -1)] = math.inf
    fest_score = {}
    fest_score[start] = 0
    same_direction = 0
    prev_dir = 4 #0 is right, 1 is left, 2 is up, 3 is down, 4 is infinite or something
    while len(to_explore) != 0:
        current = (-1, -1)
        for i in range(0, len(to_explore)):
            if best_score[to_explore[i]] < best_score[current]:
                current = to_explore[i]
        to_explore.remove(current)
        if current == goal:
            return reconstruct_path(cameFrom, current, data)
        neighbours = get_neighbours(current, data)
        for bour in neighbours:
            if same_dir(bour, current, prev_dir):
                same_direction += 1
            if same_direction == 3:
                tent_score = best_score[current] + 1000000
                same_direction = 0
            else:
                tent_score = best_score[current] + bour[0]
            if bour not in best_score:
                cameFrom[bour] = current
                best_score[bour] = tent_score
                fest_score[bour] = tent_score + 1
                if tent_score < 1000000:
                    to_explore.append(bour)
            elif best_score[bour] >= tent_score:
                cameFrom[bour] = current
                best_score[bour] = tent_score
                fest_score[bour] = tent_score + 1
                if bour not in to_explore:
                    to_explore.append(bour)
    return 0



def reconstruct_path(came_from, current, data):
    result_path = []
    result = 0
    while current in came_from.keys():
        result_path.insert(0, current)
        result += current[0]
        current = came_from[current]
    return result



def part1(data):
    result = 0
    print_matrix(data)
    return do_search(data, (data[1][1], 1, 1), (data[len(data)-2][len(data[0])-2], len(data) - 2, len(data[0])-2))


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
