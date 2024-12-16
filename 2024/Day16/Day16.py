import math
import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        temp = []
        for val in value:
            if val == '#':
                temp.append(0)
            elif val == '.':
                temp.append(1)
            elif val == 'S':
                temp.append(2)
            elif val == 'E':
                temp.append(3)
        data.append(temp)
    return data


def print_grid(data):
    for i in range(0, len(data)):
        to_print = ""
        for j in range(0, len(data[i])):
            if data[i][j] == 0:
                to_print += '#'
            elif data[i][j] == 1:
                to_print += '.'
            elif data[i][j] == 2:
                to_print += 'S'
            elif data[i][j] == 3:
                to_print += 'E'
            elif data[i][j] == 4:
                to_print += '@'
        print(to_print)


def find_start_end(data):
    start, end = (0, 0), (0, 0)
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if data[i][j] == 2:
                start = (i, j)
            elif data[i][j] == 3:
                end = (i, j)
    return start, end


def get_neighbours(current, data):
    neighbours = []
    look_around = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 0 north 1 east 2 south 3 west
    for look in look_around:
        new = tuple(map(sum, zip(current, look)))
        if data[new[0]][new[1]] != 0:
            neighbours.append(new)
    return neighbours


def do_search(data, start, goal):
    look_around = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 0 north 1 east 2 south 3 west
    to_explore = [start]
    cameFrom = {}
    best_score = {}
    best_score[start] = 0
    best_score[(-1, -1)] = math.inf
    direction = {}
    direction[start] = 1
    while len(to_explore):
        current = (-1, -1)
        for i in range(0, len(to_explore)):
            if best_score[to_explore[i]] < best_score[current]:
                current = to_explore[i]
        to_explore.remove(current)
        if current == goal:
            dir = look_around.index((cameFrom[current][0] - current[0], cameFrom[current][1] - current[1]))
            return reconstruct_path(cameFrom, current, dir)
        neighbours = get_neighbours(current, data)
        for bour in neighbours:
            dir = look_around.index((bour[0] - current[0], bour[1] - current[1]))
            if direction[current] != dir:
                tent_score = best_score[current] + 1001
            else:
                tent_score = best_score[current] + 1
            direction[bour] = dir
            if bour not in best_score:
                cameFrom[bour] = current
                best_score[bour] = tent_score
                to_explore.append(bour)
            elif best_score[bour] >= tent_score:
                cameFrom[bour] = current
                best_score[bour] = tent_score
                if bour not in to_explore:
                    to_explore.append(bour)


def part1(data):
    start, end = find_start_end(data)
    result, result_path = do_search(data, start, end)
    return result


def reconstruct_path(cameFrom, current, current_direction):
    result_path = []
    result = 0
    look_around = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 0 north 1 east 2 south 3 west
    while current in cameFrom.keys():
        result_path.insert(0, current)
        new = cameFrom[current]
        if look_around.index((current[0] - new[0], current[1] - new[1])) != current_direction:
            result += 1001
            current_direction = look_around.index((current[0] - new[0], current[1] - new[1]))
        else:
            result += 1
        current = new
    return result, result_path


def do_search_all(path, data, start, goal, supposed, turns, score_data):
    to_explore = [start]
    current_path = []
    if turns > supposed[1]:
        return [], score_data
    for i in path:
        current_path.append(i)
    if len(current_path) > supposed[0]:
        return [], score_data
    current_path.append(start)
    paths = []
    while len(to_explore) > 0:
        current = to_explore.pop(0)
        if calc_score(current_path) <= score_data[current[0]][current[1]]:
            score_data[current[0]][current[1]] = calc_score(current_path) + 1000
        else:
            return [], score_data
        if current == goal:
            if (len(current_path) - 1) == supposed[0]:
                paths.append(current_path)
                return paths, score_data
        neighbours = get_neighbours(current, data)
        if len(current_path) > 1:
            neighbours.remove(current_path[len(current_path) - 2])
        if len(neighbours) == 1:
            if neighbours[0] not in current_path:
                if len(current_path) > 1 and get_direction(current_path[len(current_path) - 1], neighbours[0]) != get_direction(current_path[len(current_path) - 2], current_path[len(current_path) - 1]):
                    turns += 1
                elif len(current_path) == 1 and get_direction(current_path[len(current_path)-1], neighbours[0]) != 1:
                    turns += 1
                current_path.append(neighbours[0])
                to_explore.append(neighbours[0])
        else:
            for bour in neighbours:
                if bour not in current_path:
                    temp_path = current_path
                    if len(current_path) == 1:
                        if get_direction(current_path[0], bour) == 1:
                            new_paths, score_data = do_search_all(temp_path, data, bour, goal, supposed, turns, score_data)
                            paths.extend(score_data)
                        else:
                            new_paths, score_data = do_search_all(temp_path, data, bour, goal, supposed, turns + 1, score_data)
                            paths.extend(new_paths)
                    else:
                        if get_direction(current_path[len(current_path)-1], bour) != get_direction(current_path[len(current_path)-2], current_path[len(current_path)-1]):
                            new_paths, score_data = do_search_all(temp_path, data, bour, goal, supposed, turns + 1, score_data)
                            paths.extend(new_paths)
                        else:
                            new_paths, score_data = do_search_all(temp_path, data, bour, goal, supposed, turns, score_data)
                            paths.extend(new_paths)
    return paths, score_data


def get_direction(one, two):
    look_around = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 0 north 1 east 2 south 3 west
    return look_around.index((two[0]-one[0], two[1]-one[1]))


def calc_score(path):
    look_around = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 0 north 1 east 2 south 3 west
    direction = 1
    score = 0
    for i in range(1, len(path)):
        one = path[i-1]
        two = path[i]
        dir = look_around.index((two[0]-one[0], two[1]-one[1]))
        if dir == direction:
            score += 1
        else:
            score += 1001
            direction = dir
    return score


def part2(data):
    start, end = find_start_end(data)
    score, best_path = do_search(data, start, end)
    good_length = len(best_path)
    turns = (score - good_length) // 1000
    score_data = []
    for i in range(0, len(data)):
        score_data.append([math.inf] * len(data[i]))
    paths, temp = do_search_all([], data, start, end, (good_length, turns), 0, score_data)
    all_coords = []
    print_grid(data)
    for path in paths:
        if (len(path)-1) == good_length:
            path_score = calc_score(path)
            if score == path_score:
                all_coords.extend(path)
    all_coords = list(set(all_coords))
    return len(all_coords)


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
