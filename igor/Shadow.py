# Shadow in battle mode

from .Enum import *
from .Persona import *

class Shadow:
  player = None
  hp = 0
  sp = 0
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

    # analyzed or not
    isKnown = (self.name in self.player.shadowsKnown)
    if (not isKnown):
      self.name = "the shadow"


######################################

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
  weak = (),
  strong = (),
  block = (),
  absorb = (),
  reflect = (),
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
  weak = (),
  strong = (),
  block = (),
  absorb = (),
  reflect = (),
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
  weak = (),
  strong = (),
  block = (),
  absorb = (),
  reflect = (),
  )
"""

# fill shadows cache by level
for s in ShadowList:
  shadow = ShadowList[s]
  for i in range(shadow.floor[0], shadow.floor[1] + 1):
    if (not i in ShadowCache):
      ShadowCache[i] = []
    ShadowCache[i].append(shadow)

