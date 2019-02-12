data = [l.strip() for l in open('./aoc2018-day17.data', "r") if l != "\n"]
scan, stack = [], []
xmin, xmax, ymin, ymax = -1, -1, -1, -1

def main():
  setup()
  stack.append({'ins': 'pour', 'x': 500, 'y': 1})
  simulate()
  print_scan()
  
  total_water = 0
  for x in range(xmin, xmax+1):
    for y in range(ymin, ymax+1):
      if scan[x][y] == '~' or scan[x][y] == '|':
        total_water += 1
  print('Solution: ' + str(total_water))

def simulate():
  while stack:
    action = stack.pop()
    instr = action['ins']
    x = action['x']
    y = action['y']

    if instr == 'pour':
      scan[x][y] = '|'
      if y + 1 > ymax:
        continue
      if scan[x][y + 1] == '.':
        stack.append({'ins': 'pour', 'x': x, 'y': y + 1})
      elif scan[x][y + 1] != '|':
        stack.append({'ins': 'spread', 'x': x, 'y': y})
    elif instr == 'spread':
      if fully_bounded(x, y):
        fill_row(x, y)
        stack.append({'ins': 'spread', 'x': x, 'y': y - 1})
      else:
        fill_and_spill(x, y)

def fully_bounded(x, y):
  for n in [-1, 1]:
    tx = x + n
    while tx >= 0 and tx <= xmax and scan[tx][y] != '#':
      if (scan[tx][y + 1] != '#' and scan[tx][y + 1] != '~'):
        return False
      else:
        tx += n
  return True

def fill_row(x, y):
  global scan
  scan[x][y] = '~'
  for n in [-1, 1]:
    tx = x + n
    while scan[tx][y] != '#':
      scan[tx][y] = '~'
      tx += n

def fill_and_spill(x, y):
  global scan
  global stack
  scan[x][y] = '|'
  for n in [-1, 1]:
    tx = x + n
    while tx >=0 and tx <= xmax and scan[tx][y] != '#':
      scan[tx][y] = '|'
      if scan[tx][y + 1] != '#' and scan[tx][y + 1] != '~':
        stack.append({'ins': 'pour', 'x': tx, 'y': y})
        break
      tx += n

def setup():
  global scan
  global xmin, xmax, ymin, ymax
  points = []
  for l in data:
    t1 = l.split(', ')[0].split('=')
    t2 = l.split(', ')[1].split('=')
    t2range = t2[1].split('..')

    for i in range(int(t2range[1]) - int(t2range[0]) + 1):
      if t1[0] == 'x':
        points.append({'x' : int(t1[1]), 'y': int(t2range[0]) + i })
      else:
        points.append({'y' : int(t1[1]), 'x': int(t2range[0]) + i })
  
  xseq, yseq = [e['x'] for e in points], [e['y'] for e in points]
  xmin, xmax = min(xseq), max(xseq) + 1
  ymin, ymax = min(yseq), max(yseq)

  for x in range(0,xmax+1):
    scan.append([])
    for y in range(0, ymax+1):
      scan[x].append('.')

  for p in points:
    scan[int(p['x'])][int(p['y'])] = '#'

  scan[500][0] = '+'

def print_scan():
  for y in range(0, ymax+1):
    output = ''
    for x in range (xmin, xmax+1):
      output += scan[x][y]
    print(output)

if __name__ == '__main__':
  main()