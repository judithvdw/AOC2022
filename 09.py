from math import dist, sqrt


def move_head(cord, step):
    direction, distance = step
    if direction == "U":
        return [(cord[0], cord[1] + i) for i in range(1, distance + 1)]
    if direction == 'D':
        return [(cord[0], cord[1] - i) for i in range(1, distance + 1)]
    if direction == 'R':
        return [(cord[0] + i, cord[1]) for i in range(1, distance + 1)]
    if direction == "L":
        return [(cord[0] - i, cord[1]) for i in range(1, distance + 1)]


def next_tail_pos(t, h):
    step_options = [(1, 1), (-1, -1), (1, -1), (-1, 1), (-1, 0), (1,0), (0, -1), (0, 1)]
    max_dist = sqrt(2)
    if dist(t, h) > max_dist:
        options = {(t[0] + s[0], t[1] + s[1]): dist((t[0] + s[0], t[1] + s[1]), h) for s in step_options}
        return min(options, key=options.get)
    else:
        return t


def run_tail(path_head, knots):
    path_tail = [(0, 0)]
    for _ in range(knots - 1):
        for i in range(len(path_head) - 1):
            prev_tail = path_tail[i]
            next_head = path_head[i + 1]
            path_tail.append(next_tail_pos(prev_tail, next_head))
        path_head = path_tail
        path_tail = [(0, 0)]

    return len(set(path_head))


with open("inputs/9.txt") as f:
    steps = [x.strip().split() for x in f.readlines()]
    steps = [[x[0], int(x[1])] for x in steps]

path_head = [(0,0)]
for step in steps:
    path_head.extend(move_head(path_head[-1], step))

print(f"Part 1: {run_tail(path_head, 2)}")
print(f"Part 2: {run_tail(path_head, 10)}")
