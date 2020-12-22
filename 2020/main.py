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


def day11a():
    """Day 11a: Seating System."""
    rows = helpers.get_input_strings("day11")
    length = len(rows)
    width = len(rows[0])
    print(f"Length: {length}, Width: {width}")
    helpers.print_rows(rows)

    limit = 4
    recurse = False

    done = False
    i = 0
    while not done:
        print(f"\nIteration {i}:\n")
        new_rows = helpers.perform_seating(rows, length, width, limit, recurse)
        helpers.print_rows(new_rows)
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
    helpers.print_rows(rows)

    limit = 5
    recurse = True

    done = False
    i = 0
    while not done:
        print(f"\nIteration {i}:\n")
        new_rows = helpers.perform_seating(rows, length, width, limit, recurse)
        helpers.print_rows(new_rows)
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


def day12a():
    """Day 12a: Rain Risk."""
    items = helpers.get_input_strings("day12")
    loc = (0, 0, "E")
    for item in items:
        loc = helpers.parse_action_a(loc, item)
    x, y, d = loc
    final = abs(x) + abs(y)
    print(f"Answer: {final}")


def day12b():
    """Day 12b: Rain Risk."""
    items = helpers.get_input_strings("day12")
    loc = (10, 1, 0, 0)
    for item in items:
        loc = helpers.parse_action_b(loc, item)
    x, y, a, b = loc
    print(f"\nWaypoint: {x}, {y}; Ship: {a}, {b}")
    answer = abs(a) + abs(b)
    print(f"\nAnswer: {answer}")


def day13a():
    """Day 13a: Shuttle Search."""
    items = helpers.get_input_strings("day13")
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


def day15a():
    """Day 15a."""
    items = helpers.get_input_strings("day15")[0].split(",")
    print(items)
    print(helpers.speak_numbers(items, 2020))


def day15b():
    """Day 15b."""
    items = helpers.get_input_strings("day15")[0].split(",")
    print(items)
    print(helpers.speak_numbers(items, 30000000))


def day16a():
    """Day 16a."""
    items = helpers.get_multiline_input("day16")
    fields = items[0]
    nearby_tickets = items[2]
    fieldmap = {}
    rangemap = {}
    for f in fields:
        field, rules = f.split(":")
        r = rules.strip().split(" or ")
        print(field, r)
        fieldmap[field] = r
        for rule in r:
            start, end = rule.split("-")
            for i in range(int(start), int(end) + 1):
                if i not in rangemap:
                    rangemap[i] = []
                rangemap[i].append(field)
    count = 0
    total = 0
    for t in nearby_tickets[1:]:
        for f in t.split(","):
            if int(f) not in rangemap:
                total += int(f)
                count += 1
    print(f"Bad Tickets: {count}, Error Rate: {total}")


def day16b():
    """Day 16b."""
    items = helpers.get_multiline_input("day16")
    fields = items[0]
    my_ticket = items[1]
    nearby_tickets = items[2]

    fieldmap = {}
    rangemap = {}
    for f in fields:
        field, rules = f.split(":")
        r = rules.strip().split(" or ")
        print(field, r)
        fieldmap[field] = r
        for rule in r:
            start, end = rule.split("-")
            for i in range(int(start), int(end) + 1):
                if i not in rangemap:
                    rangemap[i] = []
                rangemap[i].append(field)

    count = 0
    total = 0
    valid_tickets = []
    for t in nearby_tickets[1:]:
        valid = True
        for f in t.split(","):
            if int(f) not in rangemap:
                total += int(f)
                count += 1
                valid = False
        if valid:
            valid_tickets.append(t)

    print(f"{len(valid_tickets)} valid tickets.")
    schema = {}

    for t in valid_tickets:
        values = [int(v) for v in t.split(",")]
        n = 0
        while n < len(values):
            v = values[n]
            s = set(rangemap[v])
            if n not in schema:
                schema[n] = list(s)
            else:
                schema[n] = list(set(schema[n]).intersection(s))
            print(v, schema[n])
            n += 1

    final = []

    while len(final) != len(schema):
        for n in schema:
            fields = schema[n]
            if len(fields) == 1:
                field = fields[0]
                if field not in final:
                    print(f"Found: {field} [{n}]")
                    final.append(field)
            else:
                for field in list(fields):
                    if field in final:
                        print(f"Removed {field} [{n}")
                        fields.remove(field)

    print("Schema:")
    print(json.dumps(schema, indent=2, sort_keys=True))

    me = [int(x) for x in my_ticket[1].split(",")]
    print(me)
    departure = 1
    for n in schema:
        f = schema[n][0]
        if f.startswith("departure"):
            departure *= me[n]

    print(departure)


def day17a():
    """Day 17a."""
    items = helpers.get_input_strings("day17")
    cubes = helpers.get_3d_cubes(items)
    helpers.print_3d_grid(cubes)

    n = 0
    while n < 6:
        cubes = helpers.run_3d_conway_cubes(cubes)
        # print_grid(cubes)
        n += 1

    count = 0
    for i in cubes:
        if cubes[i] == "#":
            count += 1

    print(f"Count: {count}")


def day17b():
    """Day 17b."""
    items = helpers.get_input_strings("day17test")


def day18a():
    """Day 18a."""
    items = helpers.get_input_strings("day18")
    total = 0
    for expression in items:
        total += helpers.evaluate_expression(expression)
    print(f"Total: {total}")


def day18b():
    """Day 18a."""
    items = helpers.get_input_strings("day18")
    total = 0
    for expression in items:
        total += helpers.evaluate_expression_advanced(expression)
    print(f"Total: {total}")


def day19a():
    """Day 19a: Monster Messages."""
    items = helpers.get_multiline_input("day19test")
    rules = {}
    for r in items[0]:
        i = int(r.split(":")[0])
        rules[i] = r.split(":")[1].strip().replace('"', '')
    print(json.dumps(rules, indent=2, sort_keys=True))
    messages = items[1]

    string = helpers.build_rule_regexp(rules)
    regexp = f"^{string}$"

    matches = 0
    for m in messages:
        if re.match(regexp, m):
            print(f"{m} matches!")
            matches += 1
        else:
            print(f"{m} does not match.")
    print(f"Matches: {matches}")


def day19b():
    """Day 19b."""
    items = helpers.get_multiline_input("day19")
    rules = {}
    for r in items[0]:
        i = int(r.split(":")[0])
        rules[i] = r.split(":")[1].strip().replace('"', '')
    rules[8] = "42 | 42 8"
    rules[11] = "42 31 | 42 11 31"
    print(json.dumps(rules, indent=2, sort_keys=True))
    messages = items[1]

    r31 = helpers.build_rule_regexp(rules, 31)
    r42 = helpers.build_rule_regexp(rules, 42)

    # string = f"{r42}+{r31}+"
    # print(string)
    regexp = f"^{r42}+{r31}+$"

    matches = 0
    for m in messages:
        if re.match(regexp, m):
            print(f"{m} matches!")
            matches += 1
        else:
            print(f"{m} does not match.")
    print(f"Matches: {matches}")


def get_edges(tile):
    """Get tile edges."""
    edges = []
    edges.append(tile[0])
    edges.append(tile[-1])
    left = []
    right = []
    for line in tile:
        left.append(line[0])
        right.append(line[-1])
    edges.append("".join(left))
    edges.append("".join(right))
    print("")
    return edges


def day20a():
    """Day 20a: Jurassic Jigsaw."""
    items = helpers.get_multiline_input("day20")

    edges = {}
    tiles = {}
    for i in items:
        t = helpers.Tile(i)
        tiles[t.id] = t
        for e in t.edges:
            if e not in edges:
                edges[e] = [t.id]
            else:
                edges[e].append(t.id)

    for e in edges:
        if len(edges[e]) == 2:
            j, k = edges[e]
            if k not in tiles[j].neighbors:
                tiles[j].neighbors.append(k)
            if j not in tiles[k].neighbors:
                tiles[k].neighbors.append(j)

    corners = []
    for tid in tiles:
        t = tiles[tid]
        if len(t.neighbors) == 2:
            if tid not in corners:
                corners.append(tid)

    print(f"\n{' * '.join([str(i) for i in corners])} = {math.prod(corners)}")


def day20b():
    """Day 20b: Jurassic Jigsaw."""
    items = helpers.get_multiline_input("day20")
    size = int(math.sqrt(len(items)))
    print(f"Grid Size: {size}x{size}")

    edges = {}
    tiles = {}
    for i in items:
        t = helpers.Tile(i)
        tiles[t.id] = t
        for e in t.edges:
            if e not in edges:
                edges[e] = [t.id]
            else:
                edges[e].append(t.id)

    for e in edges:
        if len(edges[e]) == 2:
            j, k = edges[e]
            if k not in tiles[j].neighbors:
                tiles[j].neighbors.append(k)
            if j not in tiles[k].neighbors:
                tiles[k].neighbors.append(j)

    corners = []
    for tid in tiles:
        t = tiles[tid]
        if len(t.neighbors) == 2:
            if tid not in corners:
                corners.append(tid)

    # print(f"\n{' * '.join([str(i) for i in corners])} = {math.prod(corners)}")

    # choose a tile to be the top-left tile in the grid
    topleft = corners[0]
    tiles[topleft].location = (0, 0)

    # locate the neighbors to the right and bottom
    right = tiles[topleft].neighbors[0]
    tiles[right].location = (0, 1)
    bottom = tiles[topleft].neighbors[1]
    tiles[bottom].location = (1, 0)

    print(f"\nTop-Left: {topleft}")
    print(f"Right: {right}")
    print(f"Bottom: {bottom}\n")

    # orient the top-left tile
    tiles[topleft].orient_topleft(tiles[right], tiles[bottom])

    grid = {}
    for y in range(0, size):
        for x in range(0, size):
            v = (y, x)
            if v == (0, 0):
                grid[v] = tiles[topleft]
            else:
                if v[1] > 0:
                    l1 = grid[(v[0], v[1] - 1)]
                    left = l1.right
                    e = edges[left]
                    print(v)
                    print(e)
                    e.remove(l1.id)
                    tid = e[0]
                    t = tiles[tid]
                    grid[v] = t
                    t.orient_left(left)
                else:
                    t1 = grid[(v[0] - 1, v[1])]
                    top = t1.bottom
                    e = edges[top]
                    e.remove(t1.id)
                    print(top)
                    tid = e[0]
                    t = tiles[tid]
                    grid[v] = t
                    t.orient_top(top)
            print(v)
            grid[v].display_tile()
            print()

    # remove edges
    for v in grid:
        grid[v].remove_edges()

    # assemble new tile out of full grid
    newrows = ["Tile 0:"]
    for y in range(0, size):
        for i in range(0, 8):
            row = ""
            for x in range(0, size):
                v = (y, x)
                t = grid[v]
                row += t.rows[i]
            newrows.append(row)
    g = helpers.Tile(newrows)

    count = g.find_sea_monsters()
    while not count:
        g.rotate_right()
        count = g.find_sea_monsters()
        if not count:
            g.flip_horizontally()
            count = g.find_sea_monsters()
            if not count:
                g.flip_horizontally()
            else:
                break

    print()
    g.display_tile()

    print(f"\nCount: {count} sea monsters")

    rapids = 0
    for row in g.rows:
        rapids += row.count("#")
    print(f"Roughness: {rapids}")


def day21a():
    """Day 21a."""
    items = helpers.get_input_strings("day21")

    allergens = {}
    ingredients = {}

    for i in items:
        f, a = i.strip(")").split(" (contains ")
        foods = []
        algns = []
        for food in f.strip().split(" "):
            foods.append(food)
        for algn in a.split(","):
            algns.append(algn.strip())
        print(foods)
        print(algns)
        print("")
        for allergen in algns:
            if allergen not in allergens:
                allergens[allergen] = foods
            else:
                allergens[allergen] = list(set(allergens[allergen]).intersection(set(foods)))
        for food in foods:
            if food not in ingredients:
                ingredients[food] = 0
            ingredients[food] += 1

    print(json.dumps(allergens, indent=2, sort_keys=True))

    found = {}
    while len(found) < len(allergens):

        for allergen in allergens:
            i = allergens[allergen]
            if len(i) == 1:
                f = i[0]
                found[f] = allergen
                for a in allergens:
                    if f in allergens[a]:
                        allergens[a].remove(f)

    print(json.dumps(found, indent=2, sort_keys=True))

    total = 0
    for food in ingredients:
        if food not in found:
            total += ingredients[food]

    print(f"Total: {total}")

    print(",".join(sorted(found, key=lambda x: found[x])))


def day22a():
    """Day 22a: Crab Combat."""
    items = helpers.get_multiline_input("day22")
    player1 = items[0][1:]
    player2 = items[1][1:]

    round = 0
    while len(player1) and len(player2):
        round += 1
        print(f"\n-- Round {round} --")
        print(f"Player 1's deck: {', '.join(player1)}")
        print(f"Player 2's deck: {', '.join(player2)}")
        p1p = player1.pop(0)
        p2p = player2.pop(0)
        print(f"Player 1 plays: {p1p}")
        print(f"Player 2 plays: {p2p}")
        if int(p1p) > int(p2p):
            print("Player 1 wins the round!")
            player1.append(p1p)
            player1.append(p2p)
        else:
            print("Player 2 wins the round!")
            player2.append(p2p)
            player2.append(p1p)

    print("\n== Post-game results ==")
    print(f"Player 1's deck: {', '.join(player1)}")
    print(f"Player 2's deck: {', '.join(player2)}")

    if player1:
        player = player1
    else:
        player = player2

    score = 0
    n = 1
    while player:
        bottom = player.pop()
        value = int(bottom) * n
        score += value
        n += 1

    print(f"Score: {score}")


def day22b():
    """Day 22b: Crab Combat."""
    items = helpers.get_multiline_input("day22")
    player1 = items[0][1:]
    player2 = items[1][1:]

    global game
    game = 0

    verbose = False

    def play_recursive_combat(player1, player2):
        """Play a game of recursive combat."""
        global game
        game += 1
        this = int(game)

        print(f"\n=== Game {this} ===")
        player1_hashes = []
        player2_hashes = []

        round = 0
        while len(player1) and len(player2):
            round += 1
            if verbose:
                print(f"\n-- Round {round} (Game {this}) --")
                print(f"Player 1's deck: {', '.join(player1)}")
                print(f"Player 2's deck: {', '.join(player2)}")

            player1_hash = ','.join(player1)

            if player1_hash in player1_hashes:
                if verbose:
                    print(f"Player 1 wins round {round} of game {this}!!")
                    print(f"The winner of game {this} is player 1!")
                return 1
            else:
                player1_hashes.append(player1_hash)

            player2_hash = ','.join(player2)
            if player2_hash in player2_hashes:
                if verbose:
                    print(f"Player 1 wins round {round} of game {this}!!")
                    print(f"The winner of game {this} is player 1!")
                return 1
            else:
                player2_hashes.append(player2_hash)

            # play a round
            p1p = player1.pop(0)
            p2p = player2.pop(0)

            if verbose:
                print(f"Player 1 plays: {p1p}")
                print(f"Player 2 plays: {p2p}")

            winner = 0
            if len(player1) >= int(p1p) and len(player2) >= int(p2p):
                print("Playing a sub-game to determine the winner...")
                winner = play_recursive_combat(player1[:int(p1p)], player2[:int(p2p)])
                print(f"\n... anyway back to game {this}.")
            elif int(p1p) > int(p2p):
                winner = 1
            elif int(p2p) > int(p1p):
                winner = 2

            if winner == 1:
                if verbose:
                    print(f"Player 1 wins round {round} of game {this}!")
                player1.append(p1p)
                player1.append(p2p)
            elif winner == 2:
                if verbose:
                    print(f"Player 2 wins round {round} of game {this}!")
                player2.append(p2p)
                player2.append(p1p)

        if player1:
            print(f"The winner of game {this} is player 1!")
            return 1
        else:
            print(f"The winner of game {this} is player 2!")
            return 2

    winner = play_recursive_combat(player1, player2)
    print("\n== Post-game results ==")
    print(f"Player 1's deck: {', '.join(player1)}")
    print(f"Player 2's deck: {', '.join(player2)}")
    if winner == 1:
        print("\nPlayer 1 Wins!!!")
    elif winner == 2:
        print("\nPlayer 2 Wins!!!")
    else:
        print("WTF!")

    if player1:
        player = player1
    else:
        player = player2

    score = 0
    n = 1
    while player:
        bottom = player.pop()
        value = int(bottom) * n
        score += value
        n += 1

    print(f"Score: {score}")


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
