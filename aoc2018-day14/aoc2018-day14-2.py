data = [l.strip() for l in open('./aoc2018-day14.data', "r")][0]
target_array = [int(c) for c in str(data)]
target_index = 0
elves = [0, 1]
recipes = [3, 7]

def tick():
  global recipes
  global elves
  for c in str(recipes[elves[0]] + recipes[elves[1]]):
    recipes.append(int(c))
    test_against_target(int(c))
  for i in range(2):
    elves[i] = (elves[i] + recipes[elves[i]] + 1) % len(recipes)

def test_against_target(i):
  global target_index
  if i == target_array[target_index]:
    target_index += 1
    if target_index == len(target_array):
      print('Length of recipe list (less the digits of the target number): ' + str(len(recipes) - len(target_array)))
      exit()
  else:
    target_index = 0

while(True):
  tick()