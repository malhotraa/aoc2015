from collections import defaultdict
from itertools import combinations

with open('input.txt') as f:
    containers = list(map(int, f.read().split('\n')))

def part1(containers, target):
    min_num = None
    num_cont_to_ways = defaultdict(int)
    for c in range(1, len(containers)+1):
        for combo in combinations(containers, c):
            if sum(combo) == target:
                if min_num is None:
                    min_num = len(combo)
                min_num = min(min_num, len(combo))
                num_cont_to_ways[len(combo)] += 1
    return sum(num_cont_to_ways.values()), num_cont_to_ways[min_num]

print('part1:', part1(containers, 150)[0])
print('part2:', part1(containers, 150)[1])