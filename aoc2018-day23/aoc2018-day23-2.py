import math
bots = []

def main():
  global bots
  mx, my, mz = 0, 0, 0

  # get our big list of bots
  for l in [l.strip() for l in open('./test.data', "r") if l != "\n"]:
    xyz = [int(s) for s in l.split("<")[1].split(">")[0].split(",")]
    bots.append({'x': xyz[0], 'y': xyz[1], 'z': xyz[2], 's': int(l.split("=")[2])})

  cube = {'x': 0, 'y': 0, 'z': 0, 'e': 128}

  # recurively divide cube into 8 subcubes and return the subcube which overlaps
  # with the most bot signals (this may be entirely the wrong way of doing this)
  for i in range(0, 100):
    cube = get_best_subcube(cube)

  print(cube)

def get_best_subcube(cube):
  half_e = cube['e']/2

  c1 = {'x': cube['x'],          'y': cube['y'],          'z': cube['z'],          'e': half_e}
  c2 = {'x': cube['x'] + half_e, 'y': cube['y'],          'z': cube['z'],          'e': half_e}
  c3 = {'x': cube['x'],          'y': cube['y'] + half_e, 'z': cube['z'],          'e': half_e}
  c4 = {'x': cube['x'] + half_e, 'y': cube['y'] + half_e, 'z': cube['z'],          'e': half_e}
  c5 = {'x': cube['x'],          'y': cube['y'],          'z': cube['z'] + half_e, 'e': half_e}
  c6 = {'x': cube['x'] + half_e, 'y': cube['y'],          'z': cube['z'] + half_e, 'e': half_e}
  c7 = {'x': cube['x'],          'y': cube['y'] + half_e, 'z': cube['z'] + half_e, 'e': half_e}
  c8 = {'x': cube['x'] + half_e, 'y': cube['y'] + half_e, 'z': cube['z'] + half_e, 'e': half_e}

  topcount, topcube = 0, None
  for c in [c1,c2,c3,c4,c5,c6,c7,c8]:
    count = 0
    for b in bots:
      sphere = {'x': b['x'], 'y': b['y'], 'z': b['z'], 'r': b['s']}
      if sphere_overlaps_cube(c, sphere):
        count += 1
    
    if count > topcount:
      topcount = count
      topcube = c
  
  return topcube

def sqr(num):
  return num * num

def sphere_overlaps_cube(cube, sphere):
  # hm

if __name__ == '__main__':
  main()