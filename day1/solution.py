with open('input.txt') as f:
    line = f.read()

def part1(line):
    return line.count('(') - line.count(')')
def part2(line):
    floor = 0
    for idx, ch in enumerate(line):
        if ch == '(':
            floor += 1
        else:
            floor -= 1
        
        if floor == -1:
            return idx+1

print('part1:', part1(line))
print('part2:', part2(line))

