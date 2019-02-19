data = [l.strip() for l in open('./aoc2018-day19.data', "r") if l != "\n"]
r = [0, 0, 0, 0, 0, 0]

def main():

#ip 2			        set r[2] as the instruction register
0	addi 2 16 2	    add 16 to r[2]. post operation 1 is always added to r[2] so effectively JMP 17

1	seti 1 4 3      r[3] = 1
2	seti 1 5 1      r[1] = 1
3	mulr 3 1 5
4	eqrr 5 4 5
5	addr 5 2 2
6	addi 2 1 2
7	addr 3 0 0
8	addi 1 1 1
9	gtrr 1 4 5
10	addr 2 5 2
11	seti 2 9 2
12	addi 3 1 3
13	gtrr 3 4 5
14	addr 5 2 2
15	seti 1 6 2
16	mulr 2 2 2

17	addi 4 2 4	  r[4] += 2
18	mulr 4 4 4	  r[4] *= r[4]
19	mulr 2 4 4    r[4] = r[4] * r[2]
20	muli 4 11 4   r[4] *= 11
21	addi 5 7 5    r[5] += 7
22	mulr 5 2 5    r[5] *= r[2]
23	addi 5 4 5    r[5] += 4
24	addr 4 5 4    r[4] = r[4] + r[5]
25	addr 2 0 2    r[2] = r[2] + r[0]  effectively JMP (26 + r[0])

26	seti 0 1 2    r[2] = 0 effectively JMP 1
27	setr 2 1 5
28	mulr 5 2 5
29	addr 2 5 5
30	mulr 2 5 5
31	muli 5 14 5
32	mulr 5 2 5
33	addr 4 5 4
34	seti 0 6 0
35	seti 0 6 2

# def do_op(opcode, input_a, input_b, output):
  # if opcode == 'addr':
  #   r[output] = r[input_a] + r[input_b]
  # elif opcode == 'addi':
  #   r[output] = r[input_a] + input_b
  # elif opcode == 'mulr':
  #   r[output] = r[input_a] * r[input_b]
  # elif opcode == 'muli':
  #   r[output] = r[input_a] * input_b
  # elif opcode == 'banr':
  #   r[output] = r[input_a] & r[input_b]
  # elif opcode == 'bani':
  #   r[output] = r[input_a] & input_b
  # elif opcode == 'borr':
  #   r[output] = r[input_a] | r[input_b]
  # elif opcode == 'bori':
  #   r[output] = r[input_a] | input_b
  # elif opcode == 'setr':
  #   r[output] = r[input_a]
  # elif opcode == 'seti':
  #   r[output] = input_a
  # elif opcode == 'gtir':
  #   r[output] = 1 if input_a > r[input_b] else 0
  # elif opcode == 'gtri':
  #   r[output] = 1 if r[input_a] > input_b else 0
  # elif opcode == 'gtrr':
  #   r[output] = 1 if r[input_a] > r[input_b] else 0
  # elif opcode == 'eqir':
  #   r[output] = 1 if input_a == r[input_b] else 0
  # elif opcode == 'eqri':
  #   r[output] = 1 if r[input_a] == input_b else 0
  # elif opcode == 'eqrr':
  #   r[output] = 1 if r[input_a] == r[input_b] else 0

if __name__ == '__main__':
  main()