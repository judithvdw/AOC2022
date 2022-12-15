from math import sqrt


def get_wall(cord1, cord2):
    wall = []
    xs, ys = list(zip(cord1, cord2))
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            wall.append((x, y))
    return wall


def create_walls(cords):
    walls = []
    for i in range(len(cords) - 1):
        walls.extend(get_wall(cords[i], cords[i + 1]))
    return set(walls)


def drop_sand_grain(walls, void, origin=(500, 0)):
    current_position = origin
    while current_position[1] < void:
        next_options = (current_position[0], current_position[1] + 1), (
        current_position[0] - 1, current_position[1] + 1), (current_position[0] + 1, current_position[1] + 1)
        if all([pos in walls for pos in next_options]):
            return current_position
        else:
            for option in next_options:
                if option not in walls:
                    current_position = option
                    break
    return None


def get_void(wall):
    return max([cord[1] for cord in wall])


def create_floor(floor):
    length = int(2 * floor / sqrt(3))
    floor_tiles = []
    for i in range(-length + 500, length + 500):
        floor_tiles.append((i, floor))
    return floor_tiles


with open('inputs/14.txt') as f:
    directions = list(set(f.readlines()))  # there seem to be a lot of duplicates
    directions = [[tuple(map(int, cord.split(","))) for cord in direction.strip().split(" -> ")] for direction in
                  directions]

    walls = set()
    for direction in directions:
        walls.update(create_walls(direction))

    void_y = get_void(walls)
    i = 0
    while True:
        next_location = drop_sand_grain(walls, void_y)
        if next_location:
            walls.update([next_location])
            i += 1
        else:
            break

    print(f"Part 1: {i}")

    walls = set()
    for direction in directions:
        walls.update(create_walls(direction))

    floor = get_void(walls) + 2
    i = 0
    floors = create_floor(floor)
    walls.update(set(floors))
    while True:
        next_location = drop_sand_grain(walls, void_y + 3)
        i += 1
        if next_location == (500, 0):
            break
        else:
            walls.update([next_location])

    print(f"Part 2: {i}")
