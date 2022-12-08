
def build_file_system(commands):
    command_chunks = [command.strip() for command in commands.split("$")[2:]]
    system = {}
    path = []
    current = system
    for chunk in command_chunks:
        chunk = chunk.split("\n")

        if chunk[0][:2] == "ls":
            for b in chunk[1:]:
                b = b.split() # dir of file
                if b[0] == 'dir':
                    current[b[1]] = {}
                else:
                    current[b[1]] = int(b[0])
            continue

        chunk = chunk[0].split()
        if chunk[0] == "cd":
            if chunk[1] == "..":
                del path[-1]
                current = system
                for pad in path:
                    current = current[pad]
            else:
                path.append(chunk[1])
                current = current[path[-1]]
    return system


def total_size(d):
    size = 0
    for k in d:
        if not type(d[k]) == dict:
            size += d[k]
        else:
            size += total_size(d[k])
    return size


def walk(d):
    sizes = []
    for k in d:
        if type(d[k]) == dict:
            sizes.append([k, total_size(d[k])])
            sizes.extend(walk(d[k]))
    return sizes


with open('inputs/7.txt') as f:
    commands = f.read()
    system = build_file_system(commands)
    system = {"root": system}
    sizes = walk(system)

    total = 0
    for _, size in sizes:
        if size <= 100000:
            total += size
    print(f"part 1: {total}")

    total_disk_space = 70_000_000
    necessary_unused = 30_000_000
    current_size = sizes[0][1]
    needed = abs(total_disk_space - necessary_unused - current_size)
    just_sizes = sorted([i[1] for i in sizes])
    for i in just_sizes:
        if i > needed:
            print(f"Part 2: {i}")
            break
