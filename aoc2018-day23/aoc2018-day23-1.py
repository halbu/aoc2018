data = [l.strip() for l in open('./aoc2018-day23.data', "r") if l != "\n"]
bots = []

def distance_between(a, b):
  return abs(a['x'] - b['x']) + abs(a['y'] - b['y']) + abs(a['z'] - b['z'])
  
for l in data:
  signal = int(l.split("=")[2])
  xyz = [int(s) for s in l.split("<")[1].split(">")[0].split(",")] # lol
  bots.append({'x': xyz[0], 'y': xyz[1], 'z': xyz[2], 's': signal})

bots.sort(key=lambda x: x['s'], reverse=True)
ssb = bots[0] # 'strongest signal bot'
print('Solution:', sum(1 for b in bots if distance_between(b, ssb) <= ssb['s']))