import numpy as np

with open('input.txt') as f:
    lines = f.read().split('\n')
    grid = np.zeros((len(lines), len(lines[0])), dtype=np.int32)
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if lines[x][y] == '#':
                grid[x][y] = 1

def num_neighbors_on(grid, x, y):
    num = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if x+dx == x and y+dy == y:
                continue
            if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and grid[x+dx, y+dy] == 1:
                num += 1
    return num

def part1(grid, steps, corner_on = False):
    if corner_on:
        grid[0][0] = 1
        grid[0][-1] = 1
        grid[-1][0] = 1
        grid[-1][-1] = 1
    for _ in range(steps):
        new_grid = np.zeros_like(grid)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                num_neigh_on = num_neighbors_on(grid, x, y)
                if grid[x, y] == 1 and num_neigh_on in [2, 3]:
                    new_grid[x, y] = 1
                if grid[x, y] == 0 and num_neigh_on == 3:
                    new_grid[x, y] = 1
        grid = new_grid
        if corner_on:
            grid[0][0] = 1
            grid[0][-1] = 1
            grid[-1][0] = 1
            grid[-1][-1] = 1
    return np.sum(grid)

print('part1:', part1(grid, 100))
print('part2:', part1(grid, 100, True))

