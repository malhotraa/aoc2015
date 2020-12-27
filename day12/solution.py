import json

with open('input.txt') as f:
    json_str = json.loads(f.read())

def part1_sum(elem):
    if isinstance(elem, dict):
        return sum(map(part1_sum, elem.values()))
    elif isinstance(elem, list):
        return sum(map(part1_sum, elem))
    elif isinstance(elem, int):
        return elem
    elif isinstance(elem, str):
        return 0

def part2_sum(elem):
    if isinstance(elem, dict):
        ignore = any(v == "red" for v in elem.values()) 
        return 0 if ignore else sum(map(part2_sum, elem.values()))
    elif isinstance(elem, list):
        return sum(map(part2_sum, elem))
    elif isinstance(elem, int):
        return elem
    elif isinstance(elem, str):
        return 0

def part1(json_str):
    return part1_sum(json_str)

def part2(json_str):
    return part2_sum(json_str)

print('part1:', part1(json_str))
print('part2:', part2(json_str))