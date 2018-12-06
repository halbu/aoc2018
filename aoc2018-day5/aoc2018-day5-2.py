import re

polymer = [str.rstrip(l) for l in open('./aoc2018-day5.data', "r")][0]
lengths = []

def main():
  for letter in list('abcdefghijklmnopqrstuvwxyz'):
    fully_reacted_polymer = list(fully_react(polymer, letter))
    lengths.append(react(fully_reacted_polymer))

  print('Solution: ' + str(min(lengths)))
  
def react(polymer):
  i = 0
  out = []
  while i < len(polymer):
    if i < len(polymer)-1 and out and (abs(ord(polymer[i]) - ord(out[len(out)-1])) == 32):
      if out:
        out.pop()
    else:
      out.append(polymer[i])
    i += 1
  return len(out)

def fully_react(polymer, char):
  return re.sub(r'[' + str.upper(char) + char + ']', '', ''.join(polymer))

if __name__ == '__main__':
  main()