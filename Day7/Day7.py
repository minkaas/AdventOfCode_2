import pathlib


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    directories = {}
    files = {}
    topdir = {}
    currentdir = ""
    for value in values:
        if "$ cd" in value:
            directory = value.split(" ")
            newdir = currentdir + "/" + directory[2]
            if directory[2] != ".." and newdir not in directories:
                directories[newdir] = []
                files[newdir] = []
                topdir[newdir] = currentdir
                currentdir = newdir
            elif directory[2] == "..":
                currentdir = topdir[currentdir]
            else:
                currentdir = currentdir + "/" + directory[1]
        elif "dir" in value:
            directory = value.split(" ")
            directories[currentdir].append(currentdir + "/" + directory[1])
        elif value.split(" ")[0].isdigit():
            filesize = value.split(" ")
            files[currentdir].append(int(filesize[0]))
    return directories, files


def getdirvalue(dir, depth, files, result):
    if len(depth[dir]) != 0:
        result[dir] = 0
        for directories in depth[dir]:
            result = getdirvalue(directories, depth, files, result)
        for directories in depth[dir]:
            result[dir] += result[directories]
        for file in files[dir]:
            result[dir] += file
    else:
        result[dir] = 0
        for file in files[dir]:
            result[dir] += file
    return result


def part1(depth, files):
    directorysizes = getdirvalue('//', depth, files, {})
    sum = 0
    for dirs in directorysizes:
        if directorysizes[dirs] <= 100000:
            sum += directorysizes[dirs]
    return sum


def part2(depth, files):
    directorysizes = getdirvalue('//', depth, files, {})
    sum = 0
    for dirs in directorysizes:
        sum += directorysizes[dirs]
    to_be_freed = directorysizes['//'] - 40000000
    possibledirs = []
    for dirs in directorysizes:
        if directorysizes[dirs] >= to_be_freed:
            possibledirs.append(directorysizes[dirs])
    return min(possibledirs)


def solve(puzzle_input):
    depth, files = parse(puzzle_input)
    sol1 = part1(depth, files)
    sol2 = part2(depth, files)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("input.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()

