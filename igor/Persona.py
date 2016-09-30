# Persona stats

from .Enum import *

class Persona:
  def __init__(self, name):
    global PersonaList
    o = PersonaList[name]
    if (o == None):
      raise Exception('No such persona: ' + name + '!')

    # copy stats from object
    self.__dict__.update(o.__dict__)


# get info string
def getPersonaInfo(owner, persona, isShadow):
  s = '[Lv ' + str(persona.level)
  if (isShadow):
    s += ', ATK ' + str(persona.atk) + \
      ', HP ' + str(persona.maxHP)
  for key, val in persona.affinity.items():
    s += ', ' + key.name + ' ' + val.name
  s += ']'

  if (len(persona.skills) > 0):
    s += ' (Skills '
    for i in range(0, len(persona.skills)):
      s += str(i + 1) + ':'
      sk = persona.skills[i]
      s += sk.getNameAndCost(owner)
      if (i < len(persona.skills) - 1):
        s += ', '
    s += ')'

  return s

# persona stats

class PersonaStats:
  def __init__(self, **fields):
    self.__dict__.update(fields)

    # get id from name
    self.id = self.name.replace(" ", "")


# persona skill

class PersonaSkill:
  def __init__(self, **fields):
    self.__dict__.update(fields)

# get skill name and cost
  def getNameAndCost(self, owner):
    return self.name + ' [' + str(self.getCost(owner)) + ' ' + self.costType + ']'

# get skill cost
  def getCost(self, player):
    c = self.cost
    if (self.costType == 'HP'):
      c = player.maxHP * c / 100.0
      c = int(c)
    return c


######################################

SkillList = dict()

# PHYSICAL SKILLS
SkillList['Bash'] = PersonaSkill(
  name = 'Bash',
  type = SkillType.Attack,
  cost = 6,
  costType = 'HP',
  damageType = DamageType.Phys,
  power = 120,
  )
SkillList['Cleave'] = PersonaSkill(
  name = 'Cleave',
  type = SkillType.Attack,
  cost = 5,
  costType = 'HP',
  damageType = DamageType.Phys,
  power = 130,
  )


# ELEMENTAL
SkillList['Agi'] = PersonaSkill(
  name = 'Agi',
  type = SkillType.Attack,
  cost = 4,
  costType = 'SP',
  damageType = DamageType.Fire,
  power = 80,
  )
SkillList['Zio'] = PersonaSkill(
  name = 'Zio',
  type = SkillType.Attack,
  cost = 4,
  costType = 'SP',
  damageType = DamageType.Elec,
  power = 80,
  )
SkillList['Bufu'] = PersonaSkill(
  name = 'Bufu',
  type = SkillType.Attack,
  cost = 4,
  costType = 'SP',
  damageType = DamageType.Ice,
  power = 80,
  )
SkillList['Garu'] = PersonaSkill(
  name = 'Garu',
  type = SkillType.Attack,
  cost = 4,
  costType = 'SP',
  damageType = DamageType.Wind,
  power = 80,
  )

# HEAL SKILLS
SkillList['Dia'] = PersonaSkill(
  name = 'Dia',
  type = SkillType.Heal,
  cost = 3,
  costType = 'SP',
  value = 50,
  )

# SUPPORT SKILLS
SkillList['Rakunda'] = PersonaSkill(
  name = 'Rakunda',
  type = SkillType.SupportEnemy,
  cost = 12,
  costType = 'SP',
  turns = 3,
  )
# all damage affinities -1
def applyRakunda(target):
  newaff = {}

  for t in DamageType:
    aff = DamageAffinity.Normal
    if (t in target.affinity):
      aff = target.affinity[t]

    aff -= 1
    if aff < 0:
      aff = 0

    if (aff != DamageAffinity.Normal):
      newaff[t] = DamageAffinity(aff)
  target.affinity = newaff

SkillList['Rakunda'].apply = applyRakunda


######################################

PersonaList = dict()

# Fool Arcana
PersonaList['Izanagi'] = PersonaStats(
  name = 'Izanagi',
  arcana = Arcana.Fool,
  level = 1,
  skills = [
    SkillList['Zio'],
    SkillList['Cleave'],
    SkillList['Rakunda'], # LV3
#Rakukaja  12 SP Increases 1 ally's Defense for 3 turns. Innate
#Tarukaja  12 SP Increases 1 ally's Attack for 3 turns.  5
    ],
  affinity = {
    DamageType.Wind: DamageAffinity.Weak,
    DamageType.Elec: DamageAffinity.Strong,
    }
  )

# Magician Arcana
PersonaList['Pixie'] = PersonaStats(
  name = 'Pixie',
  arcana = Arcana.Magician,
  level = 2,
  skills = [
    SkillList['Dia'],
    SkillList['Zio'], # LV3
#Patra   3 SP    Dispels Confusion, Fear, and Rage (1 ally). Innate
#Zio 4 SP    Deals light Elec damage to 1 foe.   3
#Me Patra    6 SP    Dispels Confusion, Fear, and Rage (party).  4
#Trafuri 24 SP   Enables escape from most battles.
#(100% chance to escape normal battles)  8
    ],
  affinity = {
    DamageType.Wind: DamageAffinity.Strong,
    DamageType.Fire: DamageAffinity.Weak,
    }
  )

# Chariot Arcana
PersonaList['Slime'] = PersonaStats(
  name = 'Slime',
  arcana = Arcana.Chariot,
  level = 2,
  skills = [
    SkillList['Bash'],
#    SkillList['Evil Touch'],
#Tarunda 12 SP Decreases 1 foe's Attack for 3 turns. 3
#Red Wall 18 SP Add Fire resistance to 1 ally (for 3 turns).  4
#Fear Boost  Passive Increases odds of inflicting Fear (1.5x). 5
#Resist Physical Passive Reduces damage from Phys attacks. 7
    ],
  affinity = {
    DamageType.Phys: DamageAffinity.Strong,
    DamageType.Fire: DamageAffinity.Weak,
    }
  )

# Devil Arcana
PersonaList['Ukobach'] = PersonaStats(
  name = 'Ukobach',
  arcana = Arcana.Devil,
  level = 3,
  skills = [
    SkillList['Agi'],
#Sukunda 12 SP   Decreases 1 foe's Hit/Evasion rate for 3 turns. Innate
#Pulinpa 5 SP    Confuses 1 foe (40% chance).    4
#Confuse Boost   Passive Increases odds of inflicting Confusion (1.5x).  5
#Resist Fire Passive Reduces damage from Fire attacks.   6
#Fire Break  15 SP   Nullifies 1 foe's Fire resistance (for 3 turns).    7
    ],
  affinity = {
    DamageType.Fire: DamageAffinity.Strong,
    DamageType.Ice: DamageAffinity.Weak,
    }
  )

# Justice Arcana
PersonaList['Angel'] = PersonaStats(
  name = 'Angel',
  arcana = Arcana.Justice,
  level = 4,
  skills = [
    SkillList['Garu'],
#Patra   3 SP    Dispels Confusion, Fear, and Rage (1 ally). Innate
#Hama    8 SP    Light: low chance of instant kill, 1 foe. (40% chance)  5
#Sukukaja    12 SP   Increases 1 ally's Hit/Evasion rate for 3 turns.    6
#Regenerate 1    Passive Restores 2% of max HP each turn in battle.  8
#Hama Boost  Passive Light-based attacks are 1.5 times more effective.   9
    ],
  affinity = {
    DamageType.Wind: DamageAffinity.Strong,
    }
  )

# Temperance Arcana
PersonaList['Apsaras'] = PersonaStats(
  name = 'Apsaras',
  arcana = Arcana.Temperance,
  level = 4,
  skills = [
    SkillList['Dia'],
    SkillList['Bufu'], # LV7
#Patra   3 SP    Dispels Confusion, Fear, and Rage (1 ally). Innate
#Dia 3 SP    Slightly restores 1 ally's HP.  Innate
#Rakunda 12 SP   Decreases 1 foe's Defense for 3 turns.  5
#Me Patra    6 SP    Dispels Confusion, Fear, and Rage (party).  6
#Bufu    4 SP    Deals light Ice damage to 1 foe.    7
    ],
  affinity = {
    DamageType.Fire: DamageAffinity.Weak,
    }
  )

# Strength Arcana
PersonaList['Sandman'] = PersonaStats(
  name = 'Sandman',
  arcana = Arcana.Strength,
  level = 5,
  skills = [
    SkillList['Garu'],
#Pulinpa 5 SP    Confuses 1 foe (40% chance).    Innate
#Skull Cracker   9% HP   Deals light Phys damage to 1 foe with a chance of Confusion.    6
#Confuse Boost   Passive Increases odds of inflicting Confusion (1.5x).  7
#Dekaja  10 SP   Nullifies stat bonuses on all foes. 8
#Traesto 18 SP   Instantly escape from a dungeon. (Not available during combat)  11
    ],
  affinity = {
    DamageType.Wind: DamageAffinity.Strong,
    DamageType.Elec: DamageAffinity.Weak,
    }
  )

"""
# A Arcana
PersonaList['X'] = PersonaStats(
  name = 'X',
  arcana = Arcana.A,
  level = L,
  skills = [
    SkillList[''],
    ],
  affinity = {
    DamageType.: DamageAffinity.Strong,
    DamageType.: DamageAffinity.Weak,
    }
  )
"""

