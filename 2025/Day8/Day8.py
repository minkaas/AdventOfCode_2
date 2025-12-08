import pathlib
from time import time
import math
import numpy as np

def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        x, y, z = value.split(",")
        data.append((int(x), int(y), int(z)))
    return data


def box_distance(box1, box2):
    return math.sqrt(abs(box1[0] - box2[0])**2 + abs(box1[1] - box2[1])**2 + abs(box1[2] - box2[2])**2)


def part1(data):
    circuits = []
    all_distances = []
    in_circuit = [0]*len(data)
    for i in range(0, len(data)):
        distance_temp = [math.inf]*(i+1)
        for j in range(i + 1, len(data)):
            box1 = data[i]
            box2 = data[j]
            distance_temp.append(box_distance(box1, box2))
        all_distances.append(distance_temp)
    all_distances = np.array(all_distances)
    connections_made = 0
    while connections_made < 1000:
        closest = all_distances.min()
        box1 = np.where(all_distances == closest)[0][0]
        box2 = np.where(all_distances == closest)[1][0]
        all_distances[box1][box2] = math.inf
        if in_circuit[box1] == 0 and in_circuit[box2] == 1:
            in_circuit[box1] = 1
            for i in range(0, len(circuits)):
                if data[box2] in circuits[i]:
                    break
            circuits[i].append(data[box1])
            # connections_made += 1
        elif in_circuit[box1] == 1 and in_circuit[box2] == 0:
            in_circuit[box2] = 1
            i = 0
            for circuit in range(0, len(circuits)):
                if data[box1] in circuits[circuit]:
                    i = circuit
                    break
            circuits[i].append(data[box2])
            # connections_made += 1
        elif in_circuit[box1] == 0 and in_circuit[box2] == 0:
            in_circuit[box1] = 1
            in_circuit[box2] = 1
            circuits.append([data[box1], data[box2]])
            # connections_made += 1
        elif in_circuit[box1] == 1 and in_circuit[box2] == 1:
            needed_index = 0
            for i in range(0, len(circuits)):
                if data[box1] in circuits[i]:
                    needed_index = i
                    break
            if data[box2] not in circuits[needed_index]:
                for k in range(0, len(circuits)):
                    if data[box2] in circuits[k]:
                        break
                circuits[needed_index] += circuits[k]
                circuits.pop(k)
        connections_made += 1
    temp = []
    for circuit in circuits:
        temp.append(len(circuit))
    temp = list(reversed(sorted(temp)))
    return temp[0] * temp[1] * temp[2]


def part2(data):
    circuits = []
    all_distances = []
    in_circuit = [0]*len(data)
    for i in range(0, len(data)):
        distance_temp = [math.inf]*(i+1)
        for j in range(i + 1, len(data)):
            box1 = data[i]
            box2 = data[j]
            distance_temp.append(box_distance(box1, box2))
        all_distances.append(distance_temp)
    all_distances = np.array(all_distances)
    connections_made = 0
    circuits.append([data[0]])
    circuits.append([data[1]])
    in_circuit[0] = 1
    in_circuit[1] = 1
    while len(circuits) > 1:
        closest = all_distances.min()
        box1 = np.where(all_distances == closest)[0][0]
        box2 = np.where(all_distances == closest)[1][0]
        all_distances[box1][box2] = math.inf
        if in_circuit[box1] == 0 and in_circuit[box2] == 1:
            in_circuit[box1] = 1
            for i in range(0, len(circuits)):
                if data[box2] in circuits[i]:
                    break
            circuits[i].append(data[box1])
            # connections_made += 1
        elif in_circuit[box1] == 1 and in_circuit[box2] == 0:
            in_circuit[box2] = 1
            i = 0
            for circuit in range(0, len(circuits)):
                if data[box1] in circuits[circuit]:
                    i = circuit
                    break
            circuits[i].append(data[box2])
            # connections_made += 1
        elif in_circuit[box1] == 0 and in_circuit[box2] == 0:
            in_circuit[box1] = 1
            in_circuit[box2] = 1
            circuits.append([data[box1], data[box2]])
            # connections_made += 1
        elif in_circuit[box1] == 1 and in_circuit[box2] == 1:
            needed_index = 0
            for i in range(0, len(circuits)):
                if data[box1] in circuits[i]:
                    needed_index = i
                    break
            if data[box2] not in circuits[needed_index]:
                for k in range(0, len(circuits)):
                    if data[box2] in circuits[k]:
                        break
                circuits[needed_index] += circuits[k]
                circuits.pop(k)
        connections_made += 1
    return data[box1][0] * data[box2][0]


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    data = parse(puzzle_input)
    sol2 = part2(data)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
