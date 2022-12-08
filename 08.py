with open("inputs/8.txt") as f:
    forest = [list(map(int, list(i.strip()))) for i in f.readlines()]
    transposed_forest = list(map(list, zip(*forest)))


visible = 0
for i, row in enumerate(forest):
    for j in range(len(row)):
        if all(row[j] > b for b in row[j + 1:]) or \
                all(row[j] > b for b in row[:j]) or \
                all(transposed_forest[j][i] > b for b in transposed_forest[j][i + 1:]) or \
                all(transposed_forest[j][i] > b for b in transposed_forest[j][:i]):
            visible += 1

print(f"Part 1: {visible}")

scenic_scores = []
for i, row in enumerate(forest):
    for j, tree in enumerate(row):
        up = next((i + 1 for i, val in enumerate(transposed_forest[j][:i][::-1]) if val >= tree), len(transposed_forest[j][:i]))
        down = next((i + 1 for i, val in enumerate(transposed_forest[j][i + 1:]) if val >= tree), len(transposed_forest[j][i + 1:]))
        left = next((i + 1 for i, val in enumerate(row[:j][::-1]) if val >= tree), len(row[:j]))
        right = next((i + 1 for i, val in enumerate(row[j + 1:]) if val >= tree), len(row[j + 1:]))
        scenic_scores.append(up * down * left * right)

print(f"Part 2: {max(scenic_scores)}")
