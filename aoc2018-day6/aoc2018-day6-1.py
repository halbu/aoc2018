def main():
  points = list([str.rstrip(l) for l in open('./aoc2018-day6.data', "r")])
  gs = 360
  
  grid = []
  for i in range(0, gs):
    grid.append([])
    for j in range(0, gs):
      grid[i].append({ 'd': 999, 'p': '.' })

  for p in points:
    x = int(p.split(', ')[0])
    y = int(p.split(', ')[1])
    for i in range(0, gs, 1):
      for j in range(0, gs, 1):
        cdist = grid[i][j]['d']
        dist = get_manhattan_dist(x, y, i, j)
        if dist < cdist:
          grid[i][j]['d'] = dist
          grid[i][j]['p'] = p
        elif dist == cdist:
          grid[i][j]['p'] = '.'

  out = {}
  for i in range(0, gs):
    for j in range(0, gs):
      if grid[i][j]['p'] not in out.keys():
        out[grid[i][j]['p']] = 1
      else:
        out[grid[i][j]['p']] += 1

  # disregard all points that touch the edge of our grid as these are infinite
  disregard = {}
  for i in range(0, gs):
    key = grid[i][0]['p']
    if grid[i][0]['p'] not in disregard.keys():
      disregard[grid[i][0]['p']] = True
    if grid[i][gs-1]['p'] not in disregard.keys():
      disregard[grid[i][gs-1]['p']] = True
    if grid[0][i]['p'] not in disregard.keys():
      disregard[grid[0][i]['p']] = True
    if grid[gs-1][i]['p'] not in disregard.keys():
      disregard[grid[gs-1][i]['p']] = True

  for w in sorted(out, key=out.get, reverse=True):
    if w not in disregard.keys():
      print("Point", w, "has region size", out[w])

def get_manhattan_dist(x, y, i, j):
  output = abs(x - i) + abs(y - j)
  return output

if __name__ == '__main__':
  main()