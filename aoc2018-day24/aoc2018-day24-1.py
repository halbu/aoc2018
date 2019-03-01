import math
data = [l.strip() for l in open('./aoc2018-day24.data', "r") if l != "\n"]
immune_group, infection_group = [], []

def main():
  global immune_group, infection_group
  
  # setup
  side = 'immune'
  for l in data:
    if l[:9] == 'Infection':
      side = 'infect'
    elif l[0].isdigit():
      if side == 'immune':
        immune_group.append(parse_group_from_line(l))
      else:
        infection_group.append(parse_group_from_line(l))

  # run the simulation
  while len(immune_group) > 0 and len(infection_group) > 0:
    get_targets()
    attack()
    immune_group = [i for i in immune_group if i['units'] > 0]
    infection_group = [i for i in infection_group if i['units'] > 0]
    untag_all()

  print(sum([i['units'] for i in infection_group]))

def attack():
  global immune_group, infection_group
  combined_group = immune_group + infection_group
  combined_group.sort(key=lambda x: x['initiative'], reverse=True)

  for i in combined_group:
    if i['target'] == None:
      continue

    total_attack = i['attack_power'] * i['units']
    if i['attack_type'] in i['target']['weakness']:
      total_attack *= 2
    if i['target']['immunity'] and i['attack_type'] in i['target']['immunity']:
      total_attack = 0

    kills = math.floor(total_attack / i['target']['hp'])
    i['target']['units'] -= kills

def untag_all():
  global immune_group, infection_group
  
  # untag and untarget everything
  for i in immune_group:
    i['targeted'] = False
    i['target'] = None
  for i in infection_group:
    i['targeted'] = False
    i['target'] = None

def get_targets():
  untag_all()

  # get immune group targets
  immune_group.sort(key=lambda x: (x['units'] * x['attack_power'], x['initiative']), reverse=True)

  for i in immune_group:
    i['target'] = None
    potential_targets = [g for g in infection_group if not g['targeted']]
    mpd = 0
    for p in potential_targets:
      dam = i['units'] * i['attack_power']
      if i['attack_type'] in p['weakness']:
        dam *= 2
      if i['attack_type'] in p['immunity']:
        dam = 0
      mpd = max(dam, mpd)
    
    new_potential_targets = []

    for p in potential_targets:
      dam = i['units'] * i['attack_power']
      if i['attack_type'] in p['weakness']:
        dam *= 2
      if i['attack_type'] in p['immunity']:
        dam = 0
      if dam == mpd:
        new_potential_targets.append(p)

    new_potential_targets.sort(key=lambda x: (x['units'] * x['attack_power'], x['initiative']), reverse=True)

    if mpd > 0:
      i['target'] = new_potential_targets[0]
      i['target']['targeted'] = True

  # get infection group targets
  infection_group.sort(key=lambda x: (x['units'] * x['attack_power'], x['initiative']), reverse=True)

  for i in infection_group:
    i['target'] = None
    potential_targets = [g for g in immune_group if not g['targeted']]
    mpd = 0
    for p in potential_targets:
      dam = i['units'] * i['attack_power']
      if i['attack_type'] in p['weakness']:
        dam *= 2
      mpd = max(dam, mpd)
    
    new_potential_targets = []

    for p in potential_targets:
      dam = i['units'] * i['attack_power']
      if i['attack_type'] in p['weakness']:
        dam *= 2
      if dam == mpd:
        new_potential_targets.append(p)

    new_potential_targets.sort(key=lambda x: (x['units'] * x['attack_power'], x['initiative']), reverse=True)

    if mpd > 0:
      i['target'] = new_potential_targets[0]
      i['target']['targeted'] = True

def parse_group_from_line(l):
  general_data = l.split(' with an attack that does ')[0]
  attack_data = l.split(' with an attack that does ')[1]
  
  units = general_data.split(' ')[0]
  hp = general_data.split(' ')[4]
  weakness, immunity = [], []

  if 'weak' in general_data:
    weakness = general_data.split('weak to ')[1].split(';')[0].split(')')[0].split(', ')
  if 'immune' in general_data:
    immunity = general_data.split('immune to ')[1].split(';')[0].split(')')[0].split(', ')

  attack_power = attack_data.split(' ')[0]
  attack_type = attack_data.split(' ')[1]
  initiative = attack_data.split(' ')[5]
    
  # I should probably make this an actual class but I can't be bothered
  return {
    'units': int(units),
    'hp': int(hp),
    'weakness': weakness,
    'immunity': immunity,
    'attack_power': int(attack_power),
    'attack_type': attack_type,
    'initiative': int(initiative),
    'targeted': False,
    'acted': False,
    'target': None
  }
  
if __name__ == '__main__':
  main()