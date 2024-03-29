import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    start = (0, 0)
    for i in range(len(values)):
        if i == 0:
            data.append((len(values[i]) + 2) * ["."])
        line = values[i]
        char_list = ["."]
        for j in range(len(line)):
            char_list.append(line[j])
            if (line[j]) == "S":
                start = (i + 1, j + 1)
        char_list.append(".")
        data.append(char_list)
    data.append((len(values[i]) + 2) * ["."])
    return data, start


def pipe_info(pipe):
    if pipe == "|":
        return [(1, 0), (-1, 0)]
    if pipe == "-":
        return [(0, -1), (0, 1)]
    if pipe == "L":
        return [(-1, 0), (0, 1)]
    if pipe == "J":
        return [(-1, 0), (0, -1)]
    if pipe == "7":
        return [(1, 0), (0, -1)]
    if pipe == "F":
        return [(1, 0), (0, 1)]
    else:
        return [(0, 0), (0, 0)]


def get_next(source, current, data):
    i, j, pipe = current
    x, y, source_pipe = source
    info = pipe_info(pipe)
    for (left, right) in info:
        if i + left == x and j + right == y:
            info.remove((left, right))
    (left, right) = info[0]
    next_pipe = data[i + left][j + right]

    return (i + left, j + right, next_pipe)


def get_pipe(data, start):
    result = []
    i, j = start
    top = data[i - 1][j]
    mid_left, mid_right = data[i][j - 1], data[i][j + 1]
    bot = data[i + 1][j]
    next_pipe = ()
    for (left, right) in pipe_info(top):
        if left == 1 and right == 0:
            next_pipe = (i-1, j, top)
    for (left, right) in pipe_info(mid_left):
        if left == 0 and right == 1:
            next_pipe = (i, j-1, mid_left)
    for (left, right) in pipe_info(mid_right):
        if left == 0 and right == -1:
            next_pipe = (i, j+1, mid_right)
    for (left, right) in pipe_info(bot):
        if left == -1 and right == 0:
            next_pipe = (i+1, j, bot)
    current_value = next_pipe[2]
    result.append((i, j, "S"))
    result.append(next_pipe)
    while current_value != "S":
        (i, j, pipe) = get_next(result[-2], result[-1], data)
        result.append((i, j, pipe))
        current_value = pipe
    return result[:-1]


def part1(pipe_data):
    return len(pipe_data) // 2


def part2(pipe_data, data):
    inside = False
    inside_count = 0
    turn = False
    turn_start = ""
    for i in range(1, len(data)-1):
        for j in range(1, len(data[0])-1):
            symbol = data[i][j]
            if (i, j, symbol) in pipe_data:
                if symbol == "|":
                    inside = not inside
                elif not turn and symbol == "F":
                    turn = True
                    turn_start = "F"
                elif not turn and symbol == "L":
                    turn = True
                    turn_start = "L"
                elif turn and symbol == "7":
                    turn = False
                    if turn_start == "L":
                        inside = not inside
                elif turn and symbol == "J":
                    turn = False
                    if turn_start == "F":
                        inside = not inside
            elif inside:
                inside_count += 1
    return inside_count


def solve(puzzle_input):
    data, start = parse(puzzle_input)
    pipe_data = get_pipe(data, start)
    sol1 = part1(pipe_data)
    sol2 = part2(pipe_data, data)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)


run()
