# Shadow in battle mode

from .Enum import *
from .Persona import *

class Shadow:
  source = None
  player = None
  hp = 0
  sp = 0
  atk = 0
  isKnown = False
  trueName = None
  knockdown = 0
  buffs = None

  def __init__(self, player):
    self.player = player
    self.buffs = dict()

# end turn, -1 turns and check for buffs timeout
  def turn(self):
    calc = False
    for s in self.buffs.copy():
      self.buffs[s] -= 1
      if (self.buffs[s] > 0):
        continue

      self.player.say(s + ' wears off.')
      del self.buffs[s]
      calc = True

    if (calc):
      self.recalc()


# recalc all stats
  def recalc(self):
    oldhp = self.hp
    oldsp = self.sp

    # copy stats from object
    self.__dict__.update(self.source.__dict__)

    # fix old stats
    self.hp = oldhp
    self.sp = oldsp
    self.isKnown = (self.name in self.player.shadowsKnown)
    if (not self.isKnown):
      self.name = "the shadow"

    # apply buffs and debuffs
    for k in self.buffs.keys():
      skill = SkillList[k]
      skill.apply(self)


# reset shadow stats
  def reset(self, o):
    # copy stats from object
    self.source = o
    self.__dict__.update(o.__dict__)
    self.trueName = self.name

    # fix stats
    self.knockdown = 0
    self.maxHP = self.hp
    self.maxSP = self.sp
    self.atk = ShadowAtk[self.level]
    self.buffs.clear()

    # analyzed or not
    self.isKnown = (self.name in self.player.shadowsKnown)
    if (not self.isKnown):
      self.name = "the shadow"


######################################

global SkillList

ShadowAtk = [ 0, 28, 35, 40, 47, 52, 58, 72, 86, 93, 101,
  114, 120, 126, 133, 140, 146, 153, 160, 166, 200 ]
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
  skills = [],
  affinity = {
    DamageType.Ice: DamageAffinity.Weak,
    DamageType.Elec: DamageAffinity.Weak,
    DamageType.Fire: DamageAffinity.Strong,
    }
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
  skills = [],
  affinity = {
    DamageType.Wind: DamageAffinity.Weak,
    DamageType.Phys: DamageAffinity.Strong,
    DamageType.Ice: DamageAffinity.Block,
    }
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
  skills = [ SkillList['Bufu'] ],
  affinity = {
    DamageType.Phys: DamageAffinity.Strong,
    DamageType.Wind: DamageAffinity.Block,
    DamageType.Ice: DamageAffinity.Block,
    DamageType.Elec: DamageAffinity.Block,
    }
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
  skills = [],
  affinity = {
    DamageType.Elec: DamageAffinity.Weak,
    DamageType.Wind: DamageAffinity.Block,
    DamageType.Fire: DamageAffinity.Block,
    }
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
  skills = [ SkillList['Agi'] ],
  # TODO: skill2 = SkillList['Blue Wall'],
  affinity = {
    DamageType.Ice: DamageAffinity.Weak,
    }
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
  skills = [ SkillList['Bash'] ],
  affinity = {
    DamageType.Elec: DamageAffinity.Weak,
    }
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
  skills = [],
  affinity = {
    DamageType.Fire: DamageAffinity.Weak,
    DamageType.Phys: DamageAffinity.Strong,
#    DamageType.Elec: DamageAffinity.Reflect,
    }
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
  skills = [],
  affinity = {
    DamageType.Elec: DamageAffinity.Weak,
    DamageType.Phys: DamageAffinity.Strong,
    }
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
  skills = [],
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

