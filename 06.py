def find_offset(buffer, l):
    for i in range(len(buffer)):
        b = buffer[i:i + l]
        if len(set(b)) == l:
            return b, i + l


with open('inputs/6.txt') as f:
    buffer = f.read()

print(f"Part 1 {find_offset(buffer, 4)}")
print(f"Part 1 {find_offset(buffer, 14)}")
