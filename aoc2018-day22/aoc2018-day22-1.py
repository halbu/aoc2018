data = [l.strip() for l in open('./aoc2018-day22.data', "r") if l != "\n"]
depth, tx, ty = 0, 0, 0
erosion_grid = []

def main():
  global tx, ty, depth, erosion_grid

  depth = int(data[0].split(' ')[1])
  target = data[1].split(' ')[1]
  tx, ty = int(target.split(',')[0]), int(target.split(',')[1])

  for x in range (0, tx + 1):
    erosion_grid.append([])
    for y in range (0, ty + 1):
      erosion_grid[x].append(get_erosion_level(get_geological_index(x, y)))

  print('Solution: ' + str(calculate_total_risk()))

def get_geological_index(x, y):
  if x == 0 and y == 0:
    return 0
  elif x == tx and y == ty:
    return 0
  elif y == 0:
    return x * 16807
  elif x == 0:
    return y * 48271
  else:
    return erosion_grid[x - 1][y] * erosion_grid[x][y - 1]

def get_erosion_level(geologic_index):
  return (geologic_index + depth) % 20183

def calculate_total_risk():
  total_risk = 0
  for y in range(0, ty + 1):
    for x in range (0, tx + 1):
      total_risk += erosion_grid[x][y] % 3
  return total_risk

if __name__ == '__main__':
  main()