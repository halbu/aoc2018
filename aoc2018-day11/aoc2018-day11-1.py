gsn = int([str.rstrip(l) for l in open('./aoc2018-day11.data', "r")][0])
grid = [[0 for _ in range(301)] for _ in range(301)]

def main():
  print('Tests:')
  test(3, 5, 8, 4)
  test(122, 79, 57, -5)
  test(217, 196, 39, 0)
  test(101, 153, 71, 4)

  print('Solution:')
  solve(gsn)

def test(x, y, g, t):
  for i in range(1, 301):
    for j in range(1, 301):
      grid[i][j] = calc_power(i, j, g)
  
  print('Power level at ' + str(x) + ', ' + str(y) + ' with grid serial ' + str(g) + ' is ' + str(grid[x][y]) + ' (expected ' + str(t) + ')')

def solve(g):
  for i in range(1, 301):
    for j in range(1, 301):
      grid[i][j] = calc_power(i, j, g)
  
  mp, mpx, mpy = -1, -1, -1
  for i in range(1, 299):
    for j in range(1, 299):
      p = 0
      for k in range(3):
        for l in range(3):
          p += grid[i+k][j+l]
      if p > mp:
        mp = p
        mpx = i
        mpy = j
  
  print('Max power value found was ' + str(mp) + ' at co-ordinate ' + str(mpx) + ', ' + str(mpy))

def calc_power(x, y, g):
  pwr = (x + 10) * y + g
  pwr = pwr * (x + 10)
  return (int(str(pwr)[len(str(pwr))-3]) if len(str(pwr)) > 2 else 0) - 5

if __name__ == '__main__':
  main()