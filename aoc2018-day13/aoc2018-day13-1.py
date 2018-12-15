import random
data = [l.rstrip('\n') for l in open('./aoc2018-day13.data', "r")]
h, w = len(data), len(data[0])
track_grid = [['.' for _ in range(h)] for _ in range(w)]
carts = []

# Translation maps
dirs = {"^": "U", "v": "D", "<": "L", ">": "R"}
turn_order = {"L": "S", "S": "R", "R": "L"}
left_turn = { "U": "L", "L": "D", "D": "R", "R": "U"}
right_turn = { "U": "R", "R": "D", "D": "L", "L": "U"}
deltas = {"U": [0, -1], "D": [0, 1], "L": [-1, 0], "R": [1, 0]}
backslash = {"U": "L", "D": "R", "R": "D", "L": "U"}
forwardslash = {"U": "R", "D": "L", "R": "U", "L": "D"}

class Cart():
  def __init__(self, x, y, d):
    self.x = x
    self.y = y
    self.d = d
    self.t = "L"
    self.uid = random.uniform(0, 1)

  def act(self):
    self.x += deltas[self.d][0]
    self.y += deltas[self.d][1]

    # Test for crash
    for c in carts:
      if c.uid != self.uid and c.x == self.x and c.y == self.y:
        print('Crash!!! ' + str(self.x) + ', ' + str(self.y))
        exit()

    # Determine new direction
    gs = track_grid[self.x][self.y]
    if gs in ["\\", "/"]:
      self.d = backslash[self.d] if gs == "\\" else forwardslash[self.d]
    elif gs == "+":
      if self.t == "L":
        self.d = left_turn[self.d]
      elif self.t == "R":
        self.d = right_turn[self.d]
      self.t = turn_order[self.t]

def main():
  setup()
  while(True):
    tick()  

def setup():
  global track_grid
  for i in range(0, w):
    for j in range(0, h):
      if data[j][i] in ["<", ">", "^", "v"]:
        carts.append(Cart(i, j, dirs[data[j][i]]))
        track_grid[i][j] = "-" if data[j][i] in ["<", ">"] else "|"
      else:
        track_grid[i][j] = data[j][i]

def tick():
  global carts
  carts = sorted(carts, key=lambda c: c.y * w + c.x)
  for c in carts:
    c.act()

if __name__ == '__main__':
  main()