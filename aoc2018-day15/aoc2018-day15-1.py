data = list([str.rstrip(l) for l in open('./test2.data', "r")])
w, h = len(data[0]), len(data)
world = [['.' for _ in range(h)] for _ in range(w)]
actors = []

def main():
  for i in range(w):
    for j in range(h):
      c = data[j][i]
      world[i][j] = '#' if c == '#' else '.'
      if c in ['G', 'E']:
        actors.append(Actor(c, i, j))
  print_world()

def print_world():
  for j in range(h):
    output = ''
    for i in range(w):
      output += world[i][j]
    print(output)

class Actor():
  def __init__(self, c, x, y):
    self.c, self.x, self.y = c, x, y
    self.hp = 200
    self.ap = 3
    self.acted_this_turn = False
    self.tag_map()
  
  def tag_map(self):
    world[self.x][self.y] = self.c

  def untag_map(self):
    world[self.x][self.y] = '.'

    # # flood fill from the goal point
    # dmap = []
    # for i in range(w):
    #   for j in range(h):
    #     if i == target['x'] and j == target['y']:
    #       dmap.append(0)
    #     elif world[i][j] == '.':
    #       dmap.append(99999) # arbitrary high number for passable tiles
    #     else:
    #       dmap.append(100000) # arbitrary number assigned to impassable tiles

    # mutated = True
    # while mutated:
    #   mutated_this_iteration = False
    #   for i in range(len(dmap)):
    #     if i == 100000:
    #       continue # skip tiles with our impassable integer in them
    #     elif get_lowest_neighbour(i) + 1 < dmap[i]:
    #       dmap[i] = get_lowest_neighbour(i) + 1
    #       mutated_this_iteration = True
    #   mutated = mutated_this_iteration

    
if __name__ == '__main__':
  main()