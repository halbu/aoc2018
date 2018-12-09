data = ([l for l in open('./aoc2018-day9.data', "r")])[0].split(' ')

np, lmpv = int(data[0]), int(data[6]) # no. players, last marble placed value
players = [0] * np
ci, cp = 0, 0 # current index, current player
circle = []

def main():
  global cp

  for i in range(0, lmpv + 1):
    place_marble(i)
    cp = cp + 1 if cp + 1 < len(players) else 0
  print('Solution: ' + str(max(players)))

def place_marble(value):
  global ci

  if value % 23 != 0:
    ci = ci - len(circle) + 2 if ci + 2 > len(circle) else ci + 2

  if value and value % 23 == 0:
    ci = ci + len(circle) - 7 if ci - 7 < 0 else ci - 7
    players[cp] += value + circle[ci]
    del circle[ci]
  else:
    if ci == len(circle):
      circle.append(value)
    else:
      circle.insert(ci, value)
  
if __name__ == '__main__':
  main()