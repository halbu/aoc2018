data = [l.strip() for l in open('./aoc2018-day21.data', "r") if l != "\n"]
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

# The geologic index can be determined using the first rule that applies from the list below:
# The region at 0,0 (the mouth of the cave) has a geologic index of 0.
# The region at the coordinates of the target has a geologic index of 0.
# If the region's Y coordinate is 0, the geologic index is its X coordinate times 16807.
# If the region's X coordinate is 0, the geologic index is its Y coordinate times 48271.
# Otherwise, the region's geologic index is the result of multiplying the erosion levels of the regions at X-1,Y and X,Y-1.
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

# A region's erosion level is its geologic index plus the cave system's depth, all modulo 20183. Then:
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