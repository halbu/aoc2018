dlist = [int(k) for k in ([l for l in open('./aoc2018-day8.data', "r")])[0].split(' ')]
metadata = []
index = 0

def process_node():
  global index
  num_children, num_metadatas = dlist[index], dlist[index + 1]
  index += 2

  for i in range(0, num_children):
    process_node()
  
  for j in range(0, num_metadatas):
    metadata.append(dlist[index])
    index += 1
    
process_node()
print('Solution: ' + str(sum(metadata)))