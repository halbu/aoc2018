data = [l.rstrip('\n') for l in open('./aoc2018-day18.data', "r")]
grid = [['.' for _ in range(len(data[0]))] for _ in range(len(data))]
w, h = len(data[0]), len(data)

def main():
  for i, l in enumerate(data):
    for j, c in enumerate(l):
      grid[i][j] = c

  for i in range(1, 1000000001):
    tick()
    if (i) % 1000 == 0:
      print('Minutes', i)
      report()
  # Output shows a repeating value at 1000, 8000, 15000, 27000... of 174420
  # therefore if (i - 1000) % 7000 == 0 resource value will be 174420
  
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

def report():
  trees = 0
  yards = 0
  for l in grid:
    for c in l:
      if c == '#':
        yards += 1
      elif c == '|':
        trees += 1
    
  print('Trees:', trees)
  print('Yards:', yards)
  print('Resource Value:', trees * yards)

if __name__ == '__main__':
  main()


#   --- Part Two ---
# This important natural resource will need to last for at least thousands of years. Are the Elves collecting this lumber sustainably?

# What will the total resource value of the lumber collection area be after 1000000000 minutes?