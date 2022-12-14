from tqdm import tqdm


def get_neighbors(node):
    valid_neighbors = []
    x, y = node
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        neighbour = x+dx, y+dy
        if neighbour in grid and grid[neighbour] - grid[node] <= 1:
            valid_neighbors.append(neighbour)
    return valid_neighbors


def bfs_shortest_path(start, end):
    queue = [[start]]
    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            neighbors = get_neighbors(node)

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == end:
                    return len(new_path) -1

        visited.append(node)
    return float('inf')


with open('inputs/12.txt') as f:
    d = [list(a.strip()) for a in f.readlines()]

    grid = {}
    start = (0,0)
    end = (0,0)
    for i, l in enumerate(d):
        for j, letter in enumerate(l):
            if letter == "S":
                start = i,j
                letter = "a"
            if letter == "E":
                end = i,j
                letter = "z"
            grid[(i,j)] = ord(letter) - ord('a')

print(f"Part 1: {bfs_shortest_path(start, end)}")

# probably shouldn't brute force this, but alas
paths = []
for k,v in tqdm(grid.items()):
    if v == 0:
        paths.append(bfs_shortest_path(k, end))

print(f"Part 2: {min(paths)}")

