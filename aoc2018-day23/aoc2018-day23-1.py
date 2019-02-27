def distance_between(a, b):
  return abs(a['x'] - b['x']) + abs(a['y'] - b['y']) + abs(a['z'] - b['z'])

bots = []

for l in [l.strip() for l in open('./aoc2018-day23.data', "r") if l != "\n"]:
  xyz = [int(s) for s in l.split("<")[1].split(">")[0].split(",")]
  bots.append({'x': xyz[0], 'y': xyz[1], 'z': xyz[2], 's': int(l.split("=")[2])})

ssb = sorted(bots, key=lambda x: x['s'], reverse=True)[0] # 'strongest signal bot'
print('Solution:', sum(1 for b in bots if distance_between(b, ssb) <= ssb['s']))