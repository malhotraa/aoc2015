from collections import defaultdict
from itertools import permutations
import re

with open('input.txt') as f:
    lines = f.read().split('\n')
    graph = defaultdict(set)
    costs = defaultdict(list)
    for line in lines:
        m = re.match(r"([A-za-z]+) to ([A-za-z]+) = (\d+)", line)
        a, b, cost = m.groups()
        cost = int(cost)
        graph[a].add(b)
        graph[b].add(a)
        costs[(a, b)] = cost
        costs[(b, a)] = cost

def cost_of_path(path, costs):
    cost = 0
    for i in range(len(path)-1):
        cost += costs[(path[i], path[i+1])]
    return cost

def minmaxcost(graph, costs):
    all_nodes = list(graph.keys())
    min_cost = None
    max_cost = None
    for combo in permutations(all_nodes, len(all_nodes)):
        cost = cost_of_path(combo, costs)
        if min_cost is None or cost < min_cost:
            min_cost = cost
        if max_cost is None or cost > max_cost:
            max_cost = cost
    return min_cost, max_cost

print('part1and2:', minmaxcost(graph, costs))
