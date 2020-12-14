#!/usr/bin/env python
"""Advent-of-Code 2020."""

# import json
from datetime import datetime
import itertools
import json
import math
import re
import sys
import time

import helpers


#
# Day 1: Report Repair
#
def day1a():
    """Day 1: Report Repair."""
    items = helpers.get_input_integers("day1")
    for i in items:
        for j in items:
            if i == j:
                continue
            if i + j == 2020:
                break
        if i + j == 2020:
            break
    print(f"\nAnswer: {i} + {j} = 2020; {i} * {j} = {i * j}")


def day1b():
    """Day 1: Report Repair."""
    items = helpers.get_input_integers("day1")
    for i in items:
        for j in items:
            if i == j:
                continue
            for k in items:
                if i in [j, k]:
                    continue
                if i + j + k == 2020:
                    break
            if i + j + k == 2020:
                break
        if i + j + k == 2020:
            break
    print(f"\nAnswer: {i} + {j} + {k} = 2020; {i} * {j} * {k} = {i * j * k}")


#
# Day 2: Password Philosophy
#
def day2a():
    """Day 2: Password Philosophy."""
    items = helpers.get_input_strings("day2")
    valid = []
    for item in items:
        result = re.findall(r"^([0-9]+)-([0-9]+) (.): (.*)$", item)
        mincount, maxcount, character, password = result[0]
        count = 0
        for c in password:
            if c == character:
                count += 1
        if count >= int(mincount) and count <= int(maxcount):
            valid.append(password)
    print(f"\nValid Passwords: {len(valid)}")


def day2b():
    """Day 2: Password Philosophy."""
    items = helpers.get_input_strings("day2")
    valid = []
    for item in items:
        result = re.findall(r"^([0-9]+)-([0-9]+) (.): (.*)$", item)
        first, second, character, password = result[0]
        a = password[int(first) - 1]
        b = password[int(second) - 1]
        if (character in [a, b]) and a != b:
            valid.append(password)
    print(f"\nValid Passwords: {len(valid)}")


#
# Day 3: Toboggan Trajectory
#

def day3a():
    """Day 3: Toboggan Trajectory."""
    items = helpers.get_input_strings("day3")
    print(f"Total Items: {len(items)}")
    trees = helpers.check_slope(3, 1, items)
    print(f"\nTrees: {trees}")


def day3b():
    """Day 3: Toboggan Trajectory."""
    items = helpers.get_input_strings("day3")
    counts = []
    counts.append(helpers.check_slope(1, 1, items))
    counts.append(helpers.check_slope(3, 1, items))
    counts.append(helpers.check_slope(5, 1, items))
    counts.append(helpers.check_slope(7, 1, items))
    counts.append(helpers.check_slope(1, 2, items))
    result = 1
    for count in counts:
        result *= count
    print(f"\nResult: {result}")


#
# Day 4: Passport Processing
#
def day4a():
    """Day 4: Passport Processing."""
    valid = helpers.check_passports()
    print(f"\nValid: {len(valid)}")


def day4b():
    """Day 4: Passport Processing."""
    valid = helpers.check_passports(True)
    print(f"\nValid: {len(valid)}")


#
# Day 5: Binary Boarding
#
def day5a(output=True):
    """Day 5: Binary Boarding."""
    rowcount = 127
    colcount = 7

    seat_ids = []

    items = helpers.get_input_strings("day5")
    verbose = False
    for i in items:
        rowstring = i[:7]
        colstring = i[-3:]
        row = helpers.check_seat_row(rowstring, 0, rowcount, verbose=verbose)
        if verbose:
            print(f"Row: {row}\n")
        col = helpers.check_seat_col(colstring, 0, colcount, verbose=verbose)
        if verbose:
            print(f"Column: {col}\n")
        seat_id = (row * 8) + col
        seat_ids.append(seat_id)
        if verbose:
            print(f"{i}: row {row}, col {col}, seat ID {seat_id}")
    if output:
        print(f"\nMax Seat ID: {max(seat_ids)}")
    return seat_ids


def day5b():
    """Day 5: Binary Boarding."""
    seat_ids = day5a(output=False)
    expected = 0
    for seat_id in sorted(seat_ids):
        if expected:
            if seat_id != expected:
                print(f"\nMissing seat: {expected}")
        expected = seat_id + 1


#
# Day 6: Custom Customs
#
def day6a():
    """Day 6a."""
    items = helpers.get_input_strings("day6")
    counts = []
    group = None
    for i in items:
        if not i:
            counts.append(len(group))
            group = {}
        if not group:
            group = {}
        for c in list(i):
            if c in group:
                group[c] += 1
            else:
                group[c] = 1
    counts.append(len(group))
    total = 0
    for t in counts:
        total += t
    print(f"\nTotal: {total}")


def day6b():
    """Day 6a."""
    items = helpers.get_multiline_input("day6")
    total = 0
    for group in items:
        n = len(group)
        qs = {}
        for p in group:
            for c in p:
                if c not in qs:
                    qs[c] = 0
                qs[c] += 1
        for q in qs:
            if qs[q] == n:
                total += 1
    print(f"\nTotal: {total}")


#
# Day 7: Handy Haversacks
#
def day7a():
    """Day 7a."""
    check = "shiny gold"
    items = helpers.get_input_strings("day7")
    bags = helpers.get_bags(items)
    # print(json.dumps(bags, indent=2, sort_keys=True))
    valid = []
    print("\nValid colors:")
    for color in bags:
        if helpers.check_valid_bag(check, color, bags):
            valid.append(color)
            print(f"  {color}")
    print(f"\nTotal: {len(valid)}")


def day7b():
    """Day 7a."""
    check = "shiny gold"
    items = helpers.get_input_strings("day7")
    bags = helpers.get_bags(items)
    # print(json.dumps(bags, indent=2, sort_keys=True))
    total = helpers.count_bags(check, bags)
    print(f"\nTotal: {total}")


#
# Day 8: Handheld Halting
#
def day8a():
    """Day 8a."""
    items = helpers.get_input_strings("day8")
    accumulator = helpers.test_boot_code(items)
    print(f"\nAccumulator: {accumulator}")


def day8b():
    """Day 8a."""
    items = helpers.get_input_strings("day8")
    i = 0
    while i < len(items):
        code = items[i]
        inst, num = code.split(" ")
        test = False
        if inst == "jmp":
            new = "nop"
            newitems = list(items)
            newitems[i] = f"{new} {num}"
            test = True
        elif inst == "nop":
            new = "jmp"
            newitems = list(items)
            newitems[i] = f"{new} {num}"
            test = True
        if test:
            print(f"Testing row {i}: {inst} -> {new}")
            accumulator = helpers.test_boot_code(newitems)
            print(f"Accumulator: {accumulator}")
        i += 1


#
# Day 9:
#
def day9a():
    """Day 9a."""
    items = helpers.get_input_integers("day9")
    n = 0
    length = 25
    preamble = items[n:n + length]
    for item in items[length:]:
        helpers.check_encoding(preamble, item)
        n += 1
        preamble = items[n:n + length]


def day9b():
    """Day 9b."""
    items = helpers.get_input_integers("day9")
    value = 105950735
    length = 2
    while True:
        print(f"Length: {length}")
        start = 0
        end = length
        while end <= len(items):
            group = items[start:end]
            if sum(group) == value:
                print("SUCCESS!")
                print(group)
                weakness = min(group) + max(group)
                print(f"Weakness: {weakness} (length: {length}")
                sys.exit()
            start += 1
            end += 1
        length += 1


#
# Day 10
#
def day10a():
    """Day 10a."""
    items = helpers.get_input_integers("day10")
    device = max(items) + 3
    jolts = sorted(items) + [device]

    ones = 0
    threes = 0
    last = 0
    for n in jolts:
        diff = n - last
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
        else:
            print("ERROR: Bad diff!")
        last = n
    print(f"{ones} ones x {threes} threes = {ones * threes}")


def day10b():
    """Day 10a."""
    items = helpers.get_input_integers("day10")
    device = max(items) + 3
    jolts = [0] + sorted(items) + [device]

    matrix = []
    n = 0
    while n < len(jolts):
        i = jolts[n]
        group = [i]
        while n + 1 < len(jolts) and jolts[n + 1] == i + 1:
            n += 1
            i = jolts[n]
            group.append(i)
        n += 1
        matrix.append(group)

    factors = []
    for row in matrix:
        print(row)
        if len(row) < 3:
            factors.append(1)
        elif len(row) == 3:
            factors.append(2)
        elif len(row) == 4:
            factors.append(4)
        elif len(row) == 5:
            factors.append(7)
    print(factors)
    print(f"Arrangements: {math.prod(factors)}")


def print_rows(rows):
    """Print rows."""
    for row in rows:
        print(row)
    print("")


def day11a():
    """Day 11a: Seating System."""
    rows = helpers.get_input_strings("day11")
    length = len(rows)
    width = len(rows[0])
    print(f"Length: {length}, Width: {width}")
    print_rows(rows)

    limit = 4
    recurse = False

    done = False
    i = 0
    while not done:
        print(f"\nIteration {i}:\n")
        new_rows = helpers.perform_seating(rows, length, width, limit, recurse)
        print_rows(new_rows)
        if new_rows == rows:
            done = True
        rows = new_rows
        i += 1

    occupied = 0
    for row in rows:
        for c in row:
            if c == "#":
                occupied += 1

    print(f"Iterations: {i}")
    print(f"Occupied: {occupied}")


def day11b():
    """Day 11b Seating System."""
    rows = helpers.get_input_strings("day11")
    length = len(rows)
    width = len(rows[0])
    print(f"Length: {length}, Width: {width}")
    print_rows(rows)

    limit = 5
    recurse = True

    done = False
    i = 0
    while not done:
        print(f"\nIteration {i}:\n")
        new_rows = helpers.perform_seating(rows, length, width, limit, recurse)
        print_rows(new_rows)
        if new_rows == rows:
            done = True
        rows = new_rows
        i += 1

    occupied = 0
    for row in rows:
        for c in row:
            if c == "#":
                occupied += 1

    print(f"Iterations: {i}")
    print(f"Occupied: {occupied}")


def parse_action_a(loc, text):
    """Return the action."""
    a = text[0]
    v = int(text[1:])
    x, y, d = loc
    if a == "N":
        print(f"North {v}")
        y += v
    elif a == "S":
        print(f"South {v}")
        y -= v
    elif a == "E":
        print(f"East {v}")
        x += v
    elif a == "W":
        print(f"West {v}")
        x -= v
    elif a == "L":
        print(f"Left {v}")
        n = 0
        while n < v / 90:
            if d == "E":
                d = "N"
            elif d == "N":
                d = "W"
            elif d == "W":
                d = "S"
            elif d == "S":
                d = "E"
            n += 1
    elif a == "R":
        print(f"Right {v}")
        n = 0
        while n < v / 90:
            if d == "E":
                d = "S"
            elif d == "S":
                d = "W"
            elif d == "W":
                d = "N"
            elif d == "N":
                d = "E"
            n += 1
    elif a == "F":
        print(f"Forward {v}")
        if d == "E":
            x += v
        elif d == "S":
            y -= v
        elif d == "W":
            x -= v
        elif d == "N":
            y += v
    else:
        print(f"ERROR: Bad action: {a}")

    return (x, y, d)


def parse_action_b(loc, text):
    """Return the action."""
    action = text[0]
    value = int(text[1:])
    x, y, a, b = loc

    if action == "N":
        print(f"North {value}")
        y += value

    elif action == "S":
        print(f"South {value}")
        y -= value

    elif action == "E":
        print(f"East {value}")
        x += value

    elif action == "W":
        print(f"West {value}")
        x -= value

    elif action == "L":
        print(f"Left {value}")
        dx = x - a
        dy = y - b
        n = 0
        while n < value / 90:
            nx = -dy
            ny = dx
            dx = nx
            dy = ny
            n += 1
        x = a + dx
        y = b + dy
    elif action == "R":
        print(f"Right {value}")
        dx = x - a
        dy = y - b
        n = 0
        while n < value / 90:
            nx = dy
            ny = -dx
            dx = nx
            dy = ny
            n += 1
        x = a + dx
        y = b + dy

    elif action == "F":
        print(f"Forward {value}")
        dx = x - a
        dy = y - b
        a = a + dx * value
        b = b + dy * value
        x = x + dx * value
        y = y + dy * value

    else:
        print(f"ERROR: Bad action: {a}")

    return (x, y, a, b)


def day12a():
    """Day 12a: Rain Risk."""
    items = helpers.get_input_strings("day12")
    loc = (0, 0, "E")
    for item in items:
        loc = parse_action_a(loc, item)
    x, y, d = loc
    final = abs(x) + abs(y)
    print(f"Answer: {final}")


def day12b():
    """Day 12b: Rain Risk."""
    items = helpers.get_input_strings("day12")
    loc = (10, 1, 0, 0)
    for item in items:
        loc = parse_action_b(loc, item)
    x, y, a, b = loc
    print(f"\nWaypoint: {x}, {y}; Ship: {a}, {b}")
    answer = abs(a) + abs(b)
    print(f"\nAnswer: {answer}")


def day13a():
    """Day 13a."""
    items = helpers.get_input_strings("day13test")
    est = int(items[0])

    busmap = {}
    i = 0
    for x in items[1].split(","):
        if x != "x":
            busmap[int(x)] = i
        i += 1
    print(est, busmap)

    times = {}
    for b in busmap:
        n = round(est / b)
        t = b * n
        if t not in times:
            times[t] = []
        times[t].append(b)
        t = b * (n + 1)
        if t not in times:
            times[t] = []
        times[t].append(b)

    for t in sorted(times):
        if t >= est:
            b = times[t][0]
            w = t - est
            a = b * w
            print(f"Bus #{b} departs at {t}, which is {w} minutes wait: {b} * {w} = {a}.")
            print(f"Answer: {a}")
            break


def day13b():
    """Day 13b: Shuttle Search."""
    items = helpers.get_input_strings("day13")

    def get_valid_busses(t, busmap):
        """Return a list of busses that are valid for a given time."""
        valid = []
        for b in sorted(busmap, reverse=True):
            n = busmap[b]
            if b and (t + n) % b == 0:
                valid.append(b)
        return valid

    busmap = {}
    i = 0
    for x in items[1].split(","):
        if x != "x":
            busmap[int(x)] = i
        i += 1

    loop = 0
    # step = max(busmap)
    step = 1
    t = 0
    while True:
        loop += 1
        t += step
        v = get_valid_busses(t, busmap)
        print(f"{t}: {v}")
        if v:
            step = math.prod(v)
        if len(v) == len(busmap):
            break
    print(f"Loops: {loop}")


def day14a():
    """Day 14a."""
    lines = helpers.get_input_strings("day14")
    mask = []
    mem = {}
    print(f"Initialize memory: {mem}")

    def apply_mask(binary):
        """Apply the mask to a binary."""
        binary_list = []
        for i in list(binary):
            binary_list.append(int(i))
        n = 0
        for x in mask:
            if x != "X":
                binary_list[n] = x
            n += 1
        binary = ''.join([str(x) for x in binary_list])
        return binary

    def get_mask_string(mask):
        """Return the mask as a string."""
        return "".join([str(x) for x in mask])

    def save_value(integer, loc):
        """Apply the mask."""
        binary = '{0:036b}'.format(integer)
        print(f"value:   {binary}  (decimal {integer})")
        print(f"mask:    {get_mask_string(mask)}")
        result = apply_mask(binary)
        value = int(result, 2)
        print(f"result:  {result}  (decimal {value})")
        mem[loc] = value

    def get_mask(mask_string):
        """Set the mask."""
        mask = []
        maskmap = {}
        i = 0
        for c in list(mask_string):
            if c == "X":
                mask.append("X")
            else:
                mask.append(int(c))
                maskmap[int(c)] = i
            i += 1
        return mask

    for line in lines:
        print()
        print(line)

        if re.match(r"mask = .*", line):
            mask_string = line.replace("mask = ", "")
            mask = get_mask(mask_string)
            print(f"Initialize mask: {mask}")

        elif re.match(r"mem\[.*\] = .*", line):
            loc, integer = line.replace("mem[", "").replace("]", "").replace(" =", "").split(" ")
            save_value(int(integer), int(loc))

    print(f"Sum: {sum(mem.values())}")
    # print(mask)
    # print(mem)


def day14b():
    """Day 14b."""
    lines = helpers.get_input_strings("day14")
    mask = []
    mem = {}
    print(f"Initialize memory: {mem}")

    def apply_mask(location):
        """Apply the mask to a binary."""
        binary = '{0:036b}'.format(location)
        print(f"address: {binary}  (decimal {location})")
        binary_list = []
        for i in list(binary):
            binary_list.append(int(i))

        n = 0
        for x in mask:
            if x == 1:
                binary_list[n] = 1
            if x == "X":
                binary_list[n] = "X"
            n += 1
        result = ''.join([str(x) for x in binary_list])
        print(f"mask:    {get_mask_string(mask)}")
        print(f"result:  {result}")
        return result

    def get_permutations(n):
        """Return all the itertaions of 0 and 1 for n items."""
        bits = ["0", "1"]
        if n == 1:
            return bits
        permutations = []
        for x in get_permutations(n - 1):
            for y in bits:
                permutations.append(x + y)
        return permutations

    def get_locations(result):
        """Return a list of locations based on the floating bits in a result."""
        locations = []
        floats = []
        fmtstring = ""
        n = 0
        f = 0
        while n < len(result):
            x = result[n]
            if x == "X":
                floats.append(n)
                fmtstring += "%s"
                f += 1
            else:
                fmtstring += str(x)
            n += 1
        locations = []
        for p in get_permutations(len(floats)):
            binary = fmtstring % tuple(list(p))
            locations.append(int(binary, 2))
        return locations

    def get_mask_string(mask):
        """Return the mask as a string."""
        return "".join([str(x) for x in mask])

    def save_value(integer, result):
        """Apply the mask."""
        print(result, integer)
        locations = get_locations(result)
        for loc in locations:
            mem[loc] = integer

    def get_mask(mask_string):
        """Set the mask."""
        mask = []
        maskmap = {}
        i = 0
        for c in list(mask_string):
            if c == "X":
                mask.append("X")
            else:
                mask.append(int(c))
                maskmap[int(c)] = i
            i += 1
        return mask

    for line in lines:
        print()
        print(line)

        if re.match(r"mask = .*", line):
            mask_string = line.replace("mask = ", "")
            mask = get_mask(mask_string)
            print(f"Initialize mask: {mask}")

        elif re.match(r"mem\[.*\] = .*", line):
            loc, integer = line.replace("mem[", "").replace("]", "").replace(" =", "").split(" ")
            result = apply_mask(int(loc))
            save_value(int(integer), result)

    print(f"Sum: {sum(mem.values())}")


def main():
    """Main function."""
    if len(sys.argv):
        function = sys.argv[-1]
        startTime = datetime.now()
        globals()[function]()
        print(f"\nRuntime: {datetime.now() - startTime}")
    else:
        print("Hello World!")


if __name__ == "__main__":
    main()
