data = list([str.rstrip(l) for l in open('./aoc2018-day10.data', "r")])
stars = []
f = 1

def main():
  global f
  
  for l in data:
    # Crude hacking up of string to get position and velocity data. TODO: refine!
    s = l[10:-1]
    s = s.split(">")
    s[1] = s[1][11:]
    p = s[0].split(",")
    v = s[1].split(",")
    stars.append({'px':int(p[0]), 'py':int(p[1]), 'vx':int(v[0]), 'vy':int(v[1])})
  
  while(1):
    advance_time()
    test_convergence()
    f += 1

def advance_time():
  for s in stars:
    s['px'] += s['vx']
    s['py'] += s['vy']

def test_convergence():
  x = [s['px'] for s in stars]
  y = [s['py'] for s in stars]

  if max(y) - min(y) < 10:
    print('Solution: ' + str(f)  + 's')
    exit()

if __name__ == '__main__':
  main()