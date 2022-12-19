import re
from scipy.spatial.distance import cityblock
from tqdm import tqdm
from collections import Counter


def part_1(questioned_y):
    not_beacons = set()
    for pair in list(zip(sensors, beacons)):
        sensor, beacon = pair
        x, y = sensor
        dist = cityblock(*pair)
        if abs(y - questioned_y) < dist:
            remainder_for_x = dist - abs(y - questioned_y)
            not_beacons.update(range(x - remainder_for_x, x + remainder_for_x + 1))
    return len(not_beacons) - 1


def part_2(questioned_y):
    for pair in list(zip(sensors, beacons)):
        sensor, beacon = pair
        x, y = sensor
        dist = cityblock(*pair)
        if abs(y - questioned_y) < dist:
            remainder_for_x = dist - abs(y - questioned_y)
            low = x - remainder_for_x - 1
            high = x + remainder_for_x + 1
            if low >= 0:
                yield low, questioned_y
            if high <= 4000000:
                yield high, questioned_y


with open('inputs/15.txt') as f:
    cords = re.findall("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", f.read())
    sensors = [tuple(map(int, cord[:2])) for cord in cords]
    beacons = [tuple(map(int, cord[2:])) for cord in cords]

    print(f"part 1 : {part_1(2000000)}")

    # Probably shouldn't loop over all the rows, but it runs in less then 10 minutes
    for y in tqdm(range(0, 4000000 + 1)):
        options = part_2(y)
        c = Counter(list(options))
        if 4 in c.values():
            a = {v: k for k, v in c.items()}
            x, y = a[4]
            print(f"Part 2: {x * 4000000 + y}")
            break
