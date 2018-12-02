file = open('./aoc2018-1.data', "r")
count = 0
for line in file:
  count = count + int(line)
print('Final count: ' + str(count))