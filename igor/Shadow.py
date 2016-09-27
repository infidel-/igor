# Shadow in battle mode

from .Enum import *
from .Persona import *

class Shadow:
  player = None
  hp = 0
  sp = 0
  atk = 0
  isKnown = False
  trueName = None

  def __init__(self, player):
    self.player = player


# reset shadow stats
  def reset(self, o):
    # copy stats from object
    self.__dict__.update(o.__dict__)
    self.trueName = self.name

    # fix stats
    self.maxHP = self.hp
    self.maxSP = self.sp
    self.atk = ShadowAtk[self.level]

    # analyzed or not
    isKnown = (self.name in self.player.shadowsKnown)
    if (not isKnown):
      self.name = "the shadow"

# get info string
  def getInfo(self):
    s = '[Lv ' + str(self.level)
    if (len(self.weak) > 0):
      s += ', Weak:'
      for t in self.weak:
        s += ' ' + t.name
    if (len(self.strong) > 0):
      s += ', Strong:'
      for t in self.strong:
        s += ' ' + t.name
    if (len(self.block) > 0):
      s += ', Block:'
      for t in self.block:
        s += ' ' + t.name
    s += ']'

    return s



######################################

global SkillList

ShadowAtk = [ 0, 40, 50, 60, 70, 75, 80, 90, 100, 110, 120 ]
ShadowCache = dict()
ShadowList = dict()

ShadowList['Lying Hablerie'] = PersonaStats(
  name = 'Lying Hablerie',
  arcana = Arcana.Magician,
  floor = (1, 2),
  level = 5,
  hp = 73,
  sp = 51,
  exp = 24,
  yen = 180,
  skill = None,
  weak = [ DamageType.Ice, DamageType.Elec ],
  strong = [ DamageType.Fire ],
  block = [],
  absorb = [],
  reflect = [],
  )

ShadowList['Calm Pesce'] = PersonaStats(
  name = 'Calm Pesce',
  arcana = Arcana.Priestess,
  floor = (1, 2),
  level = 6,
  hp = 82,
  sp = 23,
  exp = 38,
  yen = 180,
  skill = None,
  weak = [ DamageType.Wind ],
  strong = [ DamageType.Phys ],
  block = [ DamageType.Ice ],
  absorb = [],
  reflect = [],
  )

ShadowList['Trance Twins'] = PersonaStats(
  name = 'Trance Twins',
  arcana = Arcana.Hierophant,
  floor = (3, 5),
  level = 7,
  hp = 122,
  sp = 62,
  exp = 61,
  yen = 200,
  # TODO: skill = SkillList['Mabufu'],
  skill = SkillList['Bufu'],
  weak = [],
  strong = [ DamageType.Phys ],
  block = [ DamageType.Ice, DamageType.Elec, DamageType.Wind ],
  absorb = [],
  reflect = [],
  )

ShadowList['Black Raven'] = PersonaStats(
  name = 'Black Raven',
  arcana = Arcana.Hermit,
  floor = (3, 7),
  level = 7,
  hp = 108,
  sp = 25,
  exp = 57,
  yen = 180,
  #  TODO: skill = SkillList['Tarukaja'],
  skill = None,
  weak = [ DamageType.Elec ],
  strong = [],
  block = [ DamageType.Fire, DamageType.Wind ],
  absorb = [],
  reflect = [],
  )

ShadowList['Magic Hand'] = PersonaStats(
  name = 'Magic Hand',
  arcana = Arcana.Magician,
  floor = (3, 5),
  level = 8,
  hp = 130,
  sp = 10,
  exp = 77,
  yen = 190,
  skill = SkillList['Agi'],
  # TODO: skill2 = SkillList['Blue Wall'],
  weak = [ DamageType.Ice ],
  strong = [],
  block = [],
  absorb = [],
  reflect = [],
  )

# TODO: actually summoned by Positive King
ShadowList['Secret Bambino'] = PersonaStats(
  name = 'Secret Bambino',
  arcana = Arcana.Empress,
  floor = (4, 7),
  level = 10,
  hp = 122,
  sp = 62,
  exp = 61,
  yen = 200,
  skill = SkillList['Bash'],
  weak = [ DamageType.Elec ],
  strong = [],
  block = [],
  absorb = [],
  reflect = [],
  )

# TODO: special AI
# It will summon a Secret Bambino and then try to hit party members with Zio. After some turns pass, it will Stand By and then escape the battle. If a Phantom Mage is present in battle, it may instead summon a Bronze Dice shadow.
ShadowList['Positive King'] = PersonaStats(
  name = 'Positive King',
  arcana = Arcana.Emperor,
  floor = (4, 7),
  level = 11,
  hp = 160,
  sp = 43,
  exp = 142,
  yen = 200,
  # TODO: skill = SkillList['Summon Secret Bambino'],
  skill = None,
  weak = [],
  strong = [],
  block = [],
  absorb = [],
  reflect = [],
  )

ShadowList['Bronze Dice'] = PersonaStats(
  name = 'Bronze Dice',
  arcana = Arcana.Fortune,
  floor = (4, 7),
  level = 10,
  hp = 130,
  sp = 34,
  exp = 222,
  yen = 200,
  # TODO: skill = SkillList['Last Resort'],
  skill = None,
  weak = [ DamageType.Elec ],
  strong = [ DamageType.Phys ],
  block = [],
  absorb = [],
  reflect = [],
  )

"""
ShadowList[''] = PersonaStats(
  name = '',
  arcana = Arcana.,
  floor = (),
  level = ,
  hp = ,
  sp = ,
  exp = ,
  yen = ,
  skill = None,
  weak = [],
  strong = [],
  block = [],
  absorb = [],
  reflect = [],
  )
"""

# fill shadows cache by level
for s in ShadowList:
  shadow = ShadowList[s]
  for i in range(shadow.floor[0], shadow.floor[1] + 1):
    if (not i in ShadowCache):
      ShadowCache[i] = []
    ShadowCache[i].append(shadow)

