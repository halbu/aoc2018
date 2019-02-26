# main loop seems to be 3 4 5 6, 8 9 10 11

# Contents of registers every time instruction 3 gets hit:
#   [0, 1, 2, 1, 10551394, 10550400]
#   [0, 2, 2, 1, 10551394, 0]
#   [0, 3, 2, 1, 10551394, 0]
#   [0, 4, 2, 1, 10551394, 0]
#   [0, 5, 2, 1, 10551394, 0]
#   [0, 6, 2, 1, 10551394, 0]
#   [0, 7, 2, 1, 10551394, 0]
#   [0, 8, 2, 1, 10551394, 0]
#   [0, 9, 2, 1, 10551394, 0]
#   [0, 10, 2, 1, 10551394, 0]
#   [0, 11, 2, 1, 10551394, 0]
#   [0, 12, 2, 1, 10551394, 0]
#   [0, 13, 2, 1, 10551394, 0]
#   [0, 14, 2, 1, 10551394, 0]
#   [0, 15, 2, 1, 10551394, 0]
#   [0, 16, 2, 1, 10551394, 0]
#   [0, 17, 2, 1, 10551394, 0]
#   [0, 18, 2, 1, 10551394, 0]
#   [0, 19, 2, 1, 10551394, 0]
#   [0, 20, 2, 1, 10551394, 0]
#   [0, 21, 2, 1, 10551394, 0]
#   [0, 22, 2, 1, 10551394, 0]
# and so on

# pre and post states every time instruction 7 (addition of the value of register 3 to register 0) is hit:
#   PRE:  [0, 10551394, 6, 1, 10551394, 1]
#   POST: [1, 10551394, 7, 1, 10551394, 1]
#   PRE:  
#   PRE:  [1, 5275697, 6, 2, 10551394, 1]
#   POST: [3, 5275697, 7, 2, 10551394, 1]
#   PRE:  
#   PRE:  [3, 1507342, 6, 7, 10551394, 1]
#   POST: [10, 1507342, 7, 7, 10551394, 1]
#   PRE:  
#   PRE:  [10, 753671, 6, 14, 10551394, 1]
#   POST: [24, 753671, 7, 14, 10551394, 1]
# as far as I can tell every time we calculate a factor of 10551394 register 0 is being incremented by the value of
# that factor, so the solution should be the sum of all factors of 10551394, namely 18200448...

#ip 2			        set r[2] as the instruction register
0   addi 2 16 2	  r[2] += 16  # post operation 1 is always added to r[2] so effectively JMP 17

1   seti 1 4 3    r[3] = 1
2   seti 1 5 1    r[1] = 1

3   mulr 3 1 5    r[5] = r[3] * r[1]
4   eqrr 5 4 5    r[5] = (r[4] == r[5]) ? 1 : 0
5   addr 5 2 2    JMP to + r[5]                     JMP to either 6 or 7
6   addi 2 1 2    r[2] += 1 effectively JMP 8       # so, JMP 8 if r1 * r3 == r4

7   addr 3 0 0    r[0] += r[3] # i suspect we're trying to sum the factors of the big constant number in register 4? [later edit: i was right!!]

8   addi 1 1 1    r[1]++
9   gtrr 1 4 5    r[5] = (r[1] > r[4]) ? 1 : 0
10	addr 2 5 2    r[2] += r[5] # this and the previous line form conditional jump? if r[1] > r[4] then r[5] = 1 and this is JMP 12, else...
11	seti 2 9 2    r[2] = 2 (effectively JMP 3)

12	addi 3 1 3    r[3]++

13	gtrr 3 4 5    r[5] = (r[3] > r[4]) ? 1 : 0
14	addr 5 2 2    conditional JMP 16 (if r[3] > r[4], JMP 16 else continue)
15	seti 1 6 2    r[2] = 1 (effectively JMP 2)
16	mulr 2 2 2    r[2] = r[2] * r[2] (??) JMP 33...?

# 17 onward (excepting 26) appears to just get executed once at startup
17	addi 4 2 4    r[4] += 2                                           # register 4 = 2
18	mulr 4 4 4    r[4] *= r[4]                                        # 2^2 = 4
19	mulr 2 4 4    r[4] = r[4] * r[2]                                  # 4 * 19 = 76
20	muli 4 11 4   r[4] *= 11                                          # 76 * 11 = 836
21	addi 5 7 5    r[5] += 7                                           # register 5 = 7
22	mulr 5 2 5    r[5] *= r[2]                                        # 7 * 22 = 154
23	addi 5 4 5    r[5] += 4                                           # 154 + 4 = 158
24	addr 4 5 4    r[4] = r[4] + r[5]                                  # register 4 (836) += register 5 (158) = 994
25	addr 2 0 2    r[2] = r[2] + r[0]  effectively JMP (26 + r[0])     # r[0] == 1 initially so this (on first run at least) is JMP 27

26	seti 0 1 2    r[2] = 0 effectively JMP 1

# AFAIK this is further setup?
27	setr 2 1 5    r[5] = r[2]                                         # r[2] = 27
28	mulr 5 2 5    r[5] *= r[2]                                        # 27 * 28 = 756
29	addr 2 5 5    r[5] += r[2]                                        # 756 + 29 = 785
30	mulr 2 5 5    r[5] *= r[2]                                        # 785 * 30 = 23550
31	muli 5 14 5   r[5] *= 14                                          # 23550 * 14 = 329700
32	mulr 5 2 5    r[5] *= r[2]                                        # 329700 * 32 = 10550400
33	addr 4 5 4    r[4] += r[5]                                        # add 10550400 to register 4 (in practice r[4] = 10551394)
34	seti 0 6 0    r[0] = 0                                            # clear register 0
35	seti 0 6 2    r[2] = 0                                            # JMP 1

# def do_op(opcode, input_a, input_b, output):
  # if opcode == 'addr':    r[output] = r[input_a] + r[input_b]
  # elif opcode == 'addi':  r[output] = r[input_a] + input_b
  # elif opcode == 'mulr':  r[output] = r[input_a] * r[input_b]
  # elif opcode == 'muli':  r[output] = r[input_a] * input_b
  # elif opcode == 'banr':  r[output] = r[input_a] & r[input_b]
  # elif opcode == 'bani':  r[output] = r[input_a] & input_b
  # elif opcode == 'borr':  r[output] = r[input_a] | r[input_b]
  # elif opcode == 'bori':  r[output] = r[input_a] | input_b
  # elif opcode == 'setr':  r[output] = r[input_a]
  # elif opcode == 'seti':  r[output] = input_a
  # elif opcode == 'gtir':  r[output] = 1 if input_a > r[input_b] else 0
  # elif opcode == 'gtri':  r[output] = 1 if r[input_a] > input_b else 0
  # elif opcode == 'gtrr':  r[output] = 1 if r[input_a] > r[input_b] else 0
  # elif opcode == 'eqir':  r[output] = 1 if input_a == r[input_b] else 0
  # elif opcode == 'eqri':  r[output] = 1 if r[input_a] == input_b else 0
  # elif opcode == 'eqrr':  r[output] = 1 if r[input_a] == r[input_b] else 0