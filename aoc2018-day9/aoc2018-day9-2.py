data = ([l for l in open('./aoc2018-day9.data', "r")])[0].split(' ')

np, lmpv = int(data[0]), int(data[6]) * 100 # no. players, last marble placed value
players = [0] * np
ci, cp = 0, 0 # current index, current player
circle = []
cnode = None # ref to current circular linked list node

class CLLNode:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

  def get_prev(self):
    return self.prev

  def get_next(self):
    return self.next

def insert_after_current(i):
  global cnode
  n = CLLNode(i)
  n.prev = cnode
  n.next = cnode.next
  cnode.next.prev = n
  cnode.next = n
  cnode = n

def delete():
  global cnode
  cnode.prev.next = cnode.next
  cnode.next.prev = cnode.prev
  cnode = cnode.next

def main():
  global cp
  global cnode

  first = CLLNode(0)
  first.next, first.prev, cnode = first, first, first

  insert_after_current(1)

  for i in range(2, lmpv):
    if i % 23 == 0:
      players[cp] += i
      for n in range(7):
        cnode = cnode.get_prev()
      players[cp] += cnode.data
      delete()
    else:
      cnode = cnode.get_next()
      insert_after_current(i)
    cp = cp + 1 if cp + 1 < len(players) else 0

  print('Solution: ' + str(max(players)))

if __name__ == '__main__':
  main()