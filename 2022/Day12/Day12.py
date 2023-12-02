import math
import pathlib


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        temp = []
        for letter in value:
            temp.append(ord(letter))
        data.append(temp)
    for i in range(0, len(data)):
        if ord('S') in data[i]:
            start = (i, data[i].index((ord('S'))))
        if ord('E') in data[i]:
            goal = (i, data[i].index((ord('E'))))
    data[start[0]][start[1]] = ord('a')
    data[goal[0]][goal[1]] = ord('z')
    return data, start, goal


def part1(data, start, goal):
    to_explore = [start]
    cameFrom = {}
    best_score = {}
    best_score[start] = 0
    best_score[(-1, -1)] = math.inf
    fest_score = {}
    fest_score[start] = 0
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
            if data[bour[0]][bour[1]] - data[current[0]][current[1]] > 1:
                tent_score = best_score[current] + 1000000
            else:
                tent_score = best_score[current] + 1
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


def get_neighbours(node, data):
    x = node[0]
    y = node[1]
    neighbours = []
    if x != 0:
        neighbours.append((x-1, y))
    if x != (len(data) - 1):
        neighbours.append((x+1, y))
    if y != 0:
        neighbours.append((x, y-1))
    if y != (len(data[0]) - 1):
        neighbours.append((x, y+1))
    return neighbours


def reconstruct_path(came_from, current, data):
    result_path = []
    while current in came_from.keys():
        result_path.insert(0, current)
        current = came_from[current]
    return len(result_path)


def part2(data, goal):
    result = []
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if data[i][j] == 97:
                length = part1(data, (i, j), goal)
                if length != 0:
                    result.append(length)
    return min(result)


def solve(puzzle_input):
    data, start, goal = parse(puzzle_input)
    sol1 = part1(data, start, goal)
    sol2 = part2(data, goal)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()
