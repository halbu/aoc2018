data = open('./aoc2018-day2.data', "r")

twotimes = 0
threetimes = 0

for line in data:
  chars = {}
  for c in line:
    if c not in chars:
      chars[c] = 1
    else:
      chars[c] = chars[c] + 1
  
  logged_a_two = False
  logged_a_three = False
  for key in chars:
    if chars[key] == 2 and not logged_a_two:
      twotimes = twotimes + 1
      logged_a_two = True
    if chars[key] == 3 and not logged_a_three:
      threetimes = threetimes + 1
      logged_a_three = True

print('Two times: ' + str(twotimes))
print('Three times: ' + str(threetimes))