import pathlib
from time import time
import math

def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    i = 0
    start = (0,0)
    end = (0, 0)
    for value in values:
        j = 0
        to_add = []
        for val in value:
            if val == '#':
                to_add.append(-1)
            elif val == '.':
                to_add.append(0)
            elif val == 'S':
                start = (i, j)
                to_add.append(0)
            elif val == 'E':
                end = (i, j)
                to_add.append(0)
            j += 1
        data.append(to_add)
        i += 1
    return data, start, end

def reconstruct_path(cameFrom, current):
    result_path = []
    while current in cameFrom.keys():
        result_path.insert(0, current)
        current = cameFrom[current]
    return result_path


def get_neighbours(current, data):
    look_around = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 0 north 1 east 2 south 3 west
    bours = []
    for look in look_around:
        new = tuple(map(sum, zip(current, look)))
        if data[new[0]][new[1]] != -1:
            bours.append(new)
    return bours


def find_path(data, start, end):
    to_explore = [start]
    cameFrom = {}
    best_score = {}
    best_score[start] = 0
    best_score[(-1, -1)] = 100000000000
    while len(to_explore):
        current = (-1, -1)
        for i in range(0, len(to_explore)):
            if best_score[to_explore[i]] < best_score[current]:
                current = to_explore[i]
        to_explore.remove(current)
        if current == end:
            return reconstruct_path(cameFrom, current)
        neighbours = get_neighbours(current, data)
        for bour in neighbours:
            if bour not in best_score:
                cameFrom[bour] = current
                best_score[bour] = best_score[current] + 1
                to_explore.append(bour)
            elif best_score[bour] >= best_score[current] + 1:
                cameFrom[bour] = current
                best_score[bour] = best_score[current] + 1
                if bour not in to_explore:
                    to_explore.append(bour)


def part1(data, start, end):
    result = try_cheats(data, start, end, 2)
    return result


def get_wall_neighbours(current, data):
    look_around = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 0 north 1 east 2 south 3 west
    bours = []
    for look in look_around:
        new = tuple(map(sum, zip(current, look)))
        if new[0] != -1 and new[0] != len(data) - 1 and new[1] != -1 and new[1] != len(data[0]) - 1:
            if data[new[0]][new[1]] == -1:
                bours.append(new)
    return bours


def do_cheat(current, cheat_left, og_left, data, start_road, scores, cheat_path):
    cheat_path.append(current)
    normals = get_neighbours(current, data)
    result = 0
    if cheat_left == 1:
        for norm in normals:
            if scores[start_road] - scores[norm] - og_left >= 100:
                result += 1
        return result
    return result


def try_cheats(data, start, end, cheat_length):
    result = 0
    the_path = find_path(data, start, end)
    the_path.insert(0, start)
    the_path_scores = {}
    for i in range(0, len(the_path)):
        the_path_scores[the_path[i]] = i
    for i in range(0, len(the_path)):
        current = the_path[i]
        bours = get_wall_neighbours(current, data)
        for bour in bours:
            result += do_cheat(bour, cheat_length - 1, cheat_length, data, current, the_path_scores, [current])
    return result


def eucledian(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
    # return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def part2(data, start, end):
    result = 0
    the_path = find_path(data, start, end)
    the_path.insert(0, start)
    the_path_scores = {}
    for i in range(0, len(the_path)):
        the_path_scores[the_path[i]] = i
    for i in range(0, len(the_path)):
        coord = the_path[i]
        for j in range(i + 1, len(the_path)):
            coord2 = the_path[j]
            if eucledian(coord, coord2) <= 20:
                if the_path_scores[coord2] - eucledian(coord, coord2) - the_path_scores[coord] >= 100:
                    result += 1
    return result


def solve(puzzle_input):
    data, start, end = parse(puzzle_input)
    sol1 = part1(data, start, end)
    sol2 = part2(data, start, end)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
