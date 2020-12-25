with open('input.txt') as f:
    lines = f.read().split('\n')

def part2_naughty(s: str):
    found = False
    for i in range(len(s)-2):
        query = s[i:i+2]
        found = found or (s[:i].find(query) != -1) or (s[i+2:].find(query) != -1)

    if not found:
        return True
    
    for c in map(chr, range(ord('a'), ord('z')+1)):
        for i in range(len(s)-2):
            if s[i] == c and s[i+2] == c:
                return False
    return True

def part1_naughty(s: str):
    vw_count = 0
    for c in ['a','e','i','o','u']:
        vw_count += s.count(c)

    if vw_count < 3:
        return True
    
    found = False
    for c in map(chr, range(ord('a'), ord('z')+1)):
        found = found or (s.find("{}{}".format(c, c)) != -1)

    if not found:
        return True

    for c in ['ab', 'cd', 'pq', 'xy']:
        if s.find(c) != -1:
            return True

    return False

def part1(lines):
    num = 0
    for line in lines:
        if not part1_naughty(line):
            num += 1
    return num

def part2(lines):
    num = 0
    for line in lines:
        if not part2_naughty(line):
            num += 1
    return num

print('part1:', part1(lines))
print('part2:', part2(lines))