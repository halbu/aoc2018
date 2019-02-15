data = [l.strip() for l in open('./aoc2018-day19.data', "r") if l != "\n"]
r = [0, 0, 0, 0, 0, 0]

def main():
  instructions = []
  instruction_pointer, instruction_register = 0, 0

  for l in data:
    if l[0] == '#':
      instruction_register = int(l.split(' ')[1])
    else:
      tokens = l.split(' ')
      instructions.append([tokens[0], int(tokens[1]), int(tokens[2]), int(tokens[3])])

  while (instruction_pointer < len(instructions)):
    next_ins = instructions[instruction_pointer]              # get the instruction being pointed at
    r[instruction_register] = instruction_pointer             # write value of pointer to bound register
    do_op(next_ins[0], next_ins[1], next_ins[2], next_ins[3]) # perform the operation
    instruction_pointer = r[instruction_register]             # read new value back into the pointer
    instruction_pointer += 1                                  # increment value of pointer by 1

  print('Solution: ' + str(r[0]))

def do_op(opcode, input_a, input_b, output):
  if opcode == 'addr':
    r[output] = r[input_a] + r[input_b]
  elif opcode == 'addi':
    r[output] = r[input_a] + input_b
  elif opcode == 'mulr':
    r[output] = r[input_a] * r[input_b]
  elif opcode == 'muli':
    r[output] = r[input_a] * input_b
  elif opcode == 'banr':
    r[output] = r[input_a] & r[input_b]
  elif opcode == 'bani':
    r[output] = r[input_a] & input_b
  elif opcode == 'borr':
    r[output] = r[input_a] | r[input_b]
  elif opcode == 'bori':
    r[output] = r[input_a] | input_b
  elif opcode == 'setr':
    r[output] = r[input_a]
  elif opcode == 'seti':
    r[output] = input_a
  elif opcode == 'gtir':
    r[output] = 1 if input_a > r[input_b] else 0
  elif opcode == 'gtri':
    r[output] = 1 if r[input_a] > input_b else 0
  elif opcode == 'gtrr':
    r[output] = 1 if r[input_a] > r[input_b] else 0
  elif opcode == 'eqir':
    r[output] = 1 if input_a == r[input_b] else 0
  elif opcode == 'eqri':
    r[output] = 1 if r[input_a] == input_b else 0
  elif opcode == 'eqrr':
    r[output] = 1 if r[input_a] == r[input_b] else 0

if __name__ == '__main__':
  main()