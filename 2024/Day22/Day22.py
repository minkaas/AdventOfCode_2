import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        data.append(int(value))
    return data


def prune(number):
    return number % 16777216


def mix(result, number):
    return result ^ number

def stupid_solution(secret_num):
    value = secret_num * 64
    secret_num = prune(mix(value, secret_num))
    value = secret_num // 32
    secret_num = prune(mix(value, secret_num))
    value = secret_num * 2048
    secret_num = prune(mix(value, secret_num))
    return secret_num


def part1(secret_values):
    result = 0
    for val in range(0, len(secret_values)):
        for i in range(0, 2000):
            secret_values[val] = stupid_solution(secret_values[val])
    return sum(secret_values)



def calc_sequence_1(secret_num):
    numone = secret_num % 10
    numtwo = stupid_solution(secret_num)
    numthree = stupid_solution(numtwo)
    numfour = stupid_solution(numthree)
    sequences = []
    sequence = [numtwo % 10 - numone,numthree % 10 - numtwo % 10, numfour % 10 - numthree % 10]
    previous = numfour
    current = stupid_solution(previous)
    for i in range(0, 1996):
        sequence.append(current % 10 - previous % 10)
        sequences.append([i for i in sequence])
        sequence.pop(0)
        previous, current = current, stupid_solution(current)
    return sequences


def do_seq_test(secret_num, to_sequence):
    numone = secret_num % 10
    numtwo = stupid_solution(secret_num)
    numthree = stupid_solution(numtwo)
    numfour = stupid_solution(numthree)
    sequence = [numtwo % 10 - numone, numthree % 10 - numtwo % 10, numfour % 10 - numthree % 10]
    previous = numfour
    current = stupid_solution(previous)
    for i in range(0, 1996):
        sequence.append(current % 10 - previous % 10)
        if sequence == to_sequence:
            return current % 10
        sequence.pop(0)
        previous, current = current, stupid_solution(current)
    return 0


def part2(secret_nums, puzzle_input):
    result = 0
    sequences = (calc_sequence_1(secret_nums[0]))
    secret_nums = parse(puzzle_input)
    for sequence in sequences:
        temp = 0
        for num in secret_nums:
            temp += do_seq_test(num, sequence)
        secret_nums = parse(puzzle_input)
        result = max(temp, result)
    return result


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    data = parse(puzzle_input)
    sol2 = part2(data, puzzle_input)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
