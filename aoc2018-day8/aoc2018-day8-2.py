dlist = [int(k) for k in ([l for l in open('./aoc2018-day8.data', "r")])[0].split(' ')]
index = 0

def process_node():
  global index
  num_children, num_metadatas = dlist[index], dlist[index + 1]
  index += 2
  child_values = [process_node() for k in range(0, num_children)]

  value = 0
  for j in range(0, num_metadatas):
    if len(child_values) == 0:
        value += dlist[index]
    elif dlist[index] > 0 and dlist[index] <= len(child_values):
        value += child_values[dlist[index] - 1]
    index += 1

  return value

print('Solution: ' + str(process_node()))