data = [str.rstrip(l) for l in open('./aoc2018-day4.data', "r")]
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
  for i in range(int(minute), 60, 1):
    datemap[datestr]['minutes'][i] = 1 if action in ["begins", "wakes"] else 2

# Run through datemap and build a new dict, where key = guard number, value = array of int[60] representing minutes
# For each entry in the datemap, look up the associated guard in the new dict and increment every minute in the array
# where that guard was observed to be asleep
guard_sleep_map = {}
for c in datemap.keys():
  guard_number = datemap[c]['guard_number'][1:]
  minutes_sleeping = datemap[c]['minutes'].count(2)
  if guard_number not in guard_sleep_map:
    guard_sleep_map[guard_number] = [0] * 60

  for i in range(0, 60, 1):
    if datemap[c]['minutes'][i] == 2:
      guard_sleep_map[guard_number][i] += 1

answer_guard = ""
answer_minute, highest_frequency = -1, -1

for g in guard_sleep_map:
  for i in range(0, 60, 1):
    if guard_sleep_map[g][i] > highest_frequency:
      answer_guard = g
      answer_minute = i
      highest_frequency = guard_sleep_map[g][i]

print('Solution: guard ' + str(answer_guard) + ', minute ' + str(answer_minute))