import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n\n")
    map_grid = []
    moves = []
    map_parts = values[0].split("\n")
    move_parts = values[1].split("\n")
    for value in map_parts:
        to_add = []
        for val in value:
            to_add.append(val)
        map_grid.append(to_add)
    for value in move_parts:
        for val in value:
            moves.append(val)
    return map_grid, moves


def find_boxes_and_start(map_grid):
    boxes = []
    start = (0,0)
    for i in range(0, len(map_grid)):
        for j in range(0, len(map_grid[i])):
            if map_grid[i][j] == 'O':
                boxes.append((i, j))
            elif map_grid[i][j] == '@':
                start = (i, j)
    return boxes, start


def do_move(current, move, boxes, map_grid):
    if move == '^':
        new_loc = (current[0] - 1, current[1])
        if new_loc in boxes:
            i = new_loc[0] - 1
            while i > 1 and (i, new_loc[1]) in boxes:
                i -= 1
            if (i, new_loc[1]) in boxes or map_grid[i][new_loc[1]] == '#':
                return current, boxes
            else:
                while i < new_loc[0]:
                    i += 1
                    box = boxes.pop(boxes.index((i, new_loc[1])))
                    box = (i - 1, box[1])
                    boxes.append(box)
        elif map_grid[new_loc[0]][new_loc[1]] == '#':
            return current, boxes
        return new_loc, boxes
    elif move == 'v':
        new_loc = (current[0] + 1, current[1])
        if new_loc in boxes:
            i = new_loc[0] + 1
            while i < len(map_grid) - 1 and (i, new_loc[1]) in boxes:
                i += 1
            if (i, new_loc[1]) in boxes or map_grid[i][new_loc[1]] == '#':
                return current, boxes
            else:
                while i > new_loc[0]:
                    i -= 1
                    box = boxes.pop(boxes.index((i, new_loc[1])))
                    box = (i + 1, box[1])
                    boxes.append(box)
        elif map_grid[new_loc[0]][new_loc[1]] == '#':
            return current, boxes
        return new_loc, boxes
    elif move == '>':
        new_loc = (current[0], current[1] + 1)
        if new_loc in boxes:
            i = new_loc[1] + 1
            while i < len(map_grid[0]) - 1 and (new_loc[0], i) in boxes:
                i += 1
            if (new_loc[0], i) in boxes or map_grid[new_loc[0]][i] == '#':
                return current, boxes
            else:
                while i > new_loc[1]:
                    i -= 1
                    box = boxes.pop(boxes.index((new_loc[0], i)))
                    box = (box[0], i + 1)
                    boxes.append(box)
        elif map_grid[new_loc[0]][new_loc[1]] == '#':
            return current, boxes
        return new_loc, boxes
    elif move == '<':
        new_loc = (current[0], current[1] - 1)
        if new_loc in boxes:
            i = new_loc[1] - 1
            while i > 1 and (new_loc[0], i) in boxes:
                i -= 1
            if (new_loc[0], i) in boxes or map_grid[new_loc[0]][i] == '#':
                return current, boxes
            while i < new_loc[1]:
                i += 1
                box = boxes.pop(boxes.index((new_loc[0], i)))
                box = (box[0], i - 1)
                boxes.append(box)
        elif map_grid[new_loc[0]][new_loc[1]] == '#':
            return current, boxes
        return new_loc, boxes
    return 0, 0


def part1(map_grid, moves):
    boxes, current = find_boxes_and_start(map_grid)
    result = 0
    for move in moves:
        current, boxes = do_move(current, move, boxes, map_grid)
        #print_grid(map_grid, boxes, current)
    for box in boxes:
        result += 100 * box[0] + box[1]
    return result


def print_grid(map_grid, boxes, current):
    for i in range(0, len(map_grid)):
        to_print = ""
        for j in range(0, len(map_grid[i])):
            if map_grid[i][j] == '#':
                to_print += '#'
            elif (i, j) in boxes:
                to_print += 'O'
            elif (i, j, j+1) in boxes:
                to_print += '['
            elif (i, j-1, j) in boxes:
                to_print += ']'
            elif (i, j) == current:
                to_print += '@'
            else:
                to_print += '.'
        print(to_print)


def widen(map_grid):
    new_map = []
    for i in range(0, len(map_grid)):
        to_add = []
        for j in range(0, len(map_grid[i])):
            if map_grid[i][j] == '#':
                to_add.append('#')
                to_add.append('#')
            elif map_grid[i][j] == 'O':
                to_add.append('[')
                to_add.append(']')
            elif map_grid[i][j] == '@':
                to_add.append('@')
                to_add.append('.')
            else:
                to_add.append('.')
                to_add.append('.')
        new_map.append(to_add)
    return new_map


def find_boxes_and_start2(map_grid):
    boxes = []
    start = (0,0)
    one_box = (0, 0, 0)
    for i in range(0, len(map_grid)):
        for j in range(0, len(map_grid[i])):
            if map_grid[i][j] == '[':
                one_box = (i, j, 0)
            elif map_grid[i][j] == ']':
                one_box = (one_box[0], one_box[1], j)
                boxes.append(one_box)
            elif map_grid[i][j] == '@':
                start = (i, j)
    return boxes, start


def do_wide_move(current, move, boxes, map_grid):
    if move == '^':
        new_loc = (current[0] - 1, current[1])
        if (new_loc[0], new_loc[1], new_loc[1] + 1) in boxes:
            if not can_push(True, (new_loc[0], new_loc[1], new_loc[1] + 1), boxes, map_grid):
                return current, boxes
            else:
                return new_loc, push_boxes(True, (new_loc[0], new_loc[1], new_loc[1] + 1), boxes)
        elif (new_loc[0], new_loc[1] - 1, new_loc[1]) in boxes:
            if not can_push(True, (new_loc[0], new_loc[1] -1, new_loc[1]), boxes, map_grid):
                return current, boxes
            else:
                return new_loc, push_boxes(True, (new_loc[0], new_loc[1] - 1, new_loc[1]), boxes)
        elif map_grid[new_loc[0]][new_loc[1]] == '#':
            return current, boxes
        return new_loc, boxes
    elif move == 'v':
        new_loc = (current[0] + 1, current[1])
        if (new_loc[0], new_loc[1], new_loc[1] + 1) in boxes:
            if not can_push(False, (new_loc[0], new_loc[1], new_loc[1] + 1), boxes, map_grid):
                return current, boxes
            else:
                return new_loc, push_boxes(False, (new_loc[0], new_loc[1], new_loc[1] + 1), boxes)
        elif (new_loc[0], new_loc[1] - 1, new_loc[1]) in boxes:
            if not can_push(False, (new_loc[0], new_loc[1] -1, new_loc[1]), boxes, map_grid):
                return current, boxes
            else:
                return new_loc, push_boxes(False, (new_loc[0], new_loc[1] - 1, new_loc[1]), boxes)
        elif map_grid[new_loc[0]][new_loc[1]] == '#':
            return current, boxes
        return new_loc, boxes
    elif move == '>':
        new_loc = (current[0], current[1] + 1)
        if (new_loc[0], new_loc[1], new_loc[1] + 1) in boxes:
            i = new_loc[1] + 2
            while i < len(map_grid[0]) - 2 and (new_loc[0], i, i+1) in boxes:
                i += 2
            if (new_loc[0], i, i+1) in boxes or map_grid[new_loc[0]][i] == '#':
                return current, boxes
            else:
                while i > new_loc[1]:
                    i -= 2
                    box = boxes.pop(boxes.index((new_loc[0], i, i+1)))
                    box = (box[0], i+1, i+2)
                    boxes.append(box)
        elif map_grid[new_loc[0]][new_loc[1]] == '#':
            return current, boxes
        return new_loc, boxes
    elif move == '<':
        new_loc = (current[0], current[1] - 1)
        if (new_loc[0], new_loc[1] - 1, new_loc[1]) in boxes:
            i = new_loc[1] - 2
            while i > 2 and (new_loc[0], i-1, i) in boxes:
                i -= 2
            if (new_loc[0], i-1, i) in boxes or map_grid[new_loc[0]][i] == '#':
                return current, boxes
            else:
                while i < new_loc[1]:
                    i += 2
                    box = boxes.pop(boxes.index((new_loc[0], i-1, i)))
                    box = (box[0], i-2, i-1)
                    boxes.append(box)
        elif map_grid[new_loc[0]][new_loc[1]] == '#':
            return current, boxes
        return new_loc, boxes
    return 0, 0


def can_push(up, box, boxes, map_grid):
    if up:
        coord = (box[0]-1, box[1], box[2])
    else:
        coord = (box[0]+1, box[1], box[2])
    if map_grid[coord[0]][coord[1]] == '#' or map_grid[coord[0]][coord[2]] == '#':
        return False
    elif coord in boxes:
        return can_push(up, coord, boxes, map_grid)
    elif (coord[0], coord[1] - 1, coord[1]) in boxes and (coord[0], coord[2], coord[2] + 1) in boxes:
        return can_push(up, (coord[0], coord[1] - 1, coord[1]), boxes, map_grid) and can_push(up, (
        coord[0], coord[2], coord[2] + 1), boxes, map_grid)
    elif (coord[0], coord[1] - 1, coord[1]) in boxes:
        return can_push(up, (coord[0], coord[1] - 1, coord[1]), boxes, map_grid)
    elif (coord[0], coord[2], coord[2] + 1) in boxes:
        return can_push(up, (coord[0], coord[2], coord[2] + 1), boxes, map_grid)
    return True


def push_boxes(direction, box, boxes):
    if direction:
        new = (box[0] - 1, box[1], box[2])
    else:
        new = (box[0] + 1, box[1], box[2])
    if new in boxes:
        boxes = push_boxes(direction, new, boxes)
    if (new[0], new[1] - 1, new[1]) in boxes:
        boxes = push_boxes(direction, (new[0], new[1] - 1, new[1]), boxes)
    if (new[0], new[2], new[2] + 1) in boxes:
        boxes = push_boxes(direction, (new[0], new[2], new[2] + 1), boxes)
    boxes.pop(boxes.index(box))
    boxes.append(new)
    return boxes


def part2(map_grid, moves):
    result = 0
    map_grid = widen(map_grid)
    boxes, current = find_boxes_and_start2(map_grid)
    for move in moves:
        current, boxes = do_wide_move(current, move, boxes, map_grid)
    for box in boxes:
        result += 100 * box[0] + box[1]
    return result


def solve(puzzle_input):
    map_grid, moves = parse(puzzle_input)
    sol1 = part1(map_grid, moves)
    sol2 = part2(map_grid, moves)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
