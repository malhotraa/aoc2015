from functools import reduce
import re

with open('input.txt') as f:
    lines = f.read().split('\n')
    ingredients = []
    for line in lines:
        m = re.match(r'([A-Za-z]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line)
        name, cap, dur, fla, tex, cal = m.groups()
        ingredients.append((name, int(cap), int(dur), int(fla), int(tex), int(cal)))

def score_recipe(ingredients, recipe):
    cap = dur = fla = tex = 0
    for ing, amnt in zip(ingredients, recipe):
        cap += ing[1] * amnt
        dur += ing[2] * amnt
        fla += ing[3] * amnt
        tex += ing[4] * amnt
    return max(0, cap) * max(0, dur) * max(0, fla) * max(0, tex)

def calories(ingredients, recipe):
    return sum(ing[5] * amnt for ing, amnt in zip(ingredients, recipe))

def dfs(ingredients, recipe, idx, cal = None):
    if sum(recipe) == 100:
        if cal is not None and calories(ingredients, recipe) != cal:
            return 0
        return score_recipe(ingredients, recipe)
    
    if idx >= len(ingredients):
        return 0
    
    scores = []
    for i in range(101):
        recipe[idx] = i
        scores.append(dfs(ingredients, recipe, idx+1, cal))
    
    return max(scores)

def part1(ingredients):
    return dfs(ingredients, [0] * len(ingredients), 0)

def part2(ingredients):
    return dfs(ingredients, [0] * len(ingredients), 0, 500)

print('part1:', part1(ingredients))
print('part2:', part2(ingredients))