from frozendict import frozendict
from functools import lru_cache

with open('input.txt') as f:
    lines = f.read().split('\n')

@lru_cache(maxsize=None)
def wire_value(wire_to_input, wire):
    wire = wire.strip()
    if wire.isnumeric(): # Not an actual wire
        return int(wire)

    if wire not in wire_to_input:
        raise Exception('Wire {} not found in circuit'.format(wire))
    
    inp = wire_to_input[wire]

    if inp.isalpha():
        return wire_value(wire_to_input, inp)
    elif inp.isnumeric():
        return int(inp)
    elif inp.find('AND') != -1:
        a, b = inp.split('AND')
        return wire_value(wire_to_input, a) & wire_value(wire_to_input, b)
    elif inp.find('OR') != -1:
        a, b = inp.split('OR')
        return wire_value(wire_to_input, a) | wire_value(wire_to_input, b)
    elif inp.find('LSHIFT') != -1:
        a, b = inp.split('LSHIFT')
        return wire_value(wire_to_input, a) << wire_value(wire_to_input, b)
    elif inp.find('RSHIFT') != -1:
        a, b = inp.split('RSHIFT')
        return wire_value(wire_to_input, a) >> wire_value(wire_to_input, b)
    elif inp.find('NOT') != -1:
        a = inp[len('NOT '):]
        return ~wire_value(wire_to_input, a)

def part1(lines):
    wire_to_input = dict()
    for line in lines:
        inp, wire = line.split('->')
        wire_to_input[wire.strip()] = inp.strip()
    
    return wire_value(frozendict(wire_to_input), 'a')

def part2(lines):
    wire_to_input = dict()
    for line in lines:
        inp, wire = line.split('->')
        wire_to_input[wire.strip()] = inp.strip()
    wire_to_input['b'] = '956'
    return wire_value(frozendict(wire_to_input), 'a')

print('part1:', part1(lines))
print('part2:', part2(lines))