from collections import defaultdict
from itertools import permutations
import re

with open('input.txt') as f:
    lines = f.read().split('\n')
    graph = defaultdict(set)
    costs = {}
    for line in lines:
        m = re.match(r'([A-Za-z]+) would (lose|gain) (\d+) happiness units by sitting next to ([A-Za-z]+)', line)
        node1, action, pts, node2 = m.groups()
        graph[node1].add(node2)
        costs[(node1, node2)] = (-1 if action == 'lose' else 1) * int(pts)

def happiness(seating, costs):
    h = 0
    for i in range(len(seating)):
        j = (i + 1) % len(seating)
        h = h + costs[(seating[i], seating[j])] + costs[(seating[j], seating[i])]
    return h

def part1(graph, costs):
    max_ = None
    all_nodes = list(graph.keys())
    for combo in permutations(all_nodes, len(all_nodes)):
        h = happiness(combo, costs)
        if max_ is None or h > max_:
            max_ = h
    return max_

def part2(graph, costs):
    all_nodes = list(graph.keys())
    for node in all_nodes:
        graph[node].add('me')
        graph['me'].add(node)
        costs[(node, 'me')] = 0
        costs[('me', node)] = 0
    return part1(graph, costs)

print('part1:', part1(graph, costs))
print('part2:', part2(graph, costs))