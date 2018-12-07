done, progressing, workers = [], [], []
deps = {}
base_step_time = 60
total_workers = 5
time = 0

for i in range(0, total_workers, 1):
  workers.append({'task': '.', 'time': 999})

def main():
  for s in list([str.rstrip(l) for l in open('./aoc2018-day7.data', "r")]):
    tokens = s.split(' ')
    if tokens[7] not in deps:
      deps[tokens[7]] = [tokens[1]]
    else:
      deps[tokens[7]].append(tokens[1])
    if tokens[1] not in deps:
      deps[tokens[1]] = []

  while(len(deps.keys()) > 0):
    while get_idle_worker() and get_next_step():
      commence_step(get_next_step())
    advance_time()

  print('Solution: ' + str(time))

def advance_time():
  global time
  for w in workers:
    if w['task'] != '.':
      w['time'] -= 1
      if w['time'] <= 0:
        complete_step(w['task'])
        w['task'] = '.'
  time += 1

def get_next_step():
  for o in sorted([k for k in deps.keys() if not deps[k] and k not in progressing]):
    return o

def get_idle_worker():
  for k in [k for k in workers if k['task'] == '.']:
    return k

def commence_step(c):
  w = get_idle_worker()
  w['task'] = c
  w['time'] = base_step_time + ord(c) - 64
  progressing.append(c)

def complete_step(c):
  progressing.remove(c)
  done.append(c)
  for k in deps.keys():
    if c in deps[k]:
      deps[k].remove(c)
  deps.pop(c, None)

if __name__ == '__main__':
  main()