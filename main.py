#!/usr/bin/env python

import re
import sys


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


def day1a():
    """Day 1: Report Repair."""
    items = get_int_input("day1")
    for i in items:
        for j in items:
            if i == j:
                continue
            if i + j == 2020:
                break
        if i + j == 2020:
            break
    print(f"{i} + {j} = 2020; {i} * {j} = {i * j}")


def day1b():
    """Day 1: Report Repair."""
    items = get_int_input("day1")
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
    print(f"{i} + {j} + {k} = 2020; {i} * {j} * {k} = {i * j * k}")


def day2a():
    """Day 2: Password Philosophy."""
    items = get_str_input("day2")
    valid = []
    for i in items:
        parts = i.split(" ")
        mincount, maxcount = parts[0].split("-")
        character = parts[1].strip(":")
        string = parts[2]
        # print(mincount, maxcount, character, string)

        count = 0
        for c in string:
            if c == character:
                count += 1
        if count >= int(mincount) and count <= int(maxcount):
            valid.append(string)
    print(f"Valid Passwords: {len(valid)}")


def day2b():
    """Day 2: Password Philosophy."""
    items = get_str_input("day2")
    valid = []
    for i in items:
        parts = i.split(" ")
        first, second = parts[0].split("-")
        first = int(first) - 1
        second = int(second) - 1
        character = parts[1].strip(":")
        string = parts[2]
        a = string[first]
        b = string[second]
        if (character in [a, b]) and a != b:
            valid.append(string)

    print(f"Valid Passwords: {len(valid)}")


def check_slope(right, down, items):
    """Check a slope."""
    cols = len(items) * right
    print(f"Columns: {cols}")

    r = 0
    c = 0

    trees = 0

    while r < len(items):
        row = items[r]

        orig = str(row)

        # expand string
        while len(row) < cols:
            row += orig

        # don't do anything on first row
        if r == 0:
            print(row)
            r += down
            c += right
            continue

        # split string
        slist = list(row)
        i = slist[c]

        # check for trees
        if i == "#":
            trees += 1
            slist[c] = "X"
        else:
            slist[c] = "O"

        # rejoin string
        row = ''.join(slist)
        print(row)
        r += down
        c += right

    return trees


def day3a():
    """Day 3: Toboggan Trajectory."""
    items = get_str_input("day3")
    print(f"Total Items: {len(items)}")
    trees = check_slope(3, 1, items)
    print(f"Trees: {trees}")


def day3b():
    """Day 3: Toboggan Trajectory."""
    items = get_str_input("day3")
    print(f"Total Items: {len(items)}")
    counts = []
    counts.append(check_slope(1, 1, items))
    counts.append(check_slope(3, 1, items))
    counts.append(check_slope(5, 1, items))
    counts.append(check_slope(7, 1, items))
    counts.append(check_slope(1, 2, items))
    print(counts)
    result = 1
    for count in counts:
        result *= count
    print(f"Result: {result}")


def check_passports(validate=False):
    """Day 4: Passport Processing."""
    fields = {
        "byr": "Birth Year",
        "iyr": "Issue Year",
        "eyr": "Expiration Year",
        "hgt": "Height",
        "hcl": "Hair Color",
        "ecl": "Eye Color",
        "pid": "Passport ID",
        # "cid": "Country ID",
    }
    items = get_str_input("day4")
    passports = []
    passport = {}

    for i in items:
        if i:
            for key in i.split(" "):
                k, v = key.split(":")
                passport[k] = v
        else:
            passports.append(passport)
            passport = {}
    if passport:
        passports.append(passport)

    valids = []
    for p in passports:
        print(p)
        valid = True

        diff = set(list(fields)) - set(list(p))

        if diff:
            print(f"  missing: {list(diff)}")
            continue

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if int(p["byr"]) < 1920 or int(p["byr"]) > 2002:
            print(f"  - byr: {p['byr']}")
            valid = False

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if int(p["iyr"]) < 2010 or int(p["iyr"]) > 2020:
            print(f"  - iyr: {p['iyr']}")
            valid = False

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if int(p["eyr"]) < 2020 or int(p["eyr"]) > 2030:
            print(f"  - eyr: {p['eyr']}")
            valid = False

        # hgt (Height) - a number followed by either cm or in:
        #     If cm, the number must be at least 150 and at most 193.
        #     If in, the number must be at least 59 and at most 76.
        if not re.match(r"[0-9a-f]+(cm|in)$", p["hgt"]):
            print(f"  - hgt: {p['hgt']}")
            valid = False
        else:
            units = p["hgt"][-2:]
            height = int(p["hgt"][:-2])
            if units == "cm":
                if height < 150 or height > 193:
                    print(f"  - hgt: {p['hgt']}")
                    valid = False
            elif units == "in":
                if height < 59 or height > 76:
                    print(f"  - hgt: {p['hgt']}")
                    valid = False
            else:
                print(f"  - hgt: {p['hgt']}")
                valid = False

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if not re.match(r"#[0-9a-f]{6}$", p["hcl"]):
            print(f"  - hcl: {p['hcl']}")
            valid = False

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if p["ecl"] not in [
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth",
        ]:
            print(f"  - ecl: {p['ecl']}")
            valid = False

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if not re.match(r"[0-9]{9}$", p["pid"]):
            print(f"  - pid: {p['pid']}")
            valid = False

        # cid (Country ID) - ignored, missing or not.

        if valid:
            valids.append(p)

    print(f"Valid: {len(valids)}")


def day4a():
    """Day 4: Passport Processing."""
    check_passports()


def day4b():
    """Day 4: Passport Processing."""
    check_passports(True)


def check_seat_row(string, rmin, rmax):
    """Check the row."""
    size = rmax - rmin + 1
    half = int(size / 2)
    rmid = rmin + half
    chars = list(string)
    first = chars[0]
    if first == "F":
        # print(f"take the lower half, keeping rows {rmin} through {rmid - 1}")
        if len(chars) == 1:
            return rmin
        return check_seat_row("".join(string[1:]), rmin, rmid - 1)
    elif first == "B":
        # print(f"take the upper half, keeping rows {rmid} through {rmax}")
        if len(chars) == 1:
            return rmax
        return check_seat_row("".join(string[1:]), rmid, rmax)
    else:
        print(f"ERROR: Bad character!")


def check_seat_col(string, cmin, cmax):
    """Check the seat column."""
    size = cmax - cmin + 1
    half = int(size / 2)
    cmid = cmin + half
    chars = list(string)
    first = chars[0]
    if first == "L":
        if len(chars) == 1:
            return cmin
        # print(f"take the lower half, keeping rows {cmin} through {cmid - 1}")
        return check_seat_col("".join(string[1:]), cmin, cmid - 1)
    elif first == "R":
        if len(chars) == 1:
            return cmax
        # print(f"take the upper half, keeping rows {cmid} through {cmax}")
        return check_seat_col("".join(string[1:]), cmid, cmax)
    else:
        print(f"ERROR: Bad character!")


def day5a():
    """Day 5: Binary Boarding."""
    rowcount = 127
    colcount = 7

    seat_ids = []

    items = get_str_input("day5")
    for i in items:
        rowstring = i[:7]
        colstring = i[-3:]
        row = check_seat_row(rowstring, 0, rowcount)
        # print(f"Row: {row}\n")
        col = check_seat_col(colstring, 0, colcount)
        # print(f"Column: {col}\n")
        seat_id = (row * 8) + col
        seat_ids.append(seat_id)
        print(f"{i}: row {row}, col {col}, seat ID {seat_id}")
    print(f"Max Seat ID: {max(seat_ids)}")

    expected = 0
    for seat_id in sorted(seat_ids):
        if expected:
            if seat_id != expected:
                print(f"Missing seat: {expected}")
        expected = seat_id + 1

def main():
    """Main function."""
    if len(sys.argv) > 1:
        function = sys.argv[1]
        globals()[function]()
    else:
        print("Hello World!")


if __name__ == "__main__":
    main()
