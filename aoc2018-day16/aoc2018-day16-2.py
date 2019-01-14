data = [l.strip() for l in open('./aoc2018-day16.data', "r") if l != "\n"]
program_data = [l.strip() for l in open('./aoc2018-day16-2.data', "r") if l != "\n"]
i, program_instruction_index = 0, 0
M = {}
allcodes = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

def next_line():
  global i
  i += 1
  return data[i - 1]

def next_program_instruction():
  global program_instruction_index
  program_instruction_index += 1
  return program_data[program_instruction_index - 1]

def is_next_line():
  return True if i < len(data) else False

def is_next_program_instruction():
  return True if program_instruction_index < len(program_data) else False
    
def main():
  build_opcode_map()
  poss_ops, known_ops = [], [''] * 16

  # Get all possibilities
  for i, o in enumerate(M.keys()):
    poss_ops.append(get_opcode_possibilities(M[o]))

  # Match each opcode number to one specific opcode
  found_op = True
  while found_op:
    found_this_iteration = False
    for i, o in enumerate(poss_ops):
      if len(o) == 1:
        found_this_iteration = True
        known_ops[i] = o[0]
        for j in range(16):
          if known_ops[i] in poss_ops[j]:
            poss_ops[j].remove(known_ops[i])
    found_op = found_this_iteration
  
  registers = [0, 0, 0, 0]

  while is_next_program_instruction():
    instruction = next_program_instruction()
    instruction_arr = [int(e) for e in instruction.split(' ')]
    registers = do_op(known_ops[instruction_arr[0]], instruction_arr, registers)

  print('Solution:', registers[0])


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
    pre = opset[0]
    op = opset[1]
    post = opset[2]
    possibilities = []

    for opcode in allcodes:
      if do_op(opcode, op, pre.copy()) == post:
        possibilities.append(opcode)
        
    sets_of_possibilities.append(possibilities)

  return sets_of_possibilities[0]

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