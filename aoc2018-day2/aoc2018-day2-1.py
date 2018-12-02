doubles, triples = 0, 0

for line in open('./aoc2018-day2.data', "r"):
  chars = {}
  for c in line:
    if c not in chars:
      chars[c] = 1
    else:
      chars[c] = chars[c] + 1

  if 2 in chars.values():
    doubles = doubles + 1
  if 3 in chars.values():
    triples = triples + 1

print('Checksum (doubles * triples) = ' + str(doubles * triples))