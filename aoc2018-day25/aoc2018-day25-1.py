points, cpoints = [], []

def main():
  for l in [l.rstrip('\n') for l in open('./aoc2018-day25.data', "r")]:
    tokens = [int(x) for x in l.split(',')]
    points.append({'x': tokens[0], 'y': tokens[1], 'z': tokens[2], 't': tokens[3], 'c': None})

  cpoints.append(points[0])
  cpoints[0]['c'] = 0
  new_constellation_index = 1

  while(points):
    new_point = points.pop()
    constellation_match = False
    for cpoint in cpoints:
      if not constellation_match:
        if within_three(new_point, cpoint):
          constellation_match = True
          new_point['c'] = cpoint['c']
          cpoints.append(new_point)
    if not constellation_match:
      new_point['c'] = new_constellation_index
      new_constellation_index += 1
      cpoints.append(new_point)

  # Iteratively agglomerate constellations
  found_no_refinement = False
  while not found_no_refinement:
    found_overlap = False
    plist = set([x['c'] for x in cpoints])
    for i in plist:
      for j in plist:
        if i == j: continue
        if not found_overlap:
          if constellation_overlap(i, j):
            found_overlap = True
            for c in cpoints:
              if c['c'] == j:
                c['c'] = i
            continue
    
    if not found_overlap:
      found_no_refinement = True

  print('Solution: ' + str(len(set([x['c'] for x in cpoints]))))

def within_three(a, b):
  td = abs(a['x'] - b['x']) + abs(a['y'] - b['y']) + abs(a['z'] - b['z']) + abs(a['t'] - b['t'])
  return td <= 3

def constellation_overlap(x, y):
  c1 = [i for i in cpoints if i['c'] == x]
  c2 = [i for i in cpoints if i['c'] == y]

  for p1 in c1:
    for p2 in c2:
      if within_three(p1, p2):
        return True
  
  return False

if __name__ == '__main__':
  main()