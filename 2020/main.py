#!/usr/bin/env python

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


def day1b(verbose=False):
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
    items = helpers.get_input_strings("day6")
    counts = []
    group = {}
    count = 0
    num = 0
    people = 0
    for i in items:
        people += 1
        if not i:
            tot = people - 1
            for g in group:
                if group[g] == tot:
                    count += 1
            counts.append(count)
            count = 0
            group = {}
            num = 0
            people = 0
        for c in list(i):
            num += 1
            if c in group:
                group[c] += 1
            else:
                group[c] = 1

    counts.append(people)
    total = 0
    for t in counts:
        total += t
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


def main():
    """Main function."""
    if len(sys.argv):
        function = sys.argv[-1]
        globals()[function]()
    else:
        print("Hello World!")


if __name__ == "__main__":
    main()
