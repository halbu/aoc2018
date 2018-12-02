import sys
count = 0
appearances = {}
file = open('./aoc2018-1.data', "r")

while(True):
  file.seek(0)
  for line in file:
    count = count + int(line)
    if count in appearances.keys():
      print('First repeated frequency: ' + str(count))
      sys.exit()
    appearances[count] = 1