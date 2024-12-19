import pathlib
from time import time


def parse(puzzle_input):
    tokens = []
    data = []
    values = puzzle_input.split("\n\n")
    for value in values[0].split(', '):
        tokens.append(value)
    for value in values[1].split('\n'):
        data.append(value)
    return tokens, data


def starts_with_token(line, tokens):
    result = []
    for token in tokens:
        if len(token) <= len(line):
            if token == line[:len(token)]:
                result.append(token)
    return result


def rgbw_lexer(data, tokens):
    possibles = starts_with_token(data, tokens)
    if data == '':
        return True
    if len(possibles) == 0:
        return False
    elif len(possibles) == 1:
        return rgbw_lexer(data[len(possibles[0]):], tokens)
    else:
        possible = False
        i = 0
        while not possible and i < len(possibles):
            if rgbw_lexer(data[len(possibles[i]):], tokens):
                return True
            i += 1
        return False


def part1(data, tokens):
    result = 0
    impossibles = []
    i = 0
    for dat in data:
        if rgbw_lexer(dat, tokens):
            result += 1
        else:
            impossibles.append(i)
        i += 1
    return result, impossibles


def rgbw_lexer_2(data, tokens, computed):
    result = 0
    possibles = starts_with_token(data, tokens)
    if data in computed:
        return computed[data]
    if data == '':
        return 1
    if len(possibles) == 0:
        return 0
    elif len(possibles) == 1:
        to_check = data[len(possibles[0]):]
        if to_check in computed:
            return computed[to_check]
        return rgbw_lexer_2(to_check, tokens, computed)
    else:
        i = 0
        while i < len(possibles):
            to_check = data[len(possibles[i]):]
            if to_check in computed:
                result += computed[to_check]
            else:
                temp = rgbw_lexer_2(to_check, tokens, computed)
                computed[to_check] = temp
                result += temp
            i += 1
        return result




def part2(data, tokens, impossibles):
    result = 0
    i = 0
    for dat in data:
        if i not in impossibles:
            result += rgbw_lexer_2(dat, tokens, {})
        i += 1
    return result


def solve(puzzle_input):
    tokens, data = parse(puzzle_input)
    sol1, impossibles = part1(data, tokens)
    sol2 = part2(data, tokens, impossibles)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
