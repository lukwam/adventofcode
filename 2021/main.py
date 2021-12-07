#!/bin/python

import sys

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
    print(data)


def day8b():
    day = "day8b"
    print(f"Running {day}...")
    data = get_data_as_string(day)
    print(data)



# Main Function
def main():
    day = "8a"
    if len(sys.argv) > 1:
        day = sys.argv[1]
    eval(f"day{day}()")


if __name__ == "__main__":
    main()

