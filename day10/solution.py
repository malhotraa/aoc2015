def part1(inp, repeat):
    num = inp
    for r in range(repeat):
        new_num = ''
        freq = 1
        idx = 1
        while idx < len(num):
            if num[idx] == num[idx-1]:
                freq += 1
            else:
                new_num += (str(freq) + num[idx-1])
                freq = 1
            idx += 1
        
        new_num += (str(freq) + num[idx-1])
        num = new_num
    return len(num)

print('part1:', part1('1321131112', 40))
print('part2:', part1('1321131112', 50))