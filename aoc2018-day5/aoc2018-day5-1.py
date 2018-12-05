def main():
  data = list([str.rstrip(l) for l in open('./aoc2018-day5.data', "r")][0])

  r = react(data)
  while(r != data):
    r = data
    data = react(data)

  print('Solution: ' + str(len(''.join(data))))

def react(polymer):
  out = ""
  i = 0
  while i < len(polymer):
    if i == len(polymer)-1:
      out = out + polymer[i]
      i += 1
    elif (abs(ord(polymer[i]) - ord(polymer[i+1])) == 32):
      i += 2
    else:
      out = out + polymer[i]
      i += 1
  return out

if __name__ == '__main__':
  main()