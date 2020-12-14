"""Advent of Code 2019."""
import math
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

    def __init__(self, intcode):
        """Initialize a computer."""
        self.memory = []
        for i in intcode.split(","):
            self.memory.append(int(i))
        print(f"Memory: {self.memory}")

    def add(self, a, b, c):
        """Add two numbers a and b and store value in c."""
        x = self.memory[a]
        y = self.memory[b]
        self.memory[c] = x + y
        print(f"{x} + {y} = {x + y} => {c}")

    def multiply(self, a, b, c):
        """Multiply two numbers a and b and store value in c."""
        x = self.memory[a]
        y = self.memory[b]
        self.memory[c] = x * y
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
                a = self.memory[i + 1]
                b = self.memory[i + 2]
                c = self.memory[i + 3]
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
    items = get_str_input("day2")
    noun = 12
    verb = 2
    computer = Computer(items[0])
    computer.run(noun, verb)
    print(f"Position 0: {computer.memory[0]}")


def day2b():
    """Day 2b."""
    output = 19690720

    items = get_str_input("day2test")

    memory = []
    for i in items[0].split(","):
        memory.append(int(i))

    print(memory)

    # for i in items:
        # print(i)
    #     integers = []
    #     for num in i.split(","):
    #         integers.append(int(num))

    #     for j in range(0, 99, 1):
    #         print(f"J = {j}")
    #         for k in range(0, 99, 1):
    #             print(f"K = {k}")
    #             integers[1] = j
    #             integers[2] = k
    #             n = 0
    #             done = False
    #             while not done:
    #                 opcode = integers[n]
    #                 if opcode == 1:
    #                     k1 = integers[n + 1]
    #                     k2 = integers[n + 2]
    #                     k3 = integers[n + 3]
    #                     # print(f"Add opcode {k1} + {k2} and store in {k3}")
    #                     value1 = integers[k1]
    #                     value2 = integers[k2]
    #                     # value3 = integers[k3]
    #                     integers[k3] = value1 + value2
    #                     # print(integers)
    #                     n += 4

    #                 elif opcode == 2:
    #                     k1 = integers[n + 1]
    #                     k2 = integers[n + 2]
    #                     k3 = integers[n + 3]
    #                     # print(f"Add opcode {k1} + {k2} and store in {k3}")
    #                     value1 = integers[k1]
    #                     value2 = integers[k2]
    #                     # value3 = integers[k3]
    #                     integers[k3] = value1 * value2
    #                     # print(integers)
    #                     n += 4

    #                 elif opcode == 99:
    #                     print(integers[0])
    #                     if integers[0] == 19690720:
    #                         print(f"Noun: {j}, Verb: {k}")
    #                         return
    #                     done = True
    #                     # print("EXITING.")
    #                 #     break
    #                 # else:
    #                 #     print("ERROR")
    #                 #     done = True
    #                 #     return


def main():
    """Main function."""
    if len(sys.argv) > 1:
        function = sys.argv[1]
        globals()[function]()
    else:
        print("Hello World!")


if __name__ == "__main__":
    main()
