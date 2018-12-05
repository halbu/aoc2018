import datetime

def main():
  data = list([str.rstrip(l) for l in open('./aoc2018-day5.data', "r")][0])

  r = react(data)
  while(r != data):
    r = data
    data = react(data)
  
  # alternatively: half the lines, half the speed!
  # while(data != react(data)):
  #   data = react(data)

  print(len(''.join(data)))

def react(polymer):
  for i in range (1, len(polymer), 1):
    if (str.lower(polymer[i]) == str.lower(polymer[i-1])):
      if (ord(polymer[i]) != ord(polymer[i-1])): # polarity check
        return polymer[:i-1] + polymer[i+1:]
  return polymer

if __name__ == '__main__':
  main()