import pathlib


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        data.append([int(x) for x in list(value)])
    return data

def isvisible(matrix):
    visible = 0
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            done = False
            for k in range(0, 4):
                if not done and checkdirection(matrix, i, j, k, matrix[i][j]):
                    visible += 1
                    done = True
    return visible


def checkdirection(matrix, i, j, direction, og):
    if direction == 0:
        if j == 0:
            return True
        if matrix[i][j-1] < og:
            return checkdirection(matrix, i, j-1, 0, og)
        return False
    elif direction == 1:
        if j == len(matrix[0])-1:
            return True
        if matrix[i][j+1] < og:
            return checkdirection(matrix, i, j+1, 1, og)
        return False
    elif direction == 2:
        if i == len(matrix)-1:
            return True
        if matrix[i+1][j] < og:
            return checkdirection(matrix, i+1, j, 2, og)
        return False
    else:
        if i == 0:
            return True
        if matrix[i-1][j] < og:
            return checkdirection(matrix, i-1, j, 3, og)
        return False


def part1(data):
    visible = isvisible(data)
    edges = (len(data) + len(data[0])) * 2 - 4
    return visible + edges


def givescenicdirection(matrix, i, j, direction, og, score):
    if direction == 0:
        if j == 0:
            return score
        if matrix[i][j-1] < og:
            return givescenicdirection(matrix, i, j-1, 0, og, score + 1)
        return score + 1
    elif direction == 1:
        if j == len(matrix[0])-1:
            return score
        if matrix[i][j+1] < og:
            return givescenicdirection(matrix, i, j+1, 1, og, score + 1)
        return score + 1
    elif direction == 2:
        if i == len(matrix)-1:
            return score
        if matrix[i+1][j] < og:
            return givescenicdirection(matrix, i+1, j, 2, og, score + 1)
        return score + 1
    else:
        if i == 0:
            return score
        if matrix[i-1][j] < og:
            return givescenicdirection(matrix, i-1, j, 3, og, score + 1)
        return score + 1


def part2(matrix):
    scenicscore = []
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            score = []
            for k in range(0, 4):
                score.append(givescenicdirection(matrix, i, j, k, matrix[i][j], 0))
            mult = 1
            for value in score:
                mult *= value
            scenicscore.append(mult)
    return max(scenicscore)


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    sol2 = part2(data)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()