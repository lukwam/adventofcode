"""Helpers."""

import re
import sys


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
            print(error)
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
    print(f"Found {len(entries)} entries in puzzle input.")
    return entries


def print_rows(rows):
    """Print rows."""
    for row in rows:
        print(row)
    print("")


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
        print("ERROR: Bad character!")


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
        print("ERROR: Bad character!")


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


#
# Halting
#
def test_boot_code(items):
    """Test handheld game console boot code."""
    accumulator = 0
    done = False
    n = 0
    executed = []
    while not done:
        if n == len(items):
            print("Exited successfully!")
            print(accumulator)
            sys.exit()
        if n in executed:
            print("ERROR: Infinite loop!")
            return accumulator
        executed.append(n)
        code = items[n]
        inst, num = code.split(" ")
        num = int(num)
        if inst == "acc":
            print(f"add {num}")
            accumulator += num
            n += 1
        elif inst == "jmp":
            print(f"jump {num}")
            n += num
        elif inst == "nop":
            print("do nothing")
            n += 1


#
# Encoding
#
def check_encoding(preamble, value):
    """Check a single value for validity."""
    sums = {}
    for i in preamble:
        for j in preamble:
            if i == j:
                continue
            s = i + j
            if s not in sums:
                sums[s] = []
            sums[s].append([i, j])
    if value not in sums:
        print(f"ERROR: Invalid entry: {value}")


#
# Seating System
#
def check_seat_state(row, col, data, length, width, limit, recurse=False):
    """Check the state of a seat."""
    seat = list(data[row])[col]
    if seat == ".":
        return seat

    if recurse:
        recurse = max(length, width)
        recurse = 100
    else:
        recurse = 1

    occupied = 0
    for dir in ["nw", "n", "ne", "w", "e", "sw", "s", "se"]:
        if check_direction(dir, row, col, length, width, data, recurse=recurse):
            occupied += 1

    if seat == "L" and not occupied:
        return "#"

    if seat == "#" and occupied >= limit:
        return "L"

    return seat


def check_direction(dir, row, col, length, width, data, recurse=1):
    """Check if there is a seat in the given direction."""
    if dir == "nw":
        r = -1
        c = -1

    elif dir == "n":
        r = -1
        c = 0

    elif dir == "ne":
        r = -1
        c = 1

    elif dir == "w":
        r = 0
        c = -1

    elif dir == "e":
        r = 0
        c = 1

    elif dir == "sw":
        r = 1
        c = -1

    elif dir == "s":
        r = 1
        c = 0

    elif dir == "se":
        r = 1
        c = 1

    dist = 1
    while (
        (row + (r * dist) >= 0) and (row + (r * dist) < length) and
        (col + (c * dist) >= 0) and (col + (c * dist) < width) and
        dist <= recurse
    ):
        r1 = row + (r * dist)
        c1 = col + (c * dist)
        char = data[r1][c1]
        # print(r1, c1, char)
        if char == "#":
            return True
        elif char == "L":
            return False
        dist += 1
    return False


def perform_seating(data, length, width, limit, recurse):
    """Do one round of seating."""
    new = list(data)
    r = 0
    while r < length:
        c = 0
        cols = list(data[r])
        while c < width:
            cols[c] = check_seat_state(r, c, data, length, width, limit, recurse)
            c += 1
        new[r] = "".join(cols)
        r += 1
    return new


#
# Rain Risk
#
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


#
# Rambunctious Recitation
#
def speak_numbers(items, final):
    """Speak numbers in the sequence."""
    smap = {}
    last = None
    n = 1
    for i in items:
        i = int(i)
        smap[i] = [n]
        last = i
        n += 1
    while n <= final:
        if not n % 100000:
            print(n)
        if last in smap and len(smap[last]) == 1:
            i = 0
        else:
            old = smap[last].pop(0)
            i = n - old - 1

        if i not in smap:
            smap[i] = []
        smap[i].append(n)
        last = i
        n += 1
    return last


#
# Cube Matrix
#
def expand_3d_cubes(cubes):
    """Print cubes."""
    mmin, mmax = get_3d_min_max(cubes)
    for z in range(mmin[2] - 1, mmax[2] + 2):
        print(f"\nz={z}")
        for y in range(mmin[1] - 1, mmax[1] + 2):
            for x in range(mmin[0] - 1, mmax[0] + 2):
                c = (x, y, z)
                if c not in cubes:
                    cubes[c] = "."
    return cubes


def get_3d_active_neighbors(c, cubes):
    """Return the number of active neighbors for a cube."""
    neighbors = []
    x, y, z = c

    # plane above
    # row above
    neighbors.append((x - 1, y - 1, z - 1))
    neighbors.append((x, y - 1, z - 1))
    neighbors.append((x + 1, y - 1, z - 1))
    # same row
    neighbors.append((x - 1, y, z - 1))
    neighbors.append((x, y, z - 1))
    neighbors.append((x + 1, y, z - 1))
    # row below
    neighbors.append((x - 1, y + 1, z - 1))
    neighbors.append((x, y + 1, z - 1))
    neighbors.append((x + 1, y + 1, z - 1))

    # same plane
    # row above
    neighbors.append((x - 1, y - 1, z))
    neighbors.append((x, y - 1, z))
    neighbors.append((x + 1, y - 1, z))
    # same row
    neighbors.append((x - 1, y, z))
    neighbors.append((x + 1, y, z))
    # row below
    neighbors.append((x - 1, y + 1, z))
    neighbors.append((x, y + 1, z))
    neighbors.append((x + 1, y + 1, z))

    # plane below
    # row above
    neighbors.append((x - 1, y - 1, z + 1))
    neighbors.append((x, y - 1, z + 1))
    neighbors.append((x + 1, y - 1, z + 1))
    # same row
    neighbors.append((x - 1, y, z + 1))
    neighbors.append((x, y, z + 1))
    neighbors.append((x + 1, y, z + 1))
    # row below
    neighbors.append((x - 1, y + 1, z + 1))
    neighbors.append((x, y + 1, z + 1))
    neighbors.append((x + 1, y + 1, z + 1))

    active = []
    for n in neighbors:
        if n in cubes and cubes[n] == "#":
            active.append(n)
    return len(active)


def get_3d_cubes(items):
    """Return a matrix of cubes."""
    cubes = {}
    z = 0
    y = 0
    while y < len(items):
        row = list(items[y])
        x = 0
        while x < len(row):
            cubes[(x, y, z)] = row[x]
            x += 1
        y += 1
    return cubes


def get_3d_min_max(cubes):
    """Return the min and max values for x, y, and z."""
    first = sorted(cubes)[0]
    xmin, ymin, zmin = first
    xmax, ymax, zmax = first
    for cube in sorted(cubes)[1:]:
        x, y, z = cube
        xmin = min([xmin, x])
        xmax = max([xmax, x])
        ymin = min([ymin, y])
        ymax = max([ymax, y])
        zmin = min([zmin, z])
        zmax = max([zmax, z])
    return (xmin, ymin, zmin), (xmax, ymax, zmax)


def print_3d_grid(cubes):
    """Print cubes."""
    mmin, mmax = get_3d_min_max(cubes)
    for z in range(mmin[2], mmax[2] + 1):
        print(f"\nz={z}")
        for y in range(mmin[1], mmax[1] + 1):
            row = []
            for x in range(mmin[0], mmax[0] + 1):
                c = (x, y, z)
                if c in cubes:
                    row.append(cubes[c])
            print("".join(row))


def run_3d_conway_cubes(cubes):
    """Run a single cycle of the conway cube rules."""
    newcubes = {}
    cubes = expand_3d_cubes(cubes)
    for c in cubes:
        v = cubes[c]

        if v == "#":
            if get_3d_active_neighbors(c, cubes) in [2, 3]:
                newcubes[c] = "#"
            else:
                newcubes[c] = "."

        elif v == ".":
            if get_3d_active_neighbors(c, cubes) == 3:
                newcubes[c] = "#"
            else:
                newcubes[c] = "."
    return newcubes


def evaluate_expression(expression):
    """Evaluate a single expression and return the result."""
    while len(expression.split(" ")) > 3:
        print(expression)
        if "(" in expression:
            popen = expression.rfind("(")
            pclose = popen + expression[popen:].find(")")
            sub = expression[popen + 1:pclose]
            value = evaluate_expression(sub)
            expression = expression[:popen] + str(value) + expression[pclose + 1:]
        else:
            items = expression.split(" ")
            exp = " ".join(items[:3])
            rest = items[3:]
            items = [str(eval(exp))] + rest
            expression = " ".join(items)
    return eval(expression)


def evaluate_expression_advanced(expression):
    """Evaluate a single expression and return the result."""
    while len(expression.split(" ")) > 3:
        print(expression)
        if "(" in expression:
            popen = expression.rfind("(")
            pclose = popen + expression[popen:].find(")")
            sub = expression[popen + 1:pclose]
            value = evaluate_expression_advanced(sub)
            expression = expression[:popen] + str(value) + expression[pclose + 1:]
        elif "+" in expression:
            items = expression.split(" ")
            plus = items.index("+")
            value = evaluate_expression_advanced(" ".join(items[plus - 1:plus + 2]))
            expression = " ".join(items[:plus - 1] + [str(value)] + items[plus + 2:])
        else:
            return eval(expression)
    return eval(expression)
