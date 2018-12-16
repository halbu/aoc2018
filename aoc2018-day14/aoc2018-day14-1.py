data = int([l.rstrip('\n') for l in open('./aoc2018-day14.data', "r")][0])
elves = [0, 1]
recipes_created = 0
recipes = [3, 7]

def tick():
  global recipes
  global elves
  global recipes_created
  for c in str(recipes[elves[0]] + recipes[elves[1]]):
    recipes.append(int(c))
    recipes_created += 1
  for i in range(2):
    elves[i] = (elves[i] + recipes[elves[i]] + 1) % len(recipes)
    
while(recipes_created < data + 10):
  tick()

print(''.join(str(x) for x in recipes[data:data + 10]))