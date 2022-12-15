from itertools import chain


def compare(left, right):
    left = left if isinstance(left, list) else [left]
    right = right if isinstance(right, list) else [right]
    for l, r in zip(left, right):
        if isinstance(l, list) or isinstance(r, list):
            dif = compare(l,r)
        else:
            dif = r - l
        if dif != 0:
            return dif
    return len(right) - len(left)


with open('inputs/13.txt') as f:
    packets_str = [a.split('\n') for a in f.read().split("\n\n")]
    packet_pairs = [list(map(eval, packet)) for packet in packets_str]

    results = [compare(*pair) for pair in packet_pairs]
    print(f"Part 1: {sum([i+1 for i, result in enumerate(results) if result > 0])}")

    packets = list(chain(*packet_pairs))
    two = 1 # one indexed
    six = 2 # one indexed + offset for two
    for packet in packets:
        if compare(packet, [[2]]) > 0:
            two += 1
            six += 1
        elif compare(packet, [[6]]) > 0:
            six += 1

    print(f"Part 2: {two * six}")




