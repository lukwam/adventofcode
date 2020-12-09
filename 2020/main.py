#!/usr/bin/env python
"""Advent-of-Code 2020."""

# import json
import re
import sys

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


def main():
    """Main function."""
    if len(sys.argv):
        function = sys.argv[-1]
        globals()[function]()
    else:
        print("Hello World!")


if __name__ == "__main__":
    main()
