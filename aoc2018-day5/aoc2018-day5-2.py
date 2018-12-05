import re
import datetime

polymer = [str.rstrip(l) for l in open('./aoc2018-day5.data', "r")][0]
lengths = []

def main():
  for letter in list('abcdefghijklmnopqrstuvwxyz'):
    reacted = list(fully_react(polymer, letter))
    length = get_reduced_length(reacted)
    lengths.append(length)
    print('Processed ' + letter + '.' * (ord(letter) - 94))
  
  print('Solution: ' + str(min(lengths)))

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

def fully_react(polymer, char):
  return re.sub(r'[' + str.upper(char) + char + ']', '', ''.join(polymer))

def get_reduced_length(polymer):
  r = react(polymer)
  while(r != polymer):
    r = polymer
    polymer = react(polymer)
  return len(''.join(polymer))

if __name__ == '__main__':
  main()