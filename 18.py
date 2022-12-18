def get_visible_sides(cubes):
    covered_sides = 0
    for cube in cubes:
        x, y, z = cube
        options = {(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)}
        covered_sides += len(options & cubes)

    return 6 * len(cubes) - covered_sides


with open("inputs/18.txt") as f:
    lava = set([tuple(map(int, a.split(","))) for a in f.readlines()])


total_grid = set([(x,y,z) for x in range(0,22) for y in range(0,22) for z in range(0,22)])

all_air = total_grid - lava
start = (0,0,0)
outside_air = {start}
queue = [start]

while queue:
    point = queue.pop(0)
    x,y,z = point
    if point not in all_air:
        continue
    new_outside_air = {(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)} - outside_air - lava
    outside_air.update(new_outside_air)
    queue.extend(new_outside_air)

inside = all_air - outside_air

print(f"Part 1: {get_visible_sides(lava)}")
print(f"Part 2: {get_visible_sides(inside | lava)}")


