import math
data = [l.strip() for l in open('./aoc2018-day24.data', "r") if l != "\n"]
immunes, infections = [], []

def main():
  global immunes, infections
  
  # setup
  side = 'immune'
  for l in data:
    if l[:9] == 'Infection':
      side = 'infect'
    elif l[0].isdigit():
      if side == 'immune':
        immunes.append(parse_group_from_line(l))
      else:
        infections.append(parse_group_from_line(l))

  # run the simulation until one side is eliminated
  while len(immunes) > 0 and len(infections) > 0:
    get_targets()
    attack()
    immunes = [i for i in immunes if i.units > 0]
    infections = [i for i in infections if i.units > 0]

  print('Solution:', sum(i.units for i in immunes + infections))

def attack():
  combined = immunes + infections
  combined.sort(key=lambda x: x.init, reverse=True)

  for c in combined:
    if c.target:
      c.deal_damage()

def get_targets():
  for i in immunes + infections:
    i.target = None
    i.targeted = False

  immunes.sort(key=lambda x: x.effpow(), reverse=True)
  infections.sort(key=lambda x: x.effpow(), reverse=True)

  for x in [[immunes, infections], [infections, immunes]]:
    offense, defense = x[0], x[1]

    for i in offense:
      # get ALL possible targets
      targets = [j for j in defense if not j.targeted]

      # if there exist no viable targets then do nothing
      if len(targets) == 0:
        continue

      # filter for only those targets to whom we would deal the most possible total damage
      max_dmg = max(t.potential_damage(i.effpow(), i.atktype) for t in targets)
      
      # if we can deal no damage then do nothing
      if (max_dmg == 0):
        continue

      targets = [t for t in targets if t.potential_damage(i.effpow(), i.atktype) == max_dmg]
      
      # if we need to break ties, filter by the greatest opposing effective power
      if len(targets) > 1:
        max_opp_effpow = max(t.effpow() for t in targets)
        targets = [t for t in targets if t.effpow() == max_opp_effpow]

      # if we STILL need to break ties, take the target with the highest initiative score
      if len(targets) > 1:
        targets = [t for t in targets if t.init == max(t.init for t in targets)]

      # tag the opposing group as having been targeted this round and store it as the target
      final_target = targets[0]
      final_target.targeted = True
      i.target = final_target

def parse_group_from_line(l):
  general_data = l.split(' with an attack that does ')[0]
  attack_data = l.split(' with an attack that does ')[1]
  
  units = int(general_data.split(' ')[0])
  hp = int(general_data.split(' ')[4])

  weakness, immunity = [], []
  if 'weak' in general_data:
    weakness = general_data.split('weak to ')[1].split(';')[0].split(')')[0].split(', ')
  if 'immune' in general_data:
    immunity = general_data.split('immune to ')[1].split(';')[0].split(')')[0].split(', ')

  attack_power = int(attack_data.split(' ')[0])
  attack_type = attack_data.split(' ')[1]
  initiative = int(attack_data.split(' ')[5])

  return Group(units, hp, weakness, immunity, attack_power, attack_type, initiative)
  
class Group:
  def __init__(self, units, hp, weak, immune, atkpow, atktype, init):
    self.units = units
    self.hp = hp
    self.weak = weak
    self.immune = immune
    self.atkpow = atkpow
    self.atktype = atktype
    self.init = init
    self.targeted = False
    self.target = None

  def effpow(self):
    return self.units * self.atkpow

  def potential_damage(self, enemy_effpow, enemy_atktype):
    if enemy_atktype in self.weak:
      return enemy_effpow * 2
    elif enemy_atktype in self.immune:
      return 0
    else:
      return enemy_effpow

  def deal_damage(self):
    dmg = self.target.potential_damage(self.effpow(), self.atktype)
    kills = min(self.target.units, math.floor(dmg/self.target.hp))
    self.target.units = max(0, self.target.units - kills)

if __name__ == '__main__':
  main()