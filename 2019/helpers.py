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
    print(f"Found {len(entries)} entry in puzzle input.")
    return entries
