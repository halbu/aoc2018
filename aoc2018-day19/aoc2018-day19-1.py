# data = [l.strip() for l in open('./test.data', "r") if l != "\n"]
data = [l.strip() for l in open('./aoc2018-day19.data', "r") if l != "\n"]
r = [0, 0, 0, 0, 0, 0]
instructions = []
instruction_pointer = 0
instruction_register = 2

def main():
  global instructions
  global instruction_pointer

  for l in data:
    if l[0] == '#':
      instruction_register = int(l.split(' ')[1])
    else:
      tokens = l.split(' ')
      instructions.append([tokens[0], int(tokens[1]), int(tokens[2]), int(tokens[3])])

  while (instruction_pointer < len(instructions)):
    next_ins = instructions[instruction_pointer]

    # write value of instruction pointer to the bound register...
    r[instruction_register] = instruction_pointer

    # then do the op
    do_op(next_ins[0], next_ins[1], next_ins[2], next_ins[3])

    # then read the value back into the instruction pointer
    instruction_pointer = r[instruction_register]

    # then increment the value of the instruction pointer by one
    instruction_pointer += 1

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