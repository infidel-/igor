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

# SUPPORT SKILLS
SkillList['Rakunda'] = PersonaSkill(
  name = 'Rakunda',
  type = SkillType.SupportEnemy,
  cost = 12,
  costType = 'SP',
  damageType = None,
  power = 0,
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
    SkillList['Rakunda'],
#    SkillList['Rakukaja'],
#    SkillList['Tarukaja'],
    ],
  affinity = {
    DamageType.Wind: DamageAffinity.Weak,
    DamageType.Elec: DamageAffinity.Strong,
    }
  )

# Chariot Arcana
PersonaList['Slime'] = PersonaStats(
  name = 'Slime',
  arcana = Arcana.Chariot,
  level = 2,
  skills = [
    SkillList['Bash'],
    ],
  affinity = {}
  )
