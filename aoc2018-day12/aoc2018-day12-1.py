data = [str.rstrip(l) for l in open('./aoc2018-day12.data', "r")]

leftmost = 0
state = ""
m = {}

def main():
  global state
  state = data[0].split(" ")[2]
  for l in data[2:]:
    l = l.split(" => ")
    m[l[0]] = l[1]
  
  for i in range(20):
    iterate()
  
  print(sum_plant_containing_pots())

def iterate():
  global state
  global leftmost
  new_state = ""
  leftmost -= 2
  state = '..' + state + '..'
  for i in range(0, len(state)):
    locality = ""
    for j in range(-2, 3):
      locality = locality + state[i + j] if i + j >= 0 and i + j < len(state) else locality + '.'
    new_state = new_state + '#' if locality in m and m[locality] == "#" else new_state + '.'

  while new_state[0] == '.':
    leftmost += 1
    new_state = new_state[1:]
    
  while new_state[len(new_state)-1] == '.':
    new_state = new_state[:-1]
    
  state = new_state

def sum_plant_containing_pots():
  total = 0
  for s in range(0, len(state)):
    if state[s] == '#':
      total += (s + leftmost)
  return total

if __name__ == '__main__':
  main()