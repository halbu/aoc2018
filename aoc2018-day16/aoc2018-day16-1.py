data = [l.strip() for l in open('./aoc2018-day16.data', "r") if l != "\n"]
behave_like_three_or_more, i = 0, 0

def next_line():
  global i
  i += 1
  return data[i - 1]

def is_next_line():
  return True if i < len(data) else False
    
def main():
  while(is_next_line()):
    get_matches()
  
  print('Solution:', behave_like_three_or_more)

def get_matches():
  global behave_like_three_or_more
  registers_pre = [int(i) for i in next_line().split(': ')[1][1:-1].split(', ')]
  opdata = [int(i) for i in next_line().split()]
  registers_post = [int(i) for i in next_line().split(':  ')[1][1:-1].split(', ')]

  opcode_matches = 0
  for op in ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']:
    if registers_post == (do_op(op, opdata, registers_pre.copy())):
      opcode_matches += 1

  if opcode_matches >= 3:
    behave_like_three_or_more += 1   

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