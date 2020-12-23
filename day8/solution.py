import re
import copy

with open('input.txt') as f:
    lines = f.read().split('\n')

def num_chars_in_memory(s: str):
    orig = copy.copy(s)
    s = s[1:-1]
    s = s.replace('''\\\"''', '"')
    s = s.replace('''\\\\''', '''?''')
    s = re.sub(r"\\x.{2}", '?', s)
    return len(s)

def num_chars_in_code_repr(s: str):
    orig = copy.copy(s)
    s = s.replace('"', '?"')
    s = s.replace('\\', '\\\\')
    s = s.replace('?', '\\')
    return len(s) + 2

def part1(lines):
    num_chars_code = 0
    num_chars_mem = 0
    for line in lines:
        num_chars_code += len(line)
        num_chars_mem += num_chars_in_memory(line)
    return num_chars_code - num_chars_mem

def part2(lines):
    num_chars_code = 0
    num_chars_repr = 0
    for line in lines:
        num_chars_code += len(line)
        num_chars_repr += num_chars_in_code_repr(line)
    return num_chars_repr - num_chars_code

print('part1:', part1(lines))
print('part2:', part2(lines))