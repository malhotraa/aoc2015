with open('input.txt') as f:
    lines = f.read().split('\n')

def part1(lines):
    total = 0
    for line in lines:
        dims = list(map(int, line.split('x')))
        assert len(dims) == 3
        min_area = dims[0] * dims[1]
        for i in range(3):
            area = dims[i] * dims[(i+1)%3]
            total += 2 * area
            min_area = min(min_area, area)
        total += min_area
    return total

def part2(lines):
    total = 0
    for line in lines:
        dims = list(map(int, line.split('x')))
        assert len(dims) == 3
        shortest_perim = min(2*(dims[0]+dims[1]), 2*(dims[1] + dims[2]), 2*(dims[0] + dims[2]))
        total += (shortest_perim + dims[0] * dims[1] * dims[2])
    return total

print('part1:', part1(lines))
print('part2:', part2(lines))