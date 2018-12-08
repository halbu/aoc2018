
data = ([str.rstrip(l) for l in open('./aoc2018-day8.data', "r")])[0]
dlist = [k for k in data.split(' ')]
metadata = []
index = 0

def main():
  while index < len(dlist):
    process_node()
  
  print('Solution: ' + str(sum(metadata)))

def process_node():
  global index

  num_children = int(dlist[index])
  num_metadatas = int(dlist[index + 1])
  index += 2

  for i in range(0, num_children):
    process_node()
  
  for j in range(0, num_metadatas):
    metadata.append(int(dlist[index]))
    index += 1

if __name__ == '__main__':
  main()