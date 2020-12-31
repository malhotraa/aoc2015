class Aunt:
    def __init__(self, num, attrs):
        self.num = num
        self.attrs = attrs

    def __hash__(self):
        return hash(self.num)

with open('input.txt') as f:
    lines = f.read().split('\n')
    aunts = set()
    for line in lines:
        idx = line.find(':')
        num = int(line[:idx].split(' ')[1])
        attrs = {}
        for attr_str in line[idx+1:].strip().split(','):
            attr, val = attr_str.split(':')
            attrs[attr.strip()] = int(val.strip())
        aunts.add(Aunt(num, attrs))

def part1_cond(aunt, attr, val):
    return aunt.attrs[attr] == val

def part2_cond(aunt, attr, val):
    if attr in ['cats', 'trees']:
        return aunt.attrs[attr] > val
    elif attr in ['pomeranians', 'goldfish']:
        return aunt.attrs[attr] < val
    else:
        return aunt.attrs[attr] == val

def part1(aunts, attrs, cond):
    possibles = set(aunt.num for aunt in aunts)
    for attr, val in attrs.items():
        for aunt in aunts:
            if aunt.num in possibles and attr in aunt.attrs and not cond(aunt, attr, val):
                possibles.remove(aunt.num)
    assert len(possibles) == 1
    return list(possibles)[0]

wanted_attrs = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

print('part1:', part1(aunts, wanted_attrs, part1_cond))
print('part2:', part1(aunts, wanted_attrs, part2_cond))