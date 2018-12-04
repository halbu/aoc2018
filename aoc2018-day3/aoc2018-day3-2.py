fabric = []

def main():
  for i in range (1, 1000, 1):
    fabric.append([0] * 1000)

  for line in [l for l in open('./aoc2018-day3.data', "r")]:
    rect = rectanglize(line)
    tag_square_on_map(rect['x'], rect['y'], rect['w'], rect['h'])

  for line in [l for l in open('./aoc2018-day3.data', "r")]:
    if find_intact_claim(line):
      print(line)
      exit()

def tag_square_on_map(x, y, w, h):
  for i in range (x, (x + w), 1):
    for j in range (y, (y + h), 1):
      if (fabric[i][j] == 0):
        fabric[i][j] = 1
      else:
        fabric[i][j] = 2

def find_intact_claim(claim_string):
  rect = rectanglize(claim_string)
  
  for i in range (rect['x'], (rect['x'] + rect['w']), 1):
    for j in range (rect['y'], (rect['y'] + rect['h']), 1):
      if (fabric[i][j] == 2):
        return False
  
  return True

def rectanglize(claim_string): # I know
  tokens = claim_string.split(" ")

  loc = tokens[2][:-1]
  size = tokens[3]
  output = {}

  output['x'] = int(loc.split(",")[0])
  output['y'] = int(loc.split(",")[1])
  output['w'] = int(size.split("x")[0])
  output['h'] = int(size.split("x")[1])

  return output

if __name__ == '__main__':
  main()