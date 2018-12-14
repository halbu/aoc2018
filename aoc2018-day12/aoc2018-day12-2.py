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
  
  for i in range(500001):
    if i == 5000 or i == 50000 or i == 500000:
      print('Sum at ' + str(i) + 'th iteration: ' + str(sum_plant_containing_pots()))
      # Output:
      # Sum at 5000th iteration: 491793
      # Sum at 50000th iteration: 4901793
      # Sum at 500000th iteration: 49001793
      # Therefore sum at 50bn iteration: 4900000001793 :P
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