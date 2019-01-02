data = list([str.rstrip(l) for l in open('./aoc2018-day15.data', "r")])
world = [["." for _ in range(len(data[0]))] for _ in range(len(data))]
actors = []
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

class Actor():
  def __init__(self, c, x, y):
    self.x = x
    self.y = y
    self.c = c
    self.hp = 200
    self.ap = 3
    self.acted_this_turn = False
    self.tag_map()
  
  def tag_map(self):
    world[self.x][self.y] = self.c

  def untag_map(self):
    world[self.x][self.y] = '.'
  
  def find_target(self):
    targets = [i for i in actors if i.c != self.c]
    paths = []
    for t in targets:
      i = 1
      paths.append(self.find_path(t))

  def find_path(self, t):
    openlist = [Node(self.x, self.y, 0)]

    while(openlist):
      cnode = openlist.pop(0)
      # hmm

  def report(self):
    print(vars(self))

class Node():
  def __init__(self, x, y, s):
    self.x = x
    self.y = y
    self.s = s

def main():
  setup()
  for l in world:
    print(''.join(l))

def setup():
  global world
  global actors
  for i, l in enumerate(data):
    for j, c in enumerate(l):
      world[i][j] = '#' if c == '#' else '.'
      if c in ['E', 'G']:
        actors.append(Actor(c, i, j))




if __name__ == '__main__':
  main()