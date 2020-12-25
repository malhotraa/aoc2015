import re
import numpy as np

with open('input.txt') as f:
    lines = f.read().split('\n')

def part1(lines):
    grid = np.zeros((1000, 1000), dtype=np.bool)
    for line in lines:
        m = re.match(r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)", line)
        ins, x1, y1, x2, y2 = m.groups()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if ins == 'turn on':
            grid[x1:x2+1,y1:y2+1] = True
        if ins == 'turn off':
            grid[x1:x2+1,y1:y2+1] = False
        if ins == 'toggle':
            grid[x1:x2+1,y1:y2+1] = ~grid[x1:x2+1,y1:y2+1]
    return grid.sum()

def part2(lines):
    grid = np.zeros((1000, 1000), dtype=np.int32)
    for line in lines:
        m = re.match(r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)", line)
        ins, x1, y1, x2, y2 = m.groups()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if ins == 'turn on':
            grid[x1:x2+1,y1:y2+1] += 1
        if ins == 'turn off':
            grid[x1:x2+1,y1:y2+1] -= 1
            grid[grid < 0] = 0
        if ins == 'toggle':
            grid[x1:x2+1,y1:y2+1] += 2
    return grid.sum()

print('part1:', part1(lines))
print('part2:', part2(lines))