with open('input.txt') as f:
    line = f.read()

MOVE_TO_OFFSET = {
    '^': (-1, 0),
    'v': (1, 0),
    '>': (0, 1),
    '<': (0, -1),
}

def part1(line):
    curr = (0, 0)
    visited = set([curr])
    for move in line:
        offset = MOVE_TO_OFFSET[move]
        curr = (curr[0] + offset[0], curr[1] + offset[1])
        visited.add(curr)
    return len(visited)

def part2(line):
    santa = (0, 0)
    robo = (0, 0)
    visited = set([santa])
    idx = 0
    while idx < len(line):
        s_off = MOVE_TO_OFFSET[line[idx]]
        r_off = MOVE_TO_OFFSET[line[idx+1]]
        santa = (santa[0] + s_off[0], santa[1] + s_off[1])
        robo = (robo[0] + r_off[0], robo[1] + r_off[1])
        visited.update([santa, robo])
        idx += 2
    return len(visited)

print('part1:', part1(line))
print('part2:', part2(line))