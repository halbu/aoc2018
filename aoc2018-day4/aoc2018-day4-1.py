data = [str.rstrip(l) for l in open('./aoc2018-day4.data', "r")]
data.sort()
datemap = {}

#for line in data:
for i in range(0, 10, 1):
  line = data[i]
  tokens = line.split(" ")

  date = line[1:12]
  time = line[12:17]
  hour = time.split(":")[0]
  minute = time.split(":")[1]
  action = tokens[len(tokens)-2] + " " + tokens[len(tokens)-1]

  if date not in datemap:
    datemap[date] = [0] * 60

  if action == "begins shift" or action == "wakes up":
    smin = 0 if hour == '23' else minute
    for i in range(int(smin), 60, 1):
      datemap[date][i] = 1
  elif action == "falls asleep":
    smin = 0 if hour == '23' else minute
    for i in range(int(smin), 60, 1):
      datemap[date][i] = 2