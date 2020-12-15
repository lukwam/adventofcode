"""Advent of Code 2019."""
import math
import re
import sys

import helpers


def get_entries(name):
    """Get entries separated by blank lines."""
    entries = []
    entry = []
    for i in get_str_input(name):
        if not i:
            entries.append(entry)
            entry = []
            continue
        entry.append(i)
    if entry:
        entries.append(entry)
    return entries


def get_int_input(name):
    """Get integer input from a multi-line text file."""
    f = open(f"{name}.txt")
    items = []
    for i in f.readlines():
        items.append(int(i))
    return items


def get_str_input(name):
    """Get integer input from a multi-line text file."""
    f = open(f"{name}.txt")
    items = []
    for i in f.readlines():
        items.append(i.strip())
    return items


def calculate_fuel(n):
    """Calculate fuel requirements."""
    return  math.floor(n / 3) - 2


def day1a():
    """Day 1a."""
    items = get_str_input("day1")
    total = 0
    for i in items:
        num = int(i)
        value = calculate_fuel(num)
        total += value
    print(f"Total: {total}")


def day1b():
    """Day 1a."""
    items = get_str_input("day1")
    total = 0
    for i in items:
        num = int(i)
        value = calculate_fuel(num)
        # print(value)
        while value > 0:
            # print(value)
            total += value
            value = calculate_fuel(value)
    print(f"Total: {total}")


class Computer:
    """Computer class."""

    def __init__(self, intcode, verbose=False):
        """Initialize a computer."""
        self.memory = []
        for i in intcode.split(","):
            self.memory.append(int(i))
        print(f"Memory: {self.memory}")
        self.verbose = verbose

    def add(self, a, b, c):
        """Add two numbers a and b and store value in c."""
        x = self.memory[a]
        y = self.memory[b]
        self.memory[c] = x + y
        if self.verbose:
            print(f"{x} + {y} = {x + y} => {c}")

    def multiply(self, a, b, c):
        """Multiply two numbers a and b and store value in c."""
        x = self.memory[a]
        y = self.memory[b]
        self.memory[c] = x * y
        if self.verbose:
            print(f"{x} * {y} = {x * y} => {c}")

    def run(self, noun, verb):
        """Run the program."""
        self.memory[1] = noun
        self.memory[2] = verb
        i = 0
        while True:
            opcode = self.memory[i]
            print(f"Position: {i}, Opcode: {opcode}")

            if opcode == 1:
                print(self.memory)
                a = self.memory[i + 1]
                print(f"{a}, {i + 1}")
                b = self.memory[i + 2]
                print(f"{b}, {i + 2}")
                c = self.memory[i + 3]
                print(f"{c}, {i + 3}")
                self.add(a, b, c)
                i += 4
            elif opcode == 2:
                a = self.memory[i + 1]
                b = self.memory[i + 2]
                c = self.memory[i + 3]
                self.multiply(a, b, c)
                i += 4
            elif opcode == 99:
                print("Exiting.")
                return

            print(f"Memory: {self.memory}")


def day2a():
    """Day 2a."""
    intcode = get_str_input("day2")[0]
    noun = 12
    verb = 2
    computer = Computer(intcode)
    computer.run(noun, verb)
    print(f"Output: {computer.memory[0]}")


def day2b():
    """Day 2b."""
    output = 19690720
    intcode = get_str_input("day2")[0]

    for noun in range(0, 100):
        for verb in range(0, 100):
            print(f"Noun: {noun}, Verb: {verb}")
            computer = Computer(intcode)
            computer.run(noun, verb)
            print(f"Output: {computer.memory[0]}")
            if computer.memory[0] == output:
                print("Found the answer!")
                print(f"Noun: {noun}, Verb: {verb}")
                answer = 100 * noun + verb
                print(f"Answer: {answer}")
                return


def create_path(path):
    """Draw the path for a circuit."""
    instructions = path.split(",")
    pathmap = {}
    start = (0, 0)
    current = start
    pathmap[start] = "o"
    for i in instructions:
        dir = i[0]
        dist = int(i[1:])

        if dir == "R":
            n = 0
            while n < dist:
                char = "-"
                if n == dist - 1:
                    char = "+"
                current = (current[0] + 1, current[1])
                pathmap[current] = char
                n += 1

        elif dir == "L":
            n = 0
            while n < dist:
                char = "-"
                if n == dist - 1:
                    char = "+"
                current = (current[0] - 1, current[1])
                pathmap[current] = char
                n += 1

        elif dir == "U":
            n = 0
            while n < dist:
                char = "|"
                if n == dist - 1:
                    char = "+"
                current = (current[0], current[1] + 1)
                pathmap[current] = char
                n += 1

        elif dir == "D":
            n = 0
            while n < dist:
                char = "|"
                if n == dist - 1:
                    char = "+"
                current = (current[0], current[1] + - 1)
                pathmap[current] = char
                n += 1

    return pathmap


def draw_path(pathmap):
    """Draw a path."""
    xmax = 0
    xmin = 0
    ymax = 0
    ymin = 0

    for c in pathmap:
        # print(c)
        x = c[0]
        y = c[1]
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y

    # topright = max(pathmap)
    # bottomleft = min(pathmap)
    # print(bottomleft, topright)
    # print(pathmap)

    # x0 = topright[0]
    # x1 = bottomleft[0]
    width = xmax - xmin
    xrange = range(xmin, xmax + 1)
    # print(list(xrange))

    # y0 = topright[1]
    # y1 = bottomleft[1]
    yrange = range(ymax, ymin - 1, -1)
    # print(list(yrange))
    # length = y0 - y1

    blank = ["."] * (width + 3)
    rows = [blank]

    # print(x
    # range)

    for y in yrange:
        row = ["."]
        for x in xrange:
            c = (x, y)
            if c in pathmap:
                v = pathmap[c]
                row.append(v)
            else:
                row.append(".")
        row.append(".")
        rows.append(row)
    rows.append(blank)

    for row in rows:
        print(''.join(row))


def merge_paths(first_path, second_path):
    """Merge two paths and return the new map."""
    path = {}
    for c in first_path:
        if c not in path:
            path[c] = first_path[c]

    for c in second_path:
        if c not in path:
            path[c] = second_path[c]
        elif path[c] == second_path[c]:
            continue
        else:
            # check = path[c]
            # new = second_path[c]
            # # print(f"{check} != {new}")
            path[c] = "X"

    return path


def get_distance(a, b):
    """Return the distnce between two points."""
    x = abs(b[0] - a[0])
    y = abs(b[1] - a[1])
    return x + y


def day3a():
    """Day 3a."""
    items = get_str_input("day3")
    first = items[0]
    second = items[1]
    first_path = create_path(first)
    second_path = create_path(second)

    # draw_path(first_path)
    print("")
    # draw_path(second_path)
    print("")
    path = merge_paths(first_path, second_path)
    # draw_path(path)

    start = None
    for c in path:
        v = path[c]
        if v == "o":
            start = c

    print(f"Start: {start}")

    distances = []
    for c in path:
        v = path[c]
        if v == "X":
            dist = get_distance(start, c)
            distances.append(dist)

    print(f"Distance: {min(distances)}")

def day3b():
    """Day 3b."""


def day4a():
    """Day 4."""
    items = helpers.get_input_strings("day4")
    start, stop = items[0].split("-")
    print(start, stop)

    count = 0
    for i in range(int(start), int(stop) + 1):
        string = str(i)

        valid = False
        for c in [str(x) for x in range(0, 10)]:
            if c * 2 in string and c * 3 not in string:
                valid = True
        if not valid:
            continue

        # check for sorted
        if list(string) != sorted(string):
            continue

        print(i)
        count += 1
    print(f"Count: {count}")


def main():
    """Main function."""
    if len(sys.argv) > 1:
        function = sys.argv[1]
        globals()[function]()
    else:
        print("Hello World!")


if __name__ == "__main__":
    main()
