from itertools import cycle


with open("inputs/10.txt") as f:
    instructions = [i.strip() for i in f.readlines()]

x = 1
i = 1
total = 0
checks = (20, 60, 100, 140, 180, 220)
overview = {i: x}
for idx, instruction in enumerate(cycle(instructions)):
    if instruction.startswith("addx"):
        i += 1
        overview[i] = x
        if i in checks:
            total += (i * x)
        x += int(instruction[5:])
        i += 1
        overview[i] = x
        if i in checks:
            total += (i * x)
    else:
        i += 1
        overview[i] = x
        if i in checks:
            total += (i * x)
    if i >= 241:
        break

print(f"Part 1:{total}",)
print("Part 2:")
line = ""
for i in range(1, len(overview)):
    if overview[i] in (i % 40 - 2, i % 40 - 1, i % 40):
        line += "█"
    else:
        line += " "
    if i % 40 == 0:
        print(line)
        line = ""

