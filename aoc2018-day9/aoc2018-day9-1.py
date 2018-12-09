data = ([l for l in open('./aoc2018-day9.data', "r")])[0].split(' ')

np, lmpv = int(data[0]), int(data[6]) # no. players, last marble placed value
players = [0] * np
ci, cp = 0, 0 # current index, current player
circle = []

def main():
  global cp

  for i in range(0, lmpv + 1):
    place_marble(i)
    cp = (cp + 1) % len(players)
  print('Solution: ' + str(max(players)))

def place_marble(value):
  global ci

  if value % 23 != 0:
    ci = (ci + 2) % len(circle)

  if value and value % 23 == 0:
    ci = (ci - 7) % len(circle)
    players[cp] += value + circle[ci]
    del circle[ci]
  else:
    if ci == len(circle):
      circle.append(value)
    else:
      circle.insert(ci, value)
  
if __name__ == '__main__':
  main()