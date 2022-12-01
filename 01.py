with open('inputs/1.txt') as f:
    calories = [[int(j) for j in i.split("\n")] for i in f.read().split("\n\n")]

    totals = [sum(i) for i in calories]
    part1 = max(totals)
    print(f"Part 1: {part1}")

    part2 = sum(sorted(totals)[::-1][:3])
    print(f"Part 2: {part2}")