data = open('./aoc2018-day2.data', "r")

doubles = 0
triples = 0

for line in data:
  chars = {}
  for c in line:
    if c not in chars:
      chars[c] = 1
    else:
      chars[c] = chars[c] + 1
  
  logged_a_double = False
  logged_a_triple = False
  for key in chars:
    if chars[key] == 2 and not logged_a_double:
      doubles = doubles + 1
      logged_a_double = True
    if chars[key] == 3 and not logged_a_triple:
      triples = triples + 1
      logged_a_triple = True

print('Checksum (doubles * triples) = ' + str(doubles * triples))