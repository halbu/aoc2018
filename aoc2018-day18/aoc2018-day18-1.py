data = [l.rstrip('\n') for l in open('./aoc2018-day18.data', "r")]
grid = [['.' for _ in range(len(data[0]))] for _ in range(len(data))]
w, h = len(data[0]), len(data)

def main():
  for i, l in enumerate(data):
    for j, c in enumerate(l):
      grid[i][j] = c

  for i in range(10):
    tick()

  print('Solution: ' + calculate_resource_value())

def tick():
  global grid
  new_grid = [['.' for _ in range(len(data[0]))] for _ in range(len(data))]

  for i, l in enumerate(grid):
    for j, c in enumerate(l):
      adj_trees = 0
      adj_yards = 0
      adj_open = 0
      for x in range(-1, 2):
        for y in range(-1, 2):
          if not (x == 0 and y == 0):
            if i + x >= 0 and i + x < w and j + y >= 0 and j + y < h:
              if grid[i + x][j + y] == "|":
                adj_trees += 1
              if grid[i + x][j + y] == "#":
                adj_yards += 1
              if grid[i + x][j + y] == ".":
                adj_open += 1
      if c == '.':
        new_grid[i][j] = '|' if adj_trees >= 3 else '.'
      if c == '|':
        new_grid[i][j] = '#' if adj_yards >= 3 else '|'
      if c == '#':
        new_grid[i][j] = '#' if (adj_trees >= 1 and adj_yards >= 1) else '.'
          
  grid = new_grid

def calculate_resource_value():
  trees = 0
  yards = 0
  for l in grid:
    for c in l:
      if c == '#':
        yards += 1
      elif c == '|':
        trees += 1
  return str(trees * yards)

def print_grid():
  for l in grid:
    print(''.join(l))

if __name__ == '__main__':
  main()