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

print(visible)
