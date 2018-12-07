done = []
deps = {}

def main():
  steps = list([str.rstrip(l) for l in open('./aoc2018-day7.data', "r")])
  
  for s in steps:
    tokens = s.split(' ')
    if tokens[7] not in deps:
      deps[tokens[7]] = [tokens[1]]
    else:
      deps[tokens[7]].append(tokens[1])
    if tokens[1] not in deps:
      deps[tokens[1]] = []

  while(len(deps.keys()) > 0):
    do_step((get_next_step()))

  print(''.join(done))

def get_next_step():
  ordered = sorted([k for k in deps.keys()])
  for o in ordered:
    if not deps[o]:
      return o

def do_step(c):
  done.append(c)
  for k in deps.keys():
    if c in deps[k]:
      deps[k].remove(c)
  deps.pop(c, None)

if __name__ == '__main__':
  main()