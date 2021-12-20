#!/bin/python
import json
import math
import sys
from copy import deepcopy

datadir = "data"


def get_data_as_string(day):
    """Return the data for day as a string."""
    f = open(f"{datadir}/{day}.txt")
    return f.read()


def get_data_as_list(day):
    f = open(f"{datadir}/{day}.txt")
    return f.read().split("\n")


#
# Day 1
#
def day1a():
    day = "day1a"
    print(f"Running {day}...")
    data = get_data_as_list(day)

    increased = 0
    decreased = 0
    same = 0

    last = int(data[0])
    print(f"\n{last} (N/A - no previous measurement)")
    for depth in data[1:]:
        depth = int(depth)
        if depth < last:
            decreased += 1
            print(f"{depth} (decreased)")
        elif depth > last:
            increased += 1
            print(f"{depth} (increased)")
        else:
            same += 1
            print(f"{depth} (no change)")
        last = depth

    print(f"\nIncreased: {increased}")
    print(f"Decreased: {decreased}")
    print(f"Same: {same}")


def day1b():
    day = "day1b"
    print(f"Running {day}...")
    data = get_data_as_list(day)
    windows = []

    n = 0
    while n < (len(data) - 2):
        a = int(data[n])
        b = int(data[n + 1])
        c = int(data[n + 2])
        window = sum([a, b, c])
        windows.append(window)
        n += 1

    for window in windows:
        print(window)

    increased = 0
    decreased = 0
    same = 0

    last = int(windows[0])
    print(f"\n{last} (N/A - no previous sum)")
    for depthsum in windows[1:]:
        depthsum = int(depthsum)
        if depthsum < last:
            decreased += 1
            print(f"{depthsum} (decreased)")
        elif depthsum > last:
            increased += 1
            print(f"{depthsum} (increased)")
        else:
            same += 1
            print(f"{depthsum} (no change)")
        last = depthsum

    print(f"\nIncreased: {increased}")
    print(f"Decreased: {decreased}")
    print(f"Same: {same}")
#
# Day 2
#
def day2a():
    day = "day2a"
    print(f"Running {day}...")
    data = get_data_as_list(day)
    x = 0
    y = 0
    for row in data:
        direction, dist = row.split(" ")
        if direction == "forward":
            x += int(dist)
        elif direction == "down":
            y += int(dist)
        elif direction == "up":
            y -= int(dist)
        else:
            print(f"UNKNOWN DIRECTION: {direction}")

    print(f"Location: horizontal {x}, depth {y}")
    diag = x * y
    print(f"Diagonal: {diag}")

def day2b():
    day = "day2b"
    print(f"Running {day}...")
    data = get_data_as_list(day)
    aim = 0
    x = 0
    y = 0
    for row in data:
        direction, dist = row.split(" ")
        if direction == "forward":
            x += int(dist)
            y += (int(dist) * aim)
        elif direction == "down":
            aim += int(dist)
        elif direction == "up":
            aim -= int(dist)
        else:
            print(f"UNKNOWN DIRECTION: {direction}")

    print(f"Location: horizontal {x}, depth {y}")
    diag = x * y
    print(f"Diagonal: {diag}")


#
# Day 3
#
def day3a():
    day = "day3a"
    print(f"Running {day}...")
    data = get_data_as_list(day)

    def get_gamma():
        ex = data[0]
        n = 0

        gamma = ""

        while n < len(ex):
            # check the nth character of the string
            zeros = 0
            ones = 0
            for row in data:
                char = row[n]
                if char == "0":
                    zeros += 1
                elif char == "1":
                    ones += 1
            if zeros > ones:
                gamma += "0"
            elif ones > zeros:
                gamma += "1"

            n += 1

        return gamma

    def get_epsilon():
        ex = data[0]
        n = 0

        epsilon = ""

        while n < len(ex):
            # check the nth character of the string
            zeros = 0
            ones = 0
            for row in data:
                char = row[n]
                if char == "0":
                    zeros += 1
                elif char == "1":
                    ones += 1
            if zeros > ones:
                epsilon += "1"
            elif ones > zeros:
                epsilon += "0"

            n += 1

        return epsilon


    gamma = get_gamma()
    print(f"Gamma: {gamma} ({int(gamma, 2)})")

    epsilon = get_epsilon()
    print(f"Epsilon: {epsilon} ({int(epsilon, 2)})")

    answer = int(gamma, 2) * int(epsilon, 2)
    print(f"Answer: {answer}")


def day3b():
    day = "day3b"
    print(f"Running {day}...")
    data = get_data_as_list(day)

    def get_oxygen_generator_rating():
        ex = data[0]
        n = 0

        oxygen = ""
        candidates = list(data)
        while n < len(ex):
            # check the nth character of the string
            zeros = 0
            ones = 0
            for row in candidates:
                char = row[n]
                if char == "0":
                    zeros += 1
                elif char == "1":
                    ones += 1
            if zeros > ones:
                oxygen += "0"
            else:
                oxygen += "1"
            n += 1

            newcandidates = []
            for item in candidates:
                if item.startswith(oxygen):
                    newcandidates.append(item)
            candidates = newcandidates

            if len(candidates) == 1:
                return candidates[0]

        return oxygen

    def get_co2_scrubbing_rating():
        ex = data[0]
        n = 0

        co2 = ""
        candidates = list(data)
        while n < len(ex):
            # check the nth character of the string
            zeros = 0
            ones = 0
            for row in candidates:
                char = row[n]
                if char == "0":
                    zeros += 1
                elif char == "1":
                    ones += 1
            if zeros > ones:
                co2 += "1"
            else:
                co2 += "0"
            n += 1

            newcandidates = []
            for item in candidates:
                if item.startswith(co2):
                    newcandidates.append(item)
            candidates = newcandidates

            if len(candidates) == 1:
                return candidates[0]

        return co2

    oxygen = get_oxygen_generator_rating()
    print(f"Oxygen: {oxygen} ({int(oxygen, 2)})")

    co2 = get_co2_scrubbing_rating()
    print(f"CO2: {co2} ({int(co2, 2)})")

    answer = int(oxygen, 2) * int(co2, 2)
    print(f"Answer: {answer}")



#
# Day 4
#
def day4a():
    day = "day4a"
    print(f"Running {day}...")
    data = get_data_as_string(day).split("\n\n")
    draws = data[0].split(",")

    def check_winner(items, draws):
        draws = set(draws)
        board = set(items)
        nums = draws.intersection(board)
        if len(nums) == 5:
            return True
        return False


    def create_board(board):
        """Check a single board."""
        matrix = []
        for string in board.split("\n"):
            string = string.replace("  ", " ")
            items = string.split(" ")
            row = []
            for item in items:
                x = item.strip()
                if x:
                    row.append(int(x))
            matrix.append(row)
        return matrix

    boards = []
    for board in data[1:]:
        boards.append(create_board(board))

    def check_board(board, state):
        # check rows of a board
        for row in board:
            check = check_winner(row, state)
            if check:
                print(f"Winning Row: {row}")
                return True
        # check cols of a board
        for n in range(0, 5):
            col = []
            for row in board:
                col.append(row[n])
            check = check_winner(col, state)
            if check:
                print(f"Winning Column: {col}")
                return True
        return False

    state = []
    for num in draws:
        state.append(int(num))
        # print(state)

        for board in boards:
            winner = check_board(board, state)
            if winner:
                print(f"\nWinning Board:\n")
                items = []
                for row in board:
                    print(row)
                    for item in row:
                        items.append(item)

                checked = list(set(state).intersection(set(items)))
                print(f"\nChecked items:")
                print(checked)

                unchecked = list(set(items) - set(checked))
                print(f"\nUnchecked items:")
                print(unchecked)

                print(f"\nSum of unchecked items: {sum(unchecked)}")
                last = state[-1]
                print(f"Last item selected: {last}")
                print(f"Answer: {last * sum(unchecked)}")

                sys.exit(1)

def day4b():
    day = "day4b"
    print(f"Running {day}...")
    data = get_data_as_string(day).split("\n\n")
    draws = data[0].split(",")

    def check_winner(items, draws):
        draws = set(draws)
        board = set(items)
        nums = draws.intersection(board)
        if len(nums) == 5:
            return True
        return False


    def create_board(board):
        """Check a single board."""
        matrix = []
        for string in board.split("\n"):
            string = string.replace("  ", " ")
            items = string.split(" ")
            row = []
            for item in items:
                x = item.strip()
                if x:
                    row.append(int(x))
            matrix.append(row)
        return matrix

    boards = []
    for board in data[1:]:
        boards.append(create_board(board))

    def check_board(board, state):
        # check rows of a board
        for row in board:
            check = check_winner(row, state)
            if check:
                print(f"Winning Row: {row}")
                return True
        # check cols of a board
        for n in range(0, 5):
            col = []
            for row in board:
                col.append(row[n])
            check = check_winner(col, state)
            if check:
                print(f"Winning Column: {col}")
                return True
        return False

    state = []
    for num in draws:
        state.append(int(num))
        # print(state)

        for board in boards:
            winner = check_board(board, state)
            if winner:
                boards.remove(board)
                print(f"\nWinning Board:\n")
                items = []
                for row in board:
                    print(row)
                    for item in row:
                        items.append(item)

                checked = list(set(state).intersection(set(items)))
                print(f"\nChecked items:")
                print(checked)

                unchecked = list(set(items) - set(checked))
                print(f"\nUnchecked items:")
                print(unchecked)

                print(f"\nSum of unchecked items: {sum(unchecked)}")
                last = state[-1]
                print(f"Last item selected: {last}")
                print(f"Answer: {last * sum(unchecked)}")
                print("")


#
# Day 5
#
def day5a():
    day = "day5a"
    print(f"Running {day}...")
    data = get_data_as_list(day)
    lines = []
    for item in data:
        astring, bstring = item.split(" -> ")
        ax, ay = astring.split(",")
        bx, by = bstring.split(",")
        coordinates = [(int(ax), int(ay)), (int(bx), int(by))]
        lines.append(coordinates)

    coords = {}

    for line in lines:
        a, b = line
        ax, ay = a
        bx, by = b
        if ax == bx or ay == by:
            if ax == bx:
                if ay < by:
                    choices = list(range(ay, by+1))
                else:
                    choices = list(range(by, ay+1))
                for i in choices:
                    loc = (ax, i)
                    if loc not in coords:
                        coords[loc] = 0
                    coords[loc] += 1

            elif ay == by:
                if ax < bx:
                    choices = list(range(ax, bx+1))
                else:
                    choices = list(range(bx, ax+1))
                for i in choices:
                    loc = (i, ay)
                    if loc not in coords:
                        coords[loc] = 0
                    coords[loc] += 1

    count = 0
    for loc in sorted(coords):
        val = coords[loc]
        if val >= 2:
            count += 1
        print(loc, val)
    print(count)

def day5b():
    day = "day5b"
    print(f"Running {day}...")
    data = get_data_as_list(day)
    lines = []
    for item in data:
        astring, bstring = item.split(" -> ")
        ax, ay = astring.split(",")
        bx, by = bstring.split(",")
        coordinates = [(int(ax), int(ay)), (int(bx), int(by))]
        lines.append(coordinates)

    coords = {}

    for line in lines:
        a, b = line
        ax, ay = a
        bx, by = b
        if ax == bx or ay == by:
            # handle vertical lines
            if ax == bx:
                if ay < by:
                    choices = list(range(ay, by+1))
                else:
                    choices = list(range(by, ay+1))
                for i in choices:
                    loc = (ax, i)
                    if loc not in coords:
                        coords[loc] = 0
                    coords[loc] += 1
            # handle horizontal lines
            elif ay == by:
                if ax < bx:
                    choices = list(range(ax, bx+1))
                else:
                    choices = list(range(bx, ax+1))
                for i in choices:
                    loc = (i, ay)
                    if loc not in coords:
                        coords[loc] = 0
                    coords[loc] += 1
        # handle diagonal lines
        else:
            if ax < bx:
                x_range = list(range(ax, bx+1))
            else:
                x_range = list(range(bx, ax+1))
                x_range.reverse()

            if ay < by:
                y_range = list(range(ay, by+1))
            else:
                y_range = list(range(by, ay+1))
                y_range.reverse()

            n = 0
            while n < len(x_range):
                loc = (x_range[n], y_range[n])
                if loc not in coords:
                    coords[loc] = 0
                coords[loc] += 1
                n += 1

    count = 0
    for loc in sorted(coords):
        val = coords[loc]
        if val >= 2:
            count += 1
        print(loc, val)
    print(count)


#
# Day 6
#
def day6a():
    day = "day6a"
    print(f"Running {day}...")
    data = get_data_as_string(day).split(",")

    def process_day(state):
        newstate = []
        newfish = 0

        for item in state:
            if item == "0":
                newfish += 1
                item = "6"
            else:
                item = str(int(item) - 1)
            newstate.append(item)
        n = 0
        while n < newfish:
            newstate.append("8")
            n += 1

        return newstate

    day = 0
    state = list(data)
    print(f"Initial State: {','.join(state)}")
    while day < 80:
        state = process_day(state)
        day += 1
        print(f"After {day} days: {len(state)}")
    print(f"Fish: {len(state)}")


def day6b():
    day = "day6b"
    print(f"Running {day}...")
    data = get_data_as_string(day).split(",")
    state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for item in data:
        n = int(item)
        state[n] += 1

    def process_day(state):
        zero = state.pop(0)
        state.append(zero)
        state[6] += zero
        return state

    day = 0
    while day < 256:
        state = process_day(state)
        day += 1
        print(f"After {day} days: {sum(state)}")


#
# Day 7
#
def day7a():
    day = "day7a"
    print(f"Running {day}...")
    data = []
    for item in get_data_as_string(day).split(","):
        data.append(int(item))

    print(f"Max position: {max(data)}")
    print(f"Min position: {min(data)}")

    average = sum(data) / len(data)
    print(f"Average position: {average}")

    def check_position(pos):
        """Check a single position."""
        total = 0
        for item in data:
            dist = abs(item - pos)
            total += dist
            # print(f"- Move from {item} to {pos}: {dist} fuel")

        print(f"Position: {pos}, Total fuel: {total}")
        return total

    bestpos = None
    bestfuel = None

    n = min(data)
    while n <= max(data):
        fuel = check_position(n)
        if bestpos is None:
            bestpos = n
        if bestfuel is None:
            bestfuel = fuel
        elif fuel < bestfuel:
            bestfuel = fuel
            bestpos = n
        n += 1

    print(f"Best Fuel: {bestfuel}")
    print(f"Best Position: {bestpos}")



def day7b():
    day = "day7b"
    print(f"Running {day}...")
    data = []
    for item in get_data_as_string(day).split(","):
        data.append(int(item))

    print(f"Max position: {max(data)}")
    print(f"Min position: {min(data)}")

    average = sum(data) / len(data)
    print(f"Average position: {average}")

    def check_position(pos):
        """Check a single position."""
        total = 0
        for item in data:
            dist = abs(item - pos)
            fuel = sum(range(1, dist+1))
            total += fuel
            # print(f"- Move from {item} to {pos}: {dist} fuel")

        print(f"Position: {pos}, Total fuel: {total}")
        return total

    bestpos = None
    bestfuel = None

    n = min(data)
    while n <= max(data):
        fuel = check_position(n)
        if bestpos is None:
            bestpos = n
        if bestfuel is None:
            bestfuel = fuel
        elif fuel < bestfuel:
            bestfuel = fuel
            bestpos = n
        n += 1

    print(f"Best Fuel: {bestfuel}")
    print(f"Best Position: {bestpos}")



def day8a():
    day = "day8a"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    rows = data.split("\n")

    digits = 0
    for row in rows:
        a, b = row.split("|")
        signals = a.strip()
        outputs = b.strip()

        for output in outputs.split(" "):
            value = None
            if len(output) == 2:
                value = 1
            elif len(output) == 3:
                value = 7
            elif len(output) == 4:
                value = 4
            elif len(output) == 7:
                value = 8
            print(f"{output}: {value}")
            if value:
                digits += 1

    print(f"Digits: {digits}")

def day8b():
    day = "day8b"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    rows = data.split("\n")

    ssdletters = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg",
    }

    ssdlists = {
        #  [a, b, c, d, e, f, g]
        0: [1, 1, 1, 0, 1, 1, 1],
        1: [0, 0, 1, 0, 0, 1, 0],
        2: [1, 0, 1, 1, 1, 0, 1],
        3: [1, 0, 1, 1, 0, 1, 1],
        4: [0, 1, 1, 1, 0, 1, 0],
        5: [1, 1, 0, 1, 0, 1, 1],
        6: [1, 1, 0, 1, 1, 1, 1],
        7: [1, 0, 1, 0, 0, 1, 0],
        8: [1, 1, 1, 1, 1, 1, 1],
        9: [1, 1, 1, 1, 0, 1, 1],
    }
    total = 0
    for row in rows:
        a, b = row.split("|")
        signals = a.strip().split(" ")
        outputs = b.strip().split(" ")

        patterns = {}

        # mapping = [None, None, None, None, None, None, None]

        # check for easy numbers based on length
        for string in signals:
            value = None
            if len(string) == 2:
                value = 1
                patterns[1] = string
            elif len(string) == 3:
                value = 7
                patterns[7] = string
            elif len(string) == 4:
                value = 4
                patterns[4] = string
            elif len(string) == 7:
                value = 8
                patterns[8] = string
            # print(f"{string}: {value}")

        # determine "a" based on 1 and 7
        # mapping[0] = list(set(patterns[7]) - set(patterns[1]))[0]

        # figure out 3 and 6 based on 1
        for string in signals:
            if len(string) == 6:
                if len(set(string) - set(patterns[1])) == 5:
                    patterns[6] = string
                elif len(set(string) - set(patterns[4])) == 2:
                    patterns[9] = string
                else:
                    patterns[0] = string
            elif len(string) == 5:
                if len(set(string) - set(patterns[1])) == 3:
                    patterns[3] = string
                elif len(set(string) - set(patterns[4])) == 3:
                    patterns[2] = string
                else:
                    patterns[5] = string

        # determine "c" based on 1 and 6
        # mapping[2] = list(set(patterns[1]) - set(patterns[6]))[0]

        # determine "f" based on 1 and "c"
        # mapping[5] = list(set(patterns[1]) - set([mapping[2]]))[0]

        mapping = {}
        for value in patterns:
            string = patterns[value]
            mapping[string] = value

        # print(json.dumps(patterns, indent=2, sort_keys=True))
        # print(json.dumps(mapping, indent=2, sort_keys=True))

        outputvalue = []
        for string in outputs:
            for pattern in mapping:
                if set(string) == set(pattern):
                    outputvalue.append(str(mapping[pattern]))
        number = int("".join(outputvalue))
        total += number
    print(f"Total: {total}")


def day9a():
    day = "day9a"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    matrix = []

    for row in data.split("\n"):
        items = []
        for item in list(row):
            items.append(int(item))
        matrix.append(items)

    length = len(matrix)
    width = len(matrix[0])
    print(f"Length: {length}, Width: {width}")

    def check_adjacent(l, w):
        """Check the squares adjacent to a point."""
        value = matrix[l][w]

        if l > 0:
            up = matrix[l-1][w]
        else:
            up = 10

        if l < length - 1:
            down = matrix[l+1][w]
        else:
            down = 10

        if w > 0:
            left = matrix[l][w-1]
        else:
            left = 10

        if w < width - 1:
            right = matrix[l][w+1]
        else:
            right = 10

        check = None
        if up > value and down > value and left > value and right > value:
            check = value

        return check

    total = 0
    l = 0
    while l < length:
        w = 0
        while w < width:
            check = check_adjacent(l, w)
            if not check is None:
                print(f"({l}, {w})")
                total += 1 + check
            w += 1
        l += 1
    print(f"Total: {total}")


class Basin:

    def __init__(self, l, w, matrix):
        self.count = 1
        self.matrix = matrix
        self.lowpoint = (l, w)
        self.index = [self.lowpoint]

        self.length = len(self.matrix)
        self.width = len(self.matrix[0])

    def check_location(self, l, w):
        up = (l-1, w)
        down = (l+1, w)
        left = (l, w-1)
        right = (l, w+1)

        sides = [up, down, left, right]

        for loc in sides:
            if loc in self.index:
                continue
            a, b = loc
            self.index.append(loc)
            if a < 0:
                continue
            if b < 0:
                continue
            if a > self.length - 1:
                continue
            if b > self.width - 1:
                continue
            value = self.matrix[a][b]
            if value < 9:
                self.count += 1
                self.check_location(a, b)


        return self.count



def day9b():
    day = "day9b"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    matrix = []

    for row in data.split("\n"):
        items = []
        for item in list(row):
            items.append(int(item))
        matrix.append(items)

    length = len(matrix)
    width = len(matrix[0])
    print(f"Length: {length}, Width: {width}")

    def check_adjacent(l, w):
        """Check the squares adjacent to a point."""
        value = matrix[l][w]

        if l > 0:
            up = matrix[l-1][w]
        else:
            up = 10

        if l < length - 1:
            down = matrix[l+1][w]
        else:
            down = 10

        if w > 0:
            left = matrix[l][w-1]
        else:
            left = 10

        if w < width - 1:
            right = matrix[l][w+1]
        else:
            right = 10

        check = None
        if up > value and down > value and left > value and right > value:
            check = value

        return check

    lowpoints = {}

    l = 0
    while l < length:
        w = 0
        while w < width:
            check = check_adjacent(l, w)
            if not check is None:
                lowpoints[(l, w)] = 0
            w += 1
        l += 1

    basins = {}

    for lowpoint in lowpoints:
        print(f"\nLowpoint: {lowpoint}")
        l, w = lowpoint
        basin = Basin(l, w, matrix)
        count = basin.check_location(l, w)
        basins[lowpoint] = count

    topthree = []
    for lowpoint in sorted(basins, key=lambda x: basins[x], reverse=True)[:3]:
        count = basins[lowpoint]
        print(lowpoint, count)
        topthree.append(count)
    print(f"Total: {math.prod(topthree)}")


def day10a():
    day = "day10a"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    rows = data.split("\n")

    openchars = ["(", "[", "{", "<"]
    closechars = [")", "]", "}", ">"]
    points = [3, 57, 1197, 25137]

    def check_row(row):
        """Check a single row."""
        openstack = []
        closestack = []
        value = 0
        for char in row:
            if char in openchars:
                openstack.append(char)
            elif char in closechars:
                n = closechars.index(char)
                openchar = openchars[n]
                check = openstack.pop()
                if check != openchar:
                    print(f"Expected {check} but found {char} instead.")
                    value = points[n]
                    return value
                closestack.append(char)
            else:
                print(f"Error: Unknown character: {char}")
        return value

    total = 0
    for row in rows:
        print(row)
        value = check_row(row)
        if value:
            total += value
    print(f"Total: {total}")

def day10b():
    day = "day10b"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    rows = data.split("\n")

    openchars = ["(", "[", "{", "<"]
    closechars = [")", "]", "}", ">"]
    points = [3, 57, 1197, 25137]

    def check_row(row):
        """Check a single row."""
        openstack = []
        closestack = []
        value = 0
        added = []
        for char in row:
            if char in openchars:
                openstack.append(char)
            elif char in closechars:
                n = closechars.index(char)
                openchar = openchars[n]
                check = openstack.pop()
                if check != openchar:
                    # print(f"Expected {check} but found {char} instead.")
                    # value = points[n]
                    return value
                closestack.append(char)
            else:
                print(f"Error: Unknown character: {char}")

        while openstack:
            openchar = openstack.pop()
            n = openchars.index(openchar)
            closechar = closechars[n]
            added.append(closechar)

        closepoints = [1, 2, 3, 4]
        print(f"{row} - Complete by adding {''.join(added)}")

        score = 0
        for char in added:
            # print(f"Score: {score}")
            score = score * 5
            n = closechars.index(char)
            score += closepoints[n]

        return score

    scores = []
    for row in rows:
        score = check_row(row)
        if not score:
            continue
        print(f"Score: {score}")
        scores.append(score)

    numscores = len(scores)
    print(f"Scores: {numscores}")
    for score in sorted(scores):
        print(score)
    ind = round(numscores / 2)
    print(ind)
    print(f"Answer: {sorted(scores)[ind]}")


def day11a():
    day = "day11a"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    energy = []

    print(f"Before any steps:")
    for row in data.split("\n"):
        print(row)
        numbers = []
        for char in row:
            numbers.append(int(char))
        energy.append(numbers)

    print("")

    def identify_flashes(energy, flashes=[]):
        """Return a list of flashes for a given energy grid."""
        n = 0
        newflashes = []
        while n < len(energy):
            row = energy[n]
            m = 0
            while m < len(row):
                loc = (n, m)
                num = row[m]
                if num > 9 and loc not in flashes:
                    newflashes.append(loc)
                m += 1
            n += 1
        return list(set(newflashes))

    def process_flashes(flashes, energy):
        """Process a list of flashes and return the energy grid."""
        length = len(energy)
        width = len(energy[0])

        # process flashes
        for flash in flashes:
            n, m = flash

            # up right
            ur = (n-1, m-1)

            # up
            up = (n-1, m)

            # up left
            ul = (n-1, m+1)

            # left
            left = (n, m-1)

            # right
            right = (n, m+1)

            # bottom left
            bl = (n+1, m-1)

            # bottom
            bottom = (n+1, m)

            # bottom right
            br = (n+1, m+1)

            # update the surrounding octopuses
            for loc in [ur, up, ul, left, right, bl, bottom, br]:
                a, b = loc
                if a < 0 or a > length - 1:
                    continue
                if b < 0 or b > width - 1:
                    continue
                energy[a][b] += 1
        return energy

    def process_energy(energy):
        """Process the energy of one day."""
        # add one to every octopus
        n = 0
        while n < len(energy):
            m = 0
            row = energy[n]
            while m < len(row):
                energy[n][m] += 1
                m += 1
            n += 1

        # identify initial flashes
        flashes = identify_flashes(energy)

        # process the first set of flashes
        energy = process_flashes(flashes, energy)

        newflashes = identify_flashes(energy, flashes)
        while newflashes:
            energy = process_flashes(newflashes, energy)
            flashes.extend(newflashes)
            newflashes = identify_flashes(energy, flashes)

        # drop any above 9 back to zero
        n = 0
        while n < len(energy):
            m = 0
            row = energy[n]
            while m < len(row):
                if energy[n][m] > 9:
                    energy[n][m] = 0
                m += 1
            n += 1

        return energy, len(flashes)

    n = 0
    count = 0
    while n < 100:
        print(f"\nAfter step {n+1}:")
        energy, flashcount = process_energy(energy)
        count += flashcount
        for row in energy:
            text = ""
            for num in row:
                text += str(num)
            print(text)
        n += 1

    print(f"Flashes: {count}")




def day11b():
    day = "day11b"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    energy = []

    print(f"Before any steps:")
    for row in data.split("\n"):
        print(row)
        numbers = []
        for char in row:
            numbers.append(int(char))
        energy.append(numbers)

    print("")

    def identify_flashes(energy, flashes=[]):
        """Return a list of flashes for a given energy grid."""
        n = 0
        newflashes = []
        while n < len(energy):
            row = energy[n]
            m = 0
            while m < len(row):
                loc = (n, m)
                num = row[m]
                if num > 9 and loc not in flashes:
                    newflashes.append(loc)
                m += 1
            n += 1
        return list(set(newflashes))

    def process_flashes(flashes, energy):
        """Process a list of flashes and return the energy grid."""
        length = len(energy)
        width = len(energy[0])

        # process flashes
        for flash in flashes:
            n, m = flash

            # up right
            ur = (n-1, m-1)

            # up
            up = (n-1, m)

            # up left
            ul = (n-1, m+1)

            # left
            left = (n, m-1)

            # right
            right = (n, m+1)

            # bottom left
            bl = (n+1, m-1)

            # bottom
            bottom = (n+1, m)

            # bottom right
            br = (n+1, m+1)

            # update the surrounding octopuses
            for loc in [ur, up, ul, left, right, bl, bottom, br]:
                a, b = loc
                if a < 0 or a > length - 1:
                    continue
                if b < 0 or b > width - 1:
                    continue
                energy[a][b] += 1
        return energy

    def process_energy(energy):
        """Process the energy of one day."""
        # add one to every octopus
        n = 0
        while n < len(energy):
            m = 0
            row = energy[n]
            while m < len(row):
                energy[n][m] += 1
                m += 1
            n += 1

        # identify initial flashes
        flashes = identify_flashes(energy)

        # process the first set of flashes
        energy = process_flashes(flashes, energy)

        newflashes = identify_flashes(energy, flashes)
        while newflashes:
            energy = process_flashes(newflashes, energy)
            flashes.extend(newflashes)
            newflashes = identify_flashes(energy, flashes)

        # drop any above 9 back to zero
        n = 0
        while n < len(energy):
            m = 0
            row = energy[n]
            while m < len(row):
                if energy[n][m] > 9:
                    energy[n][m] = 0
                m += 1
            n += 1

        done = False
        if energy == [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]:
            done = True
        return energy, len(flashes), done

    n = 0
    count = 0
    while n < 1000:
        print(f"\nAfter step {n+1}:")
        energy, flashcount, done = process_energy(energy)
        count += flashcount
        for row in energy:
            text = ""
            for num in row:
                text += str(num)
            print(text)
        n += 1
        if done:
            print(f"YAY WE FOUND IT!!!")
            sys.exit(1)

    print(f"Flashes: {count}")


def day12a():
    day = "day12a"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    rows = data.split("\n")
    for row in rows:
        print(row)

    def get_next_steps(points, path):
        """Return the next steps from a given point."""
        nextpoints = []
        last = path[-1]
        if last == "end":
            return []
        for x in points[last]:
            if x == x.lower() and x in path:
                continue
            nextpoints.append(x)
        return nextpoints

    def get_paths(paths):
        newpaths = []
        for path in paths:
            for step in get_next_steps(points, path):
                newpath = list(path)
                if step == step.lower() and step in path:
                    continue
                newpath.append(step)
                newpaths.append(newpath)
        return newpaths

    def get_unfinished(paths):
        """Return the count of unfinished paths."""
        newpaths = []
        for path in paths:
            if path[-1] != "end":
                newpaths.append(path)
        return newpaths

    # assemble points
    points = {}
    for row in rows:
        x, y = row.split("-")

        if x not in points:
            points[x] = []
        points[x].append(y)

        if x != "start" and y != "end":
            if y not in points:
                points[y] = []
            points[y].append(x)

    print(json.dumps(points, indent=2, sort_keys=True))

    finished = []

    paths = [["start"]]

    n = 0
    while get_unfinished(paths):
        newpaths = get_paths(paths)
        paths = []
        for path in newpaths:
            if path[-1] == "end":
                finished.append(path)
            else:
                paths.append(path)
        n += 1

    print("")
    for path in sorted(finished):
        print(",".join(path))

    print(f"Paths: {len(finished)}")


def day12b():
    day = "day12b"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    rows = data.split("\n")
    for row in rows:
        print(row)

    def get_next_steps(points, path):
        """Return the next steps from a given point."""
        nextpoints = []
        last = path[-1]
        if last == "end":
            return []
        for x in points[last]:
            skip = False
            dupes = []
            for char in set(path):
                if char == char.lower() and path.count(char) > 1:
                    dupes.append(char)
            if x == x.lower() and x in path and dupes:
                continue
            nextpoints.append(x)
        return nextpoints

    def get_paths(paths):
        newpaths = []
        for path in paths:
            for step in get_next_steps(points, path):
                newpath = list(path)
                newpath.append(step)
                newpaths.append(newpath)
        return newpaths

    def get_unfinished(paths):
        """Return the count of unfinished paths."""
        newpaths = []
        for path in paths:
            if path[-1] != "end":
                newpaths.append(path)
        return newpaths

    # assemble points
    points = {}
    for row in rows:
        x, y = row.split("-")

        if y != "start":
            if x not in points:
                points[x] = []
            points[x].append(y)

        if x != "start" and y != "end":
            if y not in points:
                points[y] = []
            points[y].append(x)

    print(json.dumps(points, indent=2, sort_keys=True))

    finished = []

    paths = [["start"]]

    n = 0
    while get_unfinished(paths):
        newpaths = get_paths(paths)
        paths = []
        for path in newpaths:
            if path[-1] == "end":
                finished.append(path)
            else:
                paths.append(path)
        n += 1

    # print("")
    # for path in sorted(finished):
    #     print(",".join(path))

    print(f"Paths: {len(finished)}")



def day13a():
    day = "day13a"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    dots, folds = data.split("\n\n")

    # prepare matrix
    cols = 0
    rows = 0
    coords = []
    for dot in dots.split("\n"):
        x, y = dot.split(",")
        x = int(x)
        y = int(y)
        loc = (x, y)
        if x > cols:
            cols = x
        if y > rows:
            rows = y
        coords.append(loc)

    matrix = []

    y = 0
    while y < rows + 1:
        x = 0
        row = []
        while x < cols + 1:
            loc = (x, y)
            if loc in coords:
                row.append("#")
            else:
                row.append(".")
            x += 1
        y += 1
        matrix.append(row)

    for row in matrix:
        print("".join(row))

    def fold_matrix(matrix, axis, num):
        print(f"fold along {axis}={num}\n")

        if axis == "y":
            n = 1
            for row in matrix[num+1:]:
                x = 0
                while x < len(row):
                    if matrix[num+n][x] == "#":
                        matrix[num-n][x] = "#"
                    x += 1
                n += 1

            newmatrix = []
            for row in matrix[:num]:
                newmatrix.append(row)

        elif axis == "x":
            n = 1
            for row in matrix:
                n = 1
                while num + n < len(row):
                    if row[num+n] == "#":
                        row[num-n] = "#"
                    n += 1

            newmatrix = []
            for row in matrix:
                newmatrix.append(row[:num])

        return newmatrix

    for fold in folds.split("\n"):
        _, _, inst = fold.split(" ")
        axis, num = inst.split("=")
        num = int(num)
        print("")
        matrix = fold_matrix(matrix, axis, num)
        count = 0
        for row in matrix:
            count += row.count("#")
            print("".join(row))
        print(f"Count: {count}")


def day13b():
    day = "day13b"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    rows = data.split("\n")


def day14a():
    day = "day14a"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    template, part2 = data.split("\n\n")
    rules = {}
    for rule in part2.split("\n"):
        a, b = rule.split(" -> ")
        rules[a] = b

    def insert_items(template, rules):
        """Insert items into the template."""
        pairs = []
        n = 0
        while n < len(template) - 1:
            pair = template[n:n+2]
            pairs.append(pair)
            n += 1

        output = ""
        for pair in pairs:
            if pair in rules:
                a, b = list(pair)
                new = rules[pair]
                # print(pair, new)
                output += f"{a}{new}"
            else:
                output += a
        output += b
        return output

    n = 0
    while n < 40:
        print(f"{n}")
        template = insert_items(template, rules)
        n += 1

    stats = {}
    for char in template:
        if char not in stats:
            stats[char] = 0
        stats[char] += 1

    data = sorted(stats, key=lambda x: stats[x])
    top = data[-1]
    bottom = data[0]
    answer = stats[top] - stats[bottom]
    print(answer)

def day14b():
    day = "day14b"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    template, part2 = data.split("\n\n")

    def get_pairs(string):
        """Return pairs."""
        pairs = []
        n = 0
        while n < len(string) - 1:
            pair = string[n:n+2]
            pairs.append(pair)
            n += 1
        return pairs

    def update_counts(counts, rules):
        data = dict(counts)
        for pair in data:
            num = data[pair]
            if not num:
                continue
            a, c = list(pair)
            b = rules[pair]
            pair1 = a + b
            pair2 = b + c
            counts[pair] -= num
            counts[pair1] += num
            counts[pair2] += num
        return counts

    counts = {}
    rules = {}
    for rule in part2.split("\n"):
        a, b = rule.split(" -> ")
        rules[a] = b
        counts[a] = 0

    # set initial counts
    for pair in get_pairs(template):
        counts[pair] += 1

    # print(json.dumps(counts, indent=2, sort_keys=True))

    last = template[-1]

    n = 0
    while n < 40:
        counts = update_counts(counts, rules)
        n += 1

    for count in sorted(counts):
        print(count, counts[count])

    letters = {last: 1}
    for pair in sorted(counts):
        count = counts[pair]
        a, b = list(pair)
        if a not in letters:
            letters[a] = 0
        letters[a] += count

    print(json.dumps(letters, indent=2, sort_keys=True))
    totals = sorted(letters, key=lambda x: letters[x])
    top = totals[-1]
    bottom = totals[0]
    print(top, bottom)
    answer = letters[top] - letters[bottom]
    print(answer)


def day15a():
    day = "day15a"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    rows = data.split("\n")

    matrix = []
    for row in rows:
        newrow = []
        for item in list(row):
            newrow.append(int(item))
        matrix.append(newrow)

    numrows = len(matrix)
    numcols = len(matrix[0])

    loc = (0, 0)
    dest = (numrows - 1, numcols - 1)

    def get_next_steps(loc):
        """Return the list of next steps for a given location."""
        next_steps = []
        x, y = loc
        right = (x, y+1)
        down = (x+1, y)
        left = (x, y-1)
        up = (x-1, y)
        for n in [
            right,
            down,
            left,
            up
        ]:
            a, b = n
            if a < 0:
                continue
            if a > numrows - 1:
                continue
            if b < 0:
                continue
            if b > numcols - 1:
                continue
            next_steps.append(n)
        return next_steps

    def find_path(loc):
        """Return the best path to the destination."""
        if loc == dest:
            x, y = dest
            risk = matrix[x][y]
            return risk

        next_steps = get_next_steps(loc)

        scores = {}
        for step in next_steps:
            x, y = step
            scores[step] = find_path(step) + matrix[x][y]

        # print(f"\n{loc}:")
        # for step in sorted(scores, key=lambda x: scores[x]):
        #     print(f" * {step}: {scores[step]}")

        lowest = sorted(scores, key=lambda x: scores[x])[0]
        # print(f"Lowest: {lowest}")
        x, y = lowest
        return scores[lowest]


    # response = find_path(loc)
    # print(response - 1)

    from collections import defaultdict

    class Graph():
        def __init__(self):
            """
            self.edges is a dict of all possible next nodes
            e.g. {'X': ['A', 'B', 'C', 'E'], ...}
            self.weights has all the weights between two nodes,
            with the two nodes as a tuple as the key
            e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
            """
            self.edges = defaultdict(list)
            self.weights = {}

        def add_edge(self, from_node, to_node, weight):
            # Note: assumes edges are bi-directional
            self.edges[from_node].append(to_node)
            # self.edges[to_node].append(from_node)
            self.weights[(from_node, to_node)] = weight
            # self.weights[(to_node, from_node)] = weight

    graph = Graph()

    def initialize_graph(graph):
        # initialize graph
        x = 0
        while x < numrows:
            y = 0
            while y < numcols:
                loc = (x, y)
                for dest in get_next_steps(loc):
                    a, b = dest
                    value = matrix[a][b]
                    graph.add_edge(loc, dest, value)
                y += 1
            x += 1

    def dijsktra(graph, initial, end):
        # shortest paths is a dict of nodes
        # whose value is a tuple of (previous node, weight)
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()

        while current_node != end:
            visited.add(current_node)
            destinations = graph.edges[current_node]
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = graph.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            # next node is the destination with the lowest weight
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        # Work back through destinations in shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        # Reverse path
        path = path[::-1]
        return path

    initialize_graph(graph)
    path = dijsktra(graph, (0, 0), dest)
    print(path)
    score = 0
    for loc in path[1:]:
        a, b = loc
        score += matrix[a][b]
    print(f"score: {score}")


def day15b():
    day = "day15b"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    rows = data.split("\n")

    matrix = []
    for row in rows:
        newrow = []
        for item in list(row):
            newrow.append(int(item))
        n = 1
        while n < 5:
            for item in list(row):
                value = int(item) + n
                if value > 9:
                    value -= 9
                newrow.append(value)
            n += 1
        matrix.append(newrow)
        print("".join([str(x) for x in newrow]))

    m = 1
    original = list(matrix)
    while m < 5:
        for row in original:
            newrow = []
            for item in row:
                value = item + m
                if value > 9:
                    value -= 9
                newrow.append(value)
            matrix.append(newrow)
            print("".join([str(x) for x in newrow]))
        m += 1

    numrows = len(matrix)
    numcols = len(matrix[0])

    loc = (0, 0)
    dest = (numrows - 1, numcols - 1)

    def get_next_steps(loc):
        """Return the list of next steps for a given location."""
        next_steps = []
        x, y = loc
        right = (x, y+1)
        down = (x+1, y)
        left = (x, y-1)
        up = (x-1, y)
        for n in [
            right,
            down,
            left,
            up
        ]:
            a, b = n
            if a < 0:
                continue
            if a > numrows - 1:
                continue
            if b < 0:
                continue
            if b > numcols - 1:
                continue
            next_steps.append(n)
        return next_steps

    def find_path(loc):
        """Return the best path to the destination."""
        if loc == dest:
            x, y = dest
            risk = matrix[x][y]
            return risk

        next_steps = get_next_steps(loc)

        scores = {}
        for step in next_steps:
            x, y = step
            scores[step] = find_path(step) + matrix[x][y]

        # print(f"\n{loc}:")
        # for step in sorted(scores, key=lambda x: scores[x]):
        #     print(f" * {step}: {scores[step]}")

        lowest = sorted(scores, key=lambda x: scores[x])[0]
        # print(f"Lowest: {lowest}")
        x, y = lowest
        return scores[lowest]


    # response = find_path(loc)
    # print(response - 1)

    from collections import defaultdict

    class Graph():
        def __init__(self):
            """
            self.edges is a dict of all possible next nodes
            e.g. {'X': ['A', 'B', 'C', 'E'], ...}
            self.weights has all the weights between two nodes,
            with the two nodes as a tuple as the key
            e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
            """
            self.edges = defaultdict(list)
            self.weights = {}

        def add_edge(self, from_node, to_node, weight):
            # Note: assumes edges are bi-directional
            self.edges[from_node].append(to_node)
            # self.edges[to_node].append(from_node)
            self.weights[(from_node, to_node)] = weight
            # self.weights[(to_node, from_node)] = weight

    graph = Graph()

    def initialize_graph(graph):
        # initialize graph
        x = 0
        while x < numrows:
            y = 0
            while y < numcols:
                loc = (x, y)
                for dest in get_next_steps(loc):
                    a, b = dest
                    value = matrix[a][b]
                    graph.add_edge(loc, dest, value)
                y += 1
            x += 1

    def dijsktra(graph, initial, end):
        # shortest paths is a dict of nodes
        # whose value is a tuple of (previous node, weight)
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()

        while current_node != end:
            if len(visited) % 1000 == 0:
                print(len(visited))
            visited.add(current_node)
            destinations = graph.edges[current_node]
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = graph.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            # next node is the destination with the lowest weight
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        # Work back through destinations in shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        # Reverse path
        path = path[::-1]
        return path

    initialize_graph(graph)
    path = dijsktra(graph, (0, 0), dest)
    print(path)
    score = 0
    for loc in path[1:]:
        a, b = loc
        score += matrix[a][b]
    print(f"score: {score}")


def day16a():
    day = "day16a"
    print(f"Running {day}...")
    data = get_data_as_string(day)

    hexmap = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    binmap = {}
    for key, value in hexmap.items():
        binmap[value] = key

    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def hex2bin(data):
        packet = ""
        for char in data:
            binary = hexmap[char]
            packet += binary
        return packet

    def get_literal(string):
        """Return the literal value."""
        binary = ""
        for chunk in chunks(list(string), 5):
            if chunk[0] == "1":
                binary += "".join(chunk[1:])
            elif chunk[0] == "0":
                binary += "".join(chunk[1:])
                break
        return int(binary, 2)

    def parse(binary_string, bit_index, versions):
        packet_version = binary_string[bit_index:bit_index+3]
        type_id = int(binary_string[bit_index+3:bit_index+6], 2)
        bit_index += 6

        versions.append(int(packet_version, 2))

        if (type_id == 4): # Literal Value
            value = ''
            while (binary_string[bit_index] == '1'):
                value += binary_string[bit_index+1:bit_index+5]
                bit_index += 5

            value += binary_string[bit_index+1:bit_index+5]
            bit_index += 5
        else: # Operator
            length_type_id = binary_string[bit_index]
            bit_index += 1

            field_length = 15 if length_type_id == '0' else 11

            remaining = int(binary_string[bit_index:bit_index+field_length], 2)
            bit_index += field_length

            while (remaining > 0):
                subpacket_length = parse(binary_string, bit_index, versions) - bit_index
                bit_index += subpacket_length
                remaining -= subpacket_length if field_length == 15 else 1

        return bit_index


    versions = []
    string = hex2bin(data)
    print(string)
    parse(string, 0, versions)
    print(f"\nVersion Sum: {sum(versions)}")

def day16b():
    day = "day16b"
    print(f"Running {day}...")
    data = get_data_as_string(day)

    hexmap = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    binmap = {}
    for key, value in hexmap.items():
        binmap[value] = key

    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def hex2bin(data):
        packet = ""
        for char in data:
            binary = hexmap[char]
            packet += binary
        return packet

    def get_literal(string):
        """Return the literal value."""
        binary = ""
        for chunk in chunks(list(string), 5):
            if chunk[0] == "1":
                binary += "".join(chunk[1:])
            elif chunk[0] == "0":
                binary += "".join(chunk[1:])
                break
        return int(binary, 2)

    def parse(binary_string, bit_index, versions):
        packet_version = binary_string[bit_index:bit_index+3]
        type_id = int(binary_string[bit_index+3:bit_index+6], 2)
        bit_index += 6

        string = binary_string[bit_index:]
        # print(f"\nString: {string}")
        # print(f"Version: {packet_version}, Type ID: {type_id}")

        versions.append(int(packet_version, 2))

        if (type_id == 4): # Literal Value
            valuestring = ''
            while (binary_string[bit_index] == '1'):
                valuestring += binary_string[bit_index+1:bit_index+5]
                bit_index += 5

            valuestring += binary_string[bit_index+1:bit_index+5]
            bit_index += 5

            value = int(valuestring, 2)
            # print(f"Value: {int(value, 2)}")

        else: # Operator
            length_type_id = binary_string[bit_index]
            bit_index += 1

            field_length = 15 if length_type_id == '0' else 11

            remaining = int(binary_string[bit_index:bit_index+field_length], 2)
            bit_index += field_length

            values = []
            while (remaining > 0):
                subindex, value = parse(binary_string, bit_index, versions)
                values.append(value)
                subpacket_length = subindex - bit_index
                bit_index += subpacket_length
                remaining -= subpacket_length if field_length == 15 else 1

            if type_id == 0:
                print(f"Add: {values}")
                value = sum(values)
            elif type_id == 1:
                print(f"Multiply: {values}")
                value = math.prod(values)
            elif type_id == 2:
                print(f"Minimum: {values}")
                value = min(values)
            elif type_id == 3:
                print(f"Maximum: {values}")
                value = max(values)
            elif type_id == 5:
                print(f"Greater Than: {values}")
                value = 1 if values[0] > values[1] else 0
            elif type_id == 6:
                print(f"Less Than: {values}")
                value = 1 if values[0] < values[1] else 0
            elif type_id == 7:
                print(f"Equal To: {values}")
                value = 1 if values[0] == values[1] else 0

        return bit_index, value


    versions = []
    string = hex2bin(data)
    _, value = parse(string, 0, versions)
    # print(index)
    print(f"Value: {value}")


def day17a():
    day = "day17a"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    string = data.replace("target area: ", "")
    a, b = string.split(", ")
    x1, x2 = a.replace("x=", "").split("..")
    y1, y2 = b.replace("y=", "").split("..")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    def run_step(start, velocity):
        x, y = start
        a, b = velocity

        x += a
        y += b

        # add drag
        if a > 0:
            a -= 1
        elif a < 0:
            a += 1

        b -= 1

        return (x, y), (a, b)

    def check_velocity(location, velocity):
        max_height = 0
        while True:
            location, velocity = run_step(location, velocity)
            x, y = location
            if y > max_height:
                max_height = y
            if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                return max_height
            # check for short miss
            if x < x1 and y < y1:
                return None
            elif x > x2 and y < y1:
                return -1
            elif y < y1:
                return None
        return None

    print(f"Target Area: x={x1}..{x2}, y={y1}..{y2}")
    location = (0, 0)

    # center_hit = (round((x1 + x2) / 2), round((y1 + y2) / 2))
    # velocity = center_hit
    velocity = (1, 1)
    # value = check_velocity(location, velocity)
    max_height = 0
    last_status = None
    while True:
        x, y = velocity
        value = check_velocity(location, velocity)
        if value is not None and value > max_height:
            max_height = value
        if value is None:
            print(f"Short Miss! {max_height}")
            last_status = "short"
            velocity = (x + 1, y)
            # break
        elif value == -1:
            print(f"Long Miss! {max_height}")
            # if last_status != "hit":
            #     print(f"Double long hit.")
            #     break
            last_status = "long"
            velocity = (1, y + 1)
            # break
        elif value > 0:
            print(f"Hit! Velocity: {velocity}, Max Height: {value}")
            last_status = "hit"
            velocity = (x + 1, y)
        else:
            break
    print(max_height)

def day17b():
    day = "day17b"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    string = data.replace("target area: ", "")
    a, b = string.split(", ")
    x1, x2 = a.replace("x=", "").split("..")
    y1, y2 = b.replace("y=", "").split("..")
    xmin = int(x1)
    xmax = int(x2)
    ymin = int(y1)
    ymax = int(y2)

    def is_hit(velocity):
        for pos in trajectory(velocity):
            if (
                xmin <= pos[0] <= xmax and
                ymin <= pos[1] <= ymax
            ):
                return True
        return False

    def trajectory(velocity):
        pos = (0, 0)
        while pos[0] <= xmax and pos[1] >= ymin:
            yield pos
            # pos = grid.addvec(pos, velocity)
            pos = tuple(x+y for x,y in zip(pos, velocity))
            velocity = (
                max(0, velocity[0] - 1),
                velocity[1] - 1
            )

    result = 0
    for xvel in range(0, xmax + 1):
        for yvel in range(ymin, -ymin):
            if is_hit((xvel, yvel)):
                result += 1
    print(result)


def day18a():
    day = "day18a"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    # inputs = []
    # for item in data.split("\n"):
    #     inputs.append(eval(item))

    def parse_line(line):
        elements = filter(lambda element: element != ',', line)
        elements = list(map(lambda element: int(element) if element.isdigit() else element, elements))
        return elements

    def explode(elements, opening_bracket_index):
        left_number = elements[opening_bracket_index + 1]
        right_number = elements[opening_bracket_index + 2]

        for i in range(opening_bracket_index - 1, 0, -1):
            if isinstance(elements[i], int):
                elements[i] += left_number
                break

        for i in range(opening_bracket_index + 4, len(elements)):
            if isinstance(elements[i], int):
                elements[i] += right_number
                break

        return elements[:opening_bracket_index] + [0] + elements[opening_bracket_index + 4:]


    def try_to_explode(elements):
        open_brackets = 0
        for i in range(len(elements)):
            if open_brackets == 4 and elements[i] == '[':
                elements = explode(elements, i)
                return True, elements
            elif elements[i] == '[':
                open_brackets += 1
            elif elements[i] == ']':
                open_brackets -= 1
        return False, elements


    def try_to_split(elements):
        for i in range(len(elements)):
            if isinstance(elements[i], int) and elements[i] >= 10:
                elements[i:i + 1] = ['[', math.floor(elements[i] / 2), math.ceil(elements[i] / 2), ']']
                return True, elements
        return False, elements


    def reduce_elements(elements):
        has_reduced = True
        while has_reduced:
            has_reduced, elements = try_to_explode(elements)
            if not has_reduced:
                has_reduced, elements = try_to_split(elements)

        return elements


    def calculate_magnitude(elements, index=0):
        if isinstance(elements[index], int):
            return elements[index], index

        left_sum, index = calculate_magnitude(elements, index + 1)
        right_sum, index = calculate_magnitude(elements, index + 1)

        return 3 * left_sum + 2 * right_sum, index + 1

    lines = data.split("\n")
    # elements = list(map(parse_line, lines))
    # result = elements[0]
    # for i in range(1, len(elements)):
    #     result = ['['] + result + elements[i] + [']']
    #     result = reduce_elements(result)
    # print(calculate_magnitude(result)[0])

    elements = list(map(parse_line, lines))

    max_magnitude = 0
    for element1 in elements:
        for element2 in elements:
            if element1 == element2:
                continue
            added_element = ['['] + deepcopy(element1) + deepcopy(element2) + [']']
            added_element = reduce_elements(added_element)
            magnitude = calculate_magnitude(added_element)[0]
            if magnitude > max_magnitude:
                max_magnitude = magnitude
    print(max_magnitude)

def day18b():
    day = "day18b"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    print(data)


def day19a():
    day = "day19a"
    print(f"Running {day}...")
    data = get_data_as_string(day)

    from grid import Grid3d

    # import the data from the input
    scanners = {}
    scanner = None
    for row in data.split("\n"):
        if not row:
            continue
        elif "scanner" in row:
            scanner = row.split(" ")[2]
            scanners[scanner] = []
        else:
            a, b, c = row.split(",")
            scanners[scanner].append((int(a), int(b), int(c)))

    # import each scanner as a grid instance
    grids = {}
    print(f"Generating a grid for each scanner...")
    for scanner in scanners:
        beacons = scanners[scanner]
        grid = Grid3d(beacons)
        grid.get_distances()
        grids[scanner] = grid

    # find scanners with matching points
    print(f"Getting matches between the different scanners based on distances...""")
    for a in sorted(grids, key=lambda x: int(x)):
        agrid = grids[a]
        for b in grids:
            if b == a:
                continue
            bgrid = grids[b]
            if len(agrid.distset.intersection(bgrid.distset)) >= 11:
                agrid.matches.append(b)

    # find matching points
    checked_pairs = []
    for a in sorted(grids, key=lambda x: int(x)):
        agrid = grids[a]
        for b in sorted(agrid.matches, key=lambda x: int(x)):
            pair = sorted([a, b])
            if pair in checked_pairs:
                continue
            checked_pairs.append(pair)
            print(f"\n{a} matches with {b}")
            agrid.get_matching_points(grids[b])

    all_points = []
    for scanner in grids:
        g = grids[scanner]
        for point in g.cube:
            if point not in all_points:
                all_points.append(point)

    print(f"Beacons: {len(all_points)}")


def day19b():
    day = "day19b"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    print(data)

def day20a():
    day = "day20a"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    algorithm, image = data.split("\n\n")

    def create_grid(image):
        """Create a grid out of an image."""
        rows = image.split("\n")
        grid = {}
        y = 0
        while y < len(rows):
            row = rows[y]
            x = 0
            while x < len(row):
                grid[(x, y)] = row[x]
                x += 1
            y += 1
        return grid

    def display_grid(grid):
        minimum = min(grid)
        maximum = max(grid)

        # xmin, ymin = minimum
        xmax, ymax = maximum
        # print(f"Min: {minimum}, Max: {maximum}")

        length = ymax + 1
        width = xmax + 1
        print(f"\nGrid Size: {width} x {length}")

        y = 0
        while y < length:
            row = []
            x = 0
            while x < width:
                p = (x, y)
                # print(p)
                v = grid[p]
                row.append(v)
                x += 1
            print("".join(row))
            y += 1

    def enhance_grid(grid, algorithm):
        default = grid[(0, 0)]

        # determine values for each pixel
        values = {}
        for point in dict(grid):
            binary = ""
            x, y = point
            items = [
                (x-1, y-1),
                (x, y-1),
                (x+1, y-1),
                (x-1, y),
                point,
                (x+1, y),
                (x-1, y+1),
                (x, y+1),
                (x+1, y+1),
            ]
            for item in items:
                if item in grid:
                    v = grid[item]
                else:
                    grid[item] = default
                    v = default

                if v == ".":
                    binary += "0"
                elif v == "#":
                    binary += "1"
                else:
                    print(f"ERROR: Invalid character: {item}")
            values[point] = int(binary, 2)

        # create new grid
        newgrid = {}
        for point in values:
            v = values[point]
            newgrid[point] = algorithm[v]
        return newgrid

    def grow_grid(grid, default=None):
        """Create a grid out of an image."""
        default = grid[(0, 0)] if default is None else default
        xmax, ymax = max(grid)
        length = ymax + 1
        width = xmax + 1

        print(f"Grid: {width} x {length}")

        newgrid = {}

        y = 0

        growth = 1

        # add top padding
        while y < growth:
            x = 0
            while x < width + (growth * 2):
                newgrid[(x, y)] = default
                x += 1
            y += 1

        while y < length + growth:
            x = 0

            # add left padding
            while x < growth:
                newgrid[(x, y)] = default
                x += 1

            # add values
            while x < length + growth:
                newgrid[(x, y)] = grid[(x - growth, y - growth)]
                x += 1

            # add right padding
            while x < length + (growth * 2):
                newgrid[(x, y)] = default
                x += 1

            y += 1

        # add bottom padding
        while y < length + (growth * 2):
            x = 0
            while x < width + (growth * 2):
                newgrid[(x, y)] = default
                x += 1
            y += 1

        return newgrid


    # create initial grid
    grid = create_grid(image)
    grid = grow_grid(grid, ".")
    display_grid(grid)

    n = 0
    while n < 50:
        grid = enhance_grid(grid, algorithm)
        grid = grow_grid(grid)
        n += 1

    # display_grid(grid)

    count = 0
    for point in grid:
        if grid[point] == "#":
            count += 1
    print(f"Count: {count}")



def day20b():
    day = "day20b"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    print(data)


# Main Function
def main():
    day = "20a"
    if len(sys.argv) > 1:
        day = sys.argv[1]
    eval(f"day{day}()")


if __name__ == "__main__":
    main()

