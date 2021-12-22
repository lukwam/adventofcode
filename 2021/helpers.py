"""Helpers for doing Advent of Code puzzles."""

DATADIR="data"


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def get_input_as_string(day):
    """Return the data for day as a string."""
    f = open(f"{DATADIR}/{day}.txt")
    return f.read()


def get_input_as_list(day):
    f = open(f"{DATADIR}/{day}.txt")
    return f.read().split("\n")

