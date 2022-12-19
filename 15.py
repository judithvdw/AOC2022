import re
from math import dist
from scipy.spatial.distance import cityblock
from tqdm import tqdm

def manhattan(pair):
    return cityblock(*pair)


def get_offsets_at_same_distance(cord, dist):
    cords = set()
    v,w = cord
    for x,y in zip(range(dist+1), range(dist+1)[::-1]):
            cords.update([(v+x,w+y)], [(v+-x,w+-y)], [(v+-x, w+y)], [(v+x,w+-y)])
    return(cords)


with open('inputs/15.txt') as f:
    cords = re.findall("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", f.read())
    sensors = [tuple(map(int, cord[:2])) for cord in cords]
    beacons = [tuple(map(int, cord[2:])) for cord in cords]

    not_beacons = set()
    Y = 2_000_000
    for pair in tqdm(list(zip(sensors, beacons))):
        sensor, beacon = pair
        dist = manhattan(pair)
        edges = get_offsets_at_same_distance(sensor, dist)
        edges = list(set(filter(lambda x:x[1]==Y, edges)))
        if not edges:
            continue
        elif len(edges) == 1:
            not_beacons.update([edges[0][0]])
        else:
            assert len(edges) == 2
            small = min(edges[0][0],edges[1][0])
            big = max(edges[0][0],edges[1][0])
            not_beacons.update(range(small, big + 1))

    print(len(not_beacons) -1)





