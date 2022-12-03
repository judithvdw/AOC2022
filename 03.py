def priority(letter):
    if letter.isupper():
        return ord(letter) - ord("A") + 1 + 26
    else:
        return ord(letter) - ord("a") + 1


with open('inputs/3.txt') as f:
    backpacks = [i.strip() for i in f.readlines()]

total = 0
for backpack in backpacks:
    length = len(backpack)
    compartment1 = set(list(backpack[:length//2]))
    compartment2 = set(list(backpack[length//2:]))
    in_both = compartment1 & compartment2
    shared = in_both.pop()
    total += priority(shared)

print(f"Part 1: {total}")

total = 0
for i in range(0,len(backpacks),3):
    group = [set(list(b)) for b in backpacks[i:i+3]]
    badge = group[0] & group[1] & group[2]
    badge = badge.pop()
    total += priority(badge)

print(f"Part 2: {total}")


