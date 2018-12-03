fabric = []

def main():
  data = [l for l in open('./aoc2018-day3.data', "r")]

  for i in range (1, 1000, 1):
    fabric.append([0] * 1000)

  for line in data:
    process_claim(line)

  for line in data:
    if find_intact_claim(line):
      print(line)
      exit()

def process_claim(str):
  tokens = str.split(" ")

  loc = tokens[2][:-1]
  size = tokens[3]

  x = int(loc.split(",")[0])
  y = int(loc.split(",")[1])
  w = int(size.split("x")[0])
  h = int(size.split("x")[1])

  tag_square_on_map(x, y, w, h)

def tag_square_on_map(x, y, w, h):
  for i in range (x, (x + w), 1):
    for j in range (y, (y + h), 1):
      if (fabric[i][j] == 0):
        fabric[i][j] = 1
      else:
        fabric[i][j] = 2

def find_intact_claim(str):
  tokens = str.split(" ")

  # TODO: DRY
  loc = tokens[2][:-1]
  size = tokens[3]

  x = int(loc.split(",")[0])
  y = int(loc.split(",")[1])
  w = int(size.split("x")[0])
  h = int(size.split("x")[1])
  
  is_valid_claim = True
  for i in range (x, (x + w), 1):
    for j in range (y, (y + h), 1):
      if (fabric[i][j] == 2):
        is_valid_claim = False
  
  return is_valid_claim

if __name__ == '__main__':
  main()