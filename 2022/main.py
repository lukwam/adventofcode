#!/bin/python
"""Advent of Code - 2022"""
import json
import os
import sys

datadir = "data"

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def get_data_as_string(day):
    """Return the data for day as a string."""
    f = open(f"{datadir}/{day}.txt")
    return f.read()


def get_data_as_list(day):
    f = open(f"{datadir}/{day}.txt")
    return f.read().split("\n")


# Day 1
def day1():
    day = "day1a"
    print(f"Running {day}...")
    data = get_data_as_list(day)
    elves = []

    elf = 0
    for value in data:
        if not value:
            elves.append(elf)
            elf = 0
        else:
            elf += int(value)

    print(f"Top Elf: {max(elves)}")
    print(f"Top 3 Elves: {sum(sorted(elves)[-3:])}")


# Day 2
def day2a():
    day = "day2a"
    print(f"Running {day}...")
    data = get_data_as_list(day)

    scores = {
        "A X": 1 + 3,
        "A Y": 2 + 6,
        "A Z": 3 + 0,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 1 + 6,
        "C Y": 2 + 0,
        "C Z": 3 + 3,
    }

    total = 0
    for game in data:
        if game not in scores:
            print(f"ERROR: {game}")
        else:
            total += scores[game]
    print(f"Total Score: {total}")


def day2b():
    day = "day2a"
    print(f"Running {day}...")
    data = get_data_as_list(day)

    scores = {
        "A X": 3 + 0,
        "A Y": 1 + 3,
        "A Z": 2 + 6,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 2 + 0,
        "C Y": 3 + 3,
        "C Z": 1 + 6,
    }

    total = 0
    for game in data:
        if game not in scores:
            print(f"ERROR: {game}")
        else:
            total += scores[game]
    print(f"Total Score: {total}")


def day3a():
    day = "day3a"
    print(f"Running {day}...")
    data = get_data_as_list(day)

    alpha = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    total = 0
    for sack in data:
        l = int(len(sack)/2)
        c1 = sack[:l]
        c2 = sack[l:]
        i = (set([*c1]) & set([*c2])).pop()
        total += alpha.index(i)

    print(f"Total: {total}")


def day3b():
    day = "day3a"
    print(f"Running {day}...")
    data = get_data_as_list(day)

    alpha = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    total = 0
    for group in chunks(data, 3):
        c1, c2, c3 = group
        i = (set([*c1]) & set([*c2]) & set([*c3])).pop()
        total += alpha.index(i)

    print(f"Total: {total}")


def day4a():
    day = "day4a"
    print(f"Running {day}...")
    data = get_data_as_list(day)

    def range_subset(range1, range2):
        """Whether range1 is a subset of range2."""
        if set(range1).issubset(set(range2)):
            return True
        return False

    count = 0
    for row in data:
        a, b = row.split(",")
        a1, a2 = a.split("-")
        b1, b2 = b.split("-")
        arange = range(int(a1), int(a2)+1)
        brange = range(int(b1), int(b2)+1)
        if range_subset(arange, brange) or range_subset(brange, arange):
            count += 1
    print(f"Count: {count}")


def day4b():
    day = "day4a"
    print(f"Running {day}...")
    data = get_data_as_list(day)

    count = 0
    for row in data:
        a, b = row.split(",")
        a1, a2 = a.split("-")
        b1, b2 = b.split("-")
        arange = range(int(a1), int(a2)+1)
        brange = range(int(b1), int(b2)+1)
        if set(arange) & set(brange):
            count += 1
    print(f"Count: {count}")


def day5a():
    day = "day5a"
    print(f"Running {day}...")
    data = get_data_as_list(day)

    body = False
    header = []
    proc = []
    for row in data:
        if not row:
            body = True
            continue
        if body:
            proc.append(row)
        else:
            header.append(row)

    stackdata = {}
    header.reverse()
    stackrow = header[0]
    stacks = stackrow.strip().split("   ")
    for stack in stacks:
        i = stackrow.index(stack)
        stackdata[stack] = []
        for row in header[1:]:
            if i < len(row):
                v = row[i]
                if v != " ":
                    stackdata[stack].append(v)

    def move(count, a, b):
        n = 0
        while n < count:
            n += 1
            i = stackdata[a].pop()
            stackdata[b].append(i)

    for row in proc:
        _, count, _, source, _, dest = row.split(" ")
        move(int(count), source, dest)
    # print(json.dumps(stackdata, indent=2, sort_keys=True))

    output = []
    for key in sorted(stackdata):
        value = stackdata[key][-1]
        print(f"{key}: {value}")
        output.append(value)
    print("".join(output))



def day5b():
    day = "day5a"
    print(f"Running {day}...")
    data = get_data_as_list(day)

    body = False
    header = []
    proc = []
    for row in data:
        if not row:
            body = True
            continue
        if body:
            proc.append(row)
        else:
            header.append(row)

    stackdata = {}
    header.reverse()
    stackrow = header[0]
    stacks = stackrow.strip().split("   ")
    for stack in stacks:
        i = stackrow.index(stack)
        stackdata[stack] = []
        for row in header[1:]:
            if i < len(row):
                v = row[i]
                if v != " ":
                    stackdata[stack].append(v)

    def move(count, a, b):
        n = 0
        items = []
        while n < count:
            n += 1
            i = stackdata[a].pop()
            items.append(i)
        items.reverse()
        for item in items:
            stackdata[b].append(item)

    for row in proc:
        _, count, _, source, _, dest = row.split(" ")
        move(int(count), source, dest)
    # print(json.dumps(stackdata, indent=2, sort_keys=True))

    output = []
    for key in sorted(stackdata):
        value = stackdata[key][-1]
        print(f"{key}: {value}")
        output.append(value)
    print("".join(output))


def day6a():
    day = "day6a"
    print(f"Running {day}...")
    data = get_data_as_string(day)

    check = []
    n = 0
    for char in [*data]:
        n += 1
        if len(check) == 4:
            check.pop(0)
        check.append(char)
        if len(check) == 4 and len(set(check)) == 4:
            break

    print(f"Index: {n}")

def day6b():
    day = "day6a"
    print(f"Running {day}...")
    data = get_data_as_string(day)

    check = []
    n = 0
    for char in [*data]:
        n += 1
        if len(check) == 14:
            check.pop(0)
        check.append(char)
        if len(check) == 14 and len(set(check)) == 14:
            break

    print(f"Index: {n}")


def day7a():
    day = "day7a"
    print(f"Running {day}...")
    data = get_data_as_list(day)

    print(os.getcwd())
    basedir = "./day7/"
    os.chdir(basedir)
    print(os.getcwd())
    listing = False
    files = []
    for row in data:
        if row == "$ ls":
            continue
        elif row == "$ cd /":
            continue
        elif row.startswith("dir "):
            path = row.split(" ")[1]
            # print(f"mkdir {path}")
            os.mkdir(path)
        elif row == "$ cd ..":
            # print(f"cd ..")
            os.chdir("..")
            # print(os.getcwd())
        elif row.startswith("$ cd "):
            path = row.split(" ")[2]
            # print(f"cd {path}")
            os.chdir(path)
            # print(os.getcwd())
        else:
            size, name = row.split(" ")
            f = open(name, "wb")
            f.seek(int(size)-1)
            f.write(b"\0")
            f.close()


def day8a():
    day = "day8a"
    print(f"Running {day}...")
    data = get_data_as_list(day)
    print(data)

    cols = len(data[0])
    rows = len(data)
    print(f"Dimensions: {cols} x {rows}")

    trees = []
    visible = {}

    # from top
    x = 0
    while x < cols:
        m = 0
        y = 0
        while y < rows:
            row = data[y]
            i = (x, y)
            val = row[x]
            if y == 0 or val > m:
                visible[i] = val
                m = val
            y += 1
        x += 1

    # from left
    y = 0
    while y < rows:
        m = 0
        x = 0
        while x < cols:
            row = data[y]
            i = (x, y)
            val = row[x]
            if x == 0 or val > m:
                visible[i] = val
                m = val
            x += 1
        y += 1

    # from left
    y = 0
    while y < rows:
        m = 0
        x = cols - 1
        while x > 0:
            row = data[y]
            i = (x, y)
            val = row[x]
            if x == cols - 1 or val > m:
                visible[i] = val
                m = val
            x -= 1
        y += 1

    # from bottom
    x = 0
    while x < cols:
        m = 0
        y = rows - 1
        while y > 0:
            row = data[y]
            i = (x, y)
            val = row[x]
            if y == rows - 1 or val > m:
                visible[i] = val
                m = val
            y -= 1
        x += 1

    print(visible)
    print(len(visible))


def day8b():
    day = "day8a"
    print(f"Running {day}...")
    data = get_data_as_list(day)
    print(data)

    cols = len(data[0])
    rows = len(data)
    print(f"Dimensions: {cols} x {rows}")

    def check_score(i):
        x, y = i

        if x == 0:
            return 0
        if y == 0:
            return 0
        if x == cols - 1:
            return 0
        if y == rows - 1:
            return 0

        # north

        # south

        # east

        # west


# Main Function
def main():
    day = "8b"
    if len(sys.argv) > 1:
        day = sys.argv[1]
    eval(f"day{day}()")


if __name__ == "__main__":
    main()
