from collections import defaultdict
import re

class Reindeer:
    def __init__(self, name, speed, move_s, rest_s):
        self.name = name
        self.speed = speed
        self.move_s = move_s
        self.rest_s = rest_s
    
    def __repr__(self):
        return "Reindeer(name={}, speed={}km/s, move_s={}s, rest_s={}s".format(self.name, self.speed, self.move_s, self.rest_s)

    def __hash__(self):
        return hash(self.name)

with open('input.txt') as f:
    lines = f.read().split('\n')
    reindeer = []
    for line in lines:
        m = re.match(r'([A-Za-z]+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)
        name, speed, move_s, rest_s = m.groups()
        reindeer.append(Reindeer(name, int(speed), int(move_s), int(rest_s)))

def distance(reindeer, duration):
    move_and_rest_s = reindeer.move_s + reindeer.rest_s
    full_cycles = duration // move_and_rest_s
    remaining_s = duration % move_and_rest_s
    dist = full_cycles * reindeer.speed * reindeer.move_s
    dist += (reindeer.speed * min(remaining_s, reindeer.move_s))
    return dist

def state(reindeer, time):
    move_and_rest_s = reindeer.move_s + reindeer.rest_s
    if time % move_and_rest_s < reindeer.move_s:
        return 'FLYING'
    else:
        return 'RESTING'

def part1(reindeer, duration):
    return max(distance(r, duration) for r in reindeer)

def part2(reindeer, duration):
    points_per_deer = defaultdict(int)
    dist_per_deer = defaultdict(int)
    for t in range(0, duration):
        for r in reindeer:
            if state(r, t) == 'FLYING':
                dist_per_deer[r] += r.speed
        max_dist_reindeer = max(dist_per_deer, key=lambda k: dist_per_deer[k])
        points_per_deer[max_dist_reindeer] += 1
    return max(points_per_deer.values())

print('part1:', part1(reindeer, 2503))
print('part2:', part2(reindeer, 2503))