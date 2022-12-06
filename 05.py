from collections import defaultdict


def parse_start_state(start):
    d = defaultdict(list)
    for row in start.split("\n")[::-1]:
        row = row[1::4]  # Every 4th character is the crate (or the space above the crates)
        for i, value in enumerate(row):
            if value != " ":
                d[i + 1].append(value)  # +1 so the key matches the instructions
    return d


def do_instruction(instruction, crates, part1=True):
    amount, origin, destination = instruction
    move = crates[origin][-amount:]
    del crates[origin][-amount:]
    crates[destination].extend(move[::-1] if part1 else move)


def run(part1=True):
    crates = parse_start_state(start_raw)
    instructions = [tuple(map(int, line.strip().split()[1::2])) for line in instuctions_raw.split("\n")]

    for instruction in instructions:
        do_instruction(instruction, crates, part1=part1)

    letters = ""
    for i in range(1, len(crates) + 1):
        letters += crates[i][-1]
    return letters


with open("inputs/5.txt") as f:
    start_raw, instuctions_raw = f.read().split("\n\n")

print(f"Part 1: {run(part1=True)}")
print(f"Part 2: {run(part1=False)}")
