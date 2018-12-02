count = 0
appearances = {}

while(True):
  for line in open('./aoc2018-day1.data', "r"):
    count = count + int(line)
    if count in appearances.keys():
      print('First repeated frequency: ' + str(count))
      exit()
    appearances[count] = 1