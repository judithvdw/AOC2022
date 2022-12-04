import re


def contains(assignment):
    return assignment[0] <= assignment[2] and assignment[1] >= assignment[3] or \
           assignment[0] >= assignment[2] and assignment[1] <= assignment[3]


def overlap(assignment):
    return not (assignment[0] < assignment[2] and assignment[1] < assignment[2] or
                assignment[0] > assignment[3] and assignment[1] > assignment[3])


with open("inputs/4.txt") as f:
    assignments = [list(map(int, re.findall('\d+', i))) for i in f.readlines()]

    print(f"Part 1: {sum(map(contains, assignments))}")
    print(f"Part 2: {sum(map(overlap, assignments))}")
