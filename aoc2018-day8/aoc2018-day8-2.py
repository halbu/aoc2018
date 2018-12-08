dlist = ([str.rstrip(l) for l in open('./aoc2018-day8.data', "r")])[0].split(' ')
metadata = []
index = 0

def main():
  print('Solution: ' + str(process_node()))

def process_node():
  global index

  num_children, num_metadatas = int(dlist[index]), int(dlist[index + 1])
  index += 2

  child_values = [process_node() for k in range(0, num_children)]

  value = 0
  for j in range(0, num_metadatas):
    if len(child_values) == 0:
        value += int(dlist[index])
    elif int(dlist[index]) > 0 and int(dlist[index]) <= len(child_values):
        value += child_values[int(dlist[index]) - 1]
    index += 1

  return value

if __name__ == '__main__':
  main()