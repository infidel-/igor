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


# persona stats

class PersonaStats:
  def __init__(self, **fields):
    self.__dict__.update(fields)


# persona skill

class PersonaSkill:
  def __init__(self, **fields):
    self.__dict__.update(fields)

# get skill name and cost
  def getNameAndCost(self, player):
    return self.name + ': ' + str(self.getCost(player)) + ' ' + self.costType

# get skill cost
  def getCost(self, player):
    c = self.cost
    if (self.costType == 'HP'):
      c = player.maxHP * c / 100.0
      c = int(c)
    return c


######################################

SkillList = dict()
SkillList['Bash'] = PersonaSkill(
  name = 'Bash',
  cost = 7,
  costType = 'HP',
  damageType = DamageType.Phys,
  power = 120,
  )
SkillList['Agi'] = PersonaSkill(
  name = 'Agi',
  cost = 4,
  costType = 'SP',
  damageType = DamageType.Fire,
  power = 80,
  )
SkillList['Zio'] = PersonaSkill(
  name = 'Zio',
  cost = 4,
  costType = 'SP',
  damageType = DamageType.Elec,
  power = 80,
  )
SkillList['Bufu'] = PersonaSkill(
  name = 'Bufu',
  cost = 4,
  costType = 'SP',
  damageType = DamageType.Ice,
  power = 80,
  )
SkillList['Garu'] = PersonaSkill(
  name = 'Garu',
  cost = 4,
  costType = 'SP',
  damageType = DamageType.Wind,
  power = 80,
  )

######################################

PersonaList = dict()

# Fool Arcana
PersonaList['Izanagi'] = PersonaStats(
  name = 'Izanagi',
  arcana = Arcana.Fool,
  level = 1,
  skill = SkillList['Zio'],
  weak = [ DamageType.Wind ],
  strong = [ DamageType.Elec ],
  block = [],
  absorb = [],
  reflect = [],
  )

# Chariot Arcana
PersonaList['Slime'] = PersonaStats(
  name = 'Slime',
  arcana = Arcana.Chariot,
  level = 2,
  skill = SkillList['Bash'],
  weak = [],
  strong = [],
  block = [],
  absorb = [],
  reflect = [],
  )
