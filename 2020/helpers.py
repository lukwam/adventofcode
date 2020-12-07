"""Helpers."""

import re


#
# Input Helpers
#
def get_input_integers(name):
    """Return the puzzle input as a list of strings."""
    integers = []
    for line in get_input_strings(name):
        try:
            integers.append(int(line))
        except Exception as error:
            print(f"ERROR: Failed to convert string to integer: {line}!")
    return integers


def get_input_strings(name):
    """Return the puzzle input as a list of strings."""
    filename = f"{name}.txt"
    f = open(filename)
    lines = []
    for line in f.readlines():
        lines.append(line.strip())
    print(f"Found {len(lines)} lines in puzzle input: {filename}")
    return lines


def get_multiline_input(name):
    """Return the puzzle input as a list of lists of strings."""
    entries = []
    entry = []
    for row in get_input_strings(name):
        if not row:
            entries.append(entry)
            entry = []
            continue
        entry.append(row)
    # handle last entry
    if entry:
        entries.append(entry)
    print(f"Found {len(entries)} lines in puzzle input: {filename}")
    return entries


#
# Toboggan
#
def check_slope(right, down, items):
    """Check a slope."""
    cols = len(items) * right
    r = 0
    c = 0
    trees = 0
    while r < len(items):
        row = items[r]
        orig = str(row)
        while len(row) < cols:
            row += orig
        if r == 0:
            r += down
            c += right
            continue
        slist = list(row)
        i = slist[c]
        if i == "#":
            trees += 1
            slist[c] = "X"
        else:
            slist[c] = "O"
        row = ''.join(slist)
        r += down
        c += right
    return trees


#
# Passports
#
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
    items = get_input_strings("day4")
    passports = []
    passport = {}

    for i in items:
        if not i:
            passports.append(passport)
            passport = {}
            continue
        for key in i.split(" "):
            k, v = key.split(":")
            passport[k] = v
    if passport:
        passports.append(passport)

    valids = []
    for p in passports:
        valid = True

        diff = set(list(fields)) - set(list(p))

        if diff:
            valid = False
            # print(f"  missing: {list(diff)}")

        elif validate:

            # byr (Birth Year) - four digits; at least 1920 and at most 2002.
            if int(p["byr"]) < 1920 or int(p["byr"]) > 2002:
                # print(f"  - byr: {p['byr']}")
                valid = False

            # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            if int(p["iyr"]) < 2010 or int(p["iyr"]) > 2020:
                # print(f"  - iyr: {p['iyr']}")
                valid = False

            # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            if int(p["eyr"]) < 2020 or int(p["eyr"]) > 2030:
                # print(f"  - eyr: {p['eyr']}")
                valid = False

            # hgt (Height) - a number followed by either cm or in:
            #     If cm, the number must be at least 150 and at most 193.
            #     If in, the number must be at least 59 and at most 76.
            if not re.match(r"[0-9a-f]+(cm|in)$", p["hgt"]):
                # print(f"  - hgt: {p['hgt']}")
                valid = False
            else:
                units = p["hgt"][-2:]
                height = int(p["hgt"][:-2])
                if units == "cm":
                    if height < 150 or height > 193:
                        # print(f"  - hgt: {p['hgt']}")
                        valid = False
                elif units == "in":
                    if height < 59 or height > 76:
                        # print(f"  - hgt: {p['hgt']}")
                        valid = False
                else:
                    # print(f"  - hgt: {p['hgt']}")
                    valid = False

            # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            if not re.match(r"#[0-9a-f]{6}$", p["hcl"]):
                # print(f"  - hcl: {p['hcl']}")
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
                # print(f"  - ecl: {p['ecl']}")
                valid = False

            # pid (Passport ID) - a nine-digit number, including leading zeroes.
            if not re.match(r"[0-9]{9}$", p["pid"]):
                # print(f"  - pid: {p['pid']}")
                valid = False

            # cid (Country ID) - ignored, missing or not.

        if valid:
            valids.append(p)

    return valids


#
# Boarding
#
def check_seat_row(string, rmin, rmax, verbose=False):
    """Check the row."""
    size = rmax - rmin + 1
    half = int(size / 2)
    rmid = rmin + half
    chars = list(string)
    first = chars[0]
    if first == "F":
        if verbose:
            print(f"take the lower half, keeping rows {rmin} through {rmid - 1}")
        if len(chars) == 1:
            return rmin
        return check_seat_row("".join(string[1:]), rmin, rmid - 1, verbose)
    elif first == "B":
        if verbose:
            print(f"take the upper half, keeping rows {rmid} through {rmax}")
        if len(chars) == 1:
            return rmax
        return check_seat_row("".join(string[1:]), rmid, rmax, verbose)
    else:
        print(f"ERROR: Bad character!")


def check_seat_col(string, cmin, cmax, verbose=False):
    """Check the seat column."""
    size = cmax - cmin + 1
    half = int(size / 2)
    cmid = cmin + half
    chars = list(string)
    first = chars[0]
    if first == "L":
        if len(chars) == 1:
            return cmin
        if verbose:
            print(f"take the lower half, keeping columns {cmin} through {cmid - 1}")
        return check_seat_col("".join(string[1:]), cmin, cmid - 1)
    elif first == "R":
        if len(chars) == 1:
            return cmax
        if verbose:
            print(f"take the upper half, keeping columns {cmid} through {cmax}")
        return check_seat_col("".join(string[1:]), cmid, cmax)
    else:
        print(f"ERROR: Bad character!")


#
# Bags
#
def get_bags(rules):
    """Return a dict of bags from the input rules."""
    bags = {}
    for rule in rules:
        result = re.findall(r"^(.*) bags contain (.*)$", rule)
        color = result[0][0]
        contents = result[0][1]
        bags[color] = {}
        if contents == "no other bags.":
            continue
        for bag in contents.split(","):
            bag = bag.strip().strip(".")
            bag_count = bag.split(" ")[0]
            bag_color = " ".join(bag.split(" ")[1:-1])
            bags[color][bag_color] = bag_count
    return bags


def check_valid_bag(check, color, bags):
    """Return True if bag can contain a bag of check color."""
    if check in bags[color]:
        return True
    for c in bags[color]:
        if check_valid_bag(check, c, bags):
            return True


def count_bags(color, bags, indent=0):
    """Count the bags contained in the given bag."""
    count = 0
    if not bags[color]:
        return count
    for c in bags[color]:
        n = int(bags[color][c])
        count += n
        print(f"{'  ' * indent}{n} {c} bag(s)")
        subcount = count_bags(c, bags, indent + 1)
        count += n * subcount
    return count