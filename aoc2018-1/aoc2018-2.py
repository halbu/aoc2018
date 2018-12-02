import sys
count = 0
appearances = {}
file = open('./aoc2018-1.data', "r")

while(True):
  file.seek(0)
  for line in file:
    if (count = count + int(line)) in appearances.keys():
      print('First repeated frequency: ' + str(count))
      sys.exit()
    appearances[count] = 1