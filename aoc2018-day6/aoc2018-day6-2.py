def main():
  gs = 360
  points = []
  grid = [[0 for i in range(gs)] for j in range(gs)]

  for p in list([str.rstrip(l) for l in open('./aoc2018-day6.data', "r")]):
    x = int(p.split(', ')[0])
    y = int(p.split(', ')[1])
    points.append({'x': x, 'y': y})

  for i in range(0, gs, 1):
    for j in range(0, gs, 1):
      total_dist = 0
      for p in points:
        total_dist += abs(p['x'] - i) + abs(p['y'] - j)
      grid[i][j] = total_dist

  under_ten_thousand = 0
  for i in range(0, gs, 1):
    for j in range(0, gs, 1):
      if grid[i][j] < 10000:
        under_ten_thousand += 1

  print('Solution: ' + str(under_ten_thousand))

if __name__ == '__main__':
  main()