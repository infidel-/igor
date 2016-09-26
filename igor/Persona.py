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
    c = self.cost[0]
    if (self.cost[1] == '%'):
      c = (player.maxHP if self.costType == 'HP' else player.maxSP) * c / 100.0
      c = int(c)
    return c


######################################

PersonaList = dict()

# Fool Arcana
PersonaList['Orpheus'] = PersonaStats(
  name = 'Orpheus',
  arcana = Arcana.Fool,
  level = 1,
  hp = 20,
  skill = PersonaSkill(
    name = 'Bash',
    cost = (7, '%'),
    costType = 'HP',
    power = 120,
    )
  )

# Chariot Arcana
PersonaList['Slime'] = PersonaStats(
  name = 'Slime',
  arcana = Arcana.Chariot,
  level = 2,
  hp = 20,
  skill = PersonaSkill(
    name = 'Bash',
    cost = (7, '%'),
    costType = 'HP',
    power = 120,
    )
  )
