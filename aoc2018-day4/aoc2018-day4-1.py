data = [str.rstrip(l) for l in open('./aoc2018-day4.data', "r")]
# data = [str.rstrip(l) for l in open('./test.data', "r")]
data.sort()

# First of all we're going to build a great big dict of dates that contains all the relevant info about a date.
# The key will be the date and the object will contain `guard_number` (string) and `minutes` (int[60])
datemap = {}
for line in data:
  tokens = line.split(" ")

  date_tokens = line[1:12].split("-")
  year, month, day = int(date_tokens[0]), int(date_tokens[1]), int(date_tokens[2])

  time = line[12:17]
  hour, minute = time.split(":")[0], time.split(":")[1]
  
  action = tokens[len(tokens)-2]

  # If a guard started their shift at 23:xx, that shift actually corresponds to the following day. Let's wrangle
  # the date to accommodate this, and shift the time forward to 00:00 as we don't care about the preceding minutes
  if int(hour) == 23:
    hour = 0
    minute = 0
    day += 1
  if (day == 29 and month == 2) or (day == 31 and month in [4, 6, 9, 11]) or day == 32:
    day = 1
    month += 1

  # Add this date to our map if it isn't already there, initialise the minutes array,
  # and tag it with the guard's number if there is a guard number present
  datestr = str(year)+'-'+str(month)+'-'+str(day)
  if datestr not in datemap:
    datemap[datestr] = {}
    datemap[datestr]['minutes'] = [0] * 60
  if tokens[len(tokens)-4] == "Guard":
    datemap[datestr]['guard_number'] = tokens[len(tokens)-3]

  # Mark the minutes on the `minutes` array as 1 (guard is awake) or 2 (guard is asleep)
  if action == "begins" or action == "wakes":
    smin = 0 if hour == '23' else minute
    for i in range(int(smin), 60, 1):
      datemap[datestr]['minutes'][i] = 1
  elif action == "falls":
    smin = 0 if hour == '23' else minute
    for i in range(int(smin), 60, 1):
      datemap[datestr]['minutes'][i] = 2

# Run through datemap and create a new dict, where key is each unique guard number
# and the value is their total minutes asleep
guardmap = {}
for c in datemap.keys():
  gn = datemap[c]['guard_number'][1:]
  minutes_sleeping = datemap[c]['minutes'].count(2)
  if gn in guardmap:
    guardmap[gn] += minutes_sleeping
  else:
    guardmap[gn] = minutes_sleeping

# Find the sleepiest guard by getting the highest value in the guardmap and returning its key. Bad guard! You're fired!
sleepiest_guard = -1
highest = 0
for c in guardmap:
  if guardmap[c] > highest:
    highest = guardmap[c]
    sleepiest_guard = c

# Run through the datemap again looking for every day where this guard was on duty and pulling out the `minutes` arrays
this_guards_activity = []
for c in datemap:
  entry = datemap[c]
  if entry['guard_number'][1:] == sleepiest_guard:
    this_guards_activity.append(entry['minutes'])

# Run through the list of all hour-long periods that guard was on duty, and calculate, for each minute, how many times
# the guard was observed to be asleep on that minute
minutes = [0] * 60
for i in this_guards_activity:
  for j in range(0, 60, 1):
    if i[j] == 2:
      minutes[j] += 1

# Find the minute with the highest sleep frequency...
sleepiest_minute = minutes.index(max(minutes))

# ¡Ole!
print(str(int(sleepiest_guard) * sleepiest_minute))