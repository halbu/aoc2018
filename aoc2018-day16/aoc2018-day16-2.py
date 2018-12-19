data = [l.strip() for l in open('./aoc2018-day16.data', "r") if l != "\n"]
i = 0
M, O = {}, {}

def next_line():
  global i
  i += 1
  return data[i - 1]

def is_next_line():
  return True if i < len(data) else False
    
def main():
  build_opcode_map()
  for o in M.keys():
    print(o)
    get_opcode_possibilities(M[o])

def build_opcode_map():
  global M
  while(is_next_line()):
    add_to_map()

def add_to_map():
  registers_pre = [int(i) for i in next_line().split(': ')[1][1:-1].split(', ')]
  opdata = [int(i) for i in next_line().split()]
  registers_post = [int(i) for i in next_line().split(':  ')[1][1:-1].split(', ')]
  opnum = opdata[0]

  if opnum not in M:
    M[opnum] = []

  M[opnum].append([registers_pre, opdata, registers_post])

def get_opcode_possibilities(o):
  sets_of_possibilities = []

  for opset in o:
    print(opset)
    pre = opset[0]
    op = opset[1]
    post = opset[2]
    possibilities = []

    for opcode in ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']:
      if do_op(opcode, op, pre.copy()) == post:
        possibilities.append(opcode)
        
    sets_of_possibilities.append(possibilities)
  
  print(sets_of_possibilities)

def do_op(opcode, op, r):
  if opcode == 'addr':
    r[op[3]] = r[op[1]] + r[op[2]]
  elif opcode == 'addi':
    r[op[3]] = r[op[1]] + op[2]
  elif opcode == 'mulr':
    r[op[3]] = r[op[1]] * r[op[2]]
  elif opcode == 'muli':
    r[op[3]] = r[op[1]] * op[2]
  elif opcode == 'banr':
    r[op[3]] = r[op[1]] & r[op[2]]
  elif opcode == 'bani':
    r[op[3]] = r[op[1]] & op[2]
  elif opcode == 'borr':
    r[op[3]] = r[op[1]] | r[op[2]]
  elif opcode == 'bori':
    r[op[3]] = r[op[1]] | op[2]
  elif opcode == 'setr':
    r[op[3]] = r[op[1]]
  elif opcode == 'seti':
    r[op[3]] = op[1]
  elif opcode == 'gtir':
    r[op[3]] = 1 if op[1] > r[op[2]] else 0
  elif opcode == 'gtri':
    r[op[3]] = 1 if r[op[1]] > op[2] else 0
  elif opcode == 'gtrr':
    r[op[3]] = 1 if r[op[1]] > r[op[2]] else 0
  elif opcode == 'eqir':
    r[op[3]] = 1 if op[1] == r[op[2]] else 0
  elif opcode == 'eqri':
    r[op[3]] = 1 if r[op[1]] == op[2] else 0
  elif opcode == 'eqrr':
    r[op[3]] = 1 if r[op[1]] == r[op[2]] else 0

  return r

if __name__ == '__main__':
  main()