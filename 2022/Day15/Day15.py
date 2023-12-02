import math
import pathlib
import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    sensors = []
    beacons = []
    highest_x = 0
    lowest_x = math.inf
    for value in values:
        value = value.split(":")
        sensor_x = int(value[0].split()[2].split(",")[0].split("=")[1])
        sensor_y = int(value[0].split()[3].split("=")[1])
        beacon_x = int(value[1].split()[4].split(",")[0].split("=")[1])
        beacon_y = int(value[1].split()[5].split("=")[1])
        sensor = (sensor_x, sensor_y)
        beacon = (beacon_x, beacon_y)
        highest_x = max(beacon_x, sensor_x, highest_x)
        lowest_x = min(beacon_x, sensor_x, lowest_x)
        sensors.append(sensor)
        beacons.append(beacon)
    return sensors, beacons, highest_x, lowest_x


def manhattan_calc(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])


def part1(sensors, beacons, highest_x, lowest_x):
    row_to_check = 2000000
    manhat_dist = []
    not_possible = 0
    for i in range(0, len(sensors)):
        manhat_dist.append(manhattan_calc(sensors[i], beacons[i]))
    for i in range(lowest_x-2000000, highest_x+2000000):
        possible_beacon = (i, row_to_check)
        possible = False
        for j in range(0, len(sensors)):
            if not possible and manhattan_calc(possible_beacon, sensors[j]) <= manhat_dist[j]:
                possible = True
        if possible_beacon not in beacons:
            not_possible += possible
    return not_possible


def add_all_impossible(sensor_pos, man_hat):
    tempset = set()
    sensor_x = sensor_pos[0]
    sensor_y = sensor_pos[1]
    for x in range(0, man_hat+1):
        for y in range(0, man_hat+1):
            if x + y <= man_hat:
                tempset.add((sensor_x+x, sensor_y+y))
                tempset.add((sensor_x-x, sensor_y+y))
                tempset.add((sensor_x+x, sensor_y-y))
                tempset.add((sensor_x-x, sensor_y-y))
    return tempset


def part2(sensors, beacons):
    covered = set(sensors).union(set(beacons))
    starttime = time.time()
    for i in range(0, len(sensors)):
        manhat_dist = manhattan_calc(sensors[i], beacons[i])
        covered = covered.union(add_all_impossible(sensors[i], manhat_dist))
        print("Done with covered " + str(time.time()-starttime))
    for x in range(0, 4000001):
        for y in range(0, 4000001):
            if y == 4000000:
                print("at x=" + str(x) + " so far it has taken " + str(time.time()-starttime) + " seconds")
            if (x, y) not in covered:
                return x*4000000 + y
    return 0


def solve(puzzle_input):
    sensors, beacons, highest_x, lowest_x = parse(puzzle_input)
    sol1 = 0 #part1(sensors, beacons, highest_x, lowest_x)
    sol2 = part2(sensors, beacons)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()
