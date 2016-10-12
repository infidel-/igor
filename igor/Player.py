# Player class

import random
from .Global import *
from .Enum import *
from .Dungeon import Dungeon
from .Battle import Battle
from .Persona import *

class Player:
  lastCommand = None
  location = Location.VELVET_ROOM
  name = None
  hp = 0
  maxHP = 0
  sp = 0
  maxSP = 0
  exp = 0
  level = 1
  atk = 0
  dungeon = None
  battle = None
  persona = None
  state = PlayerState.IDLE
  personaKnown = None
  personaInited = None
  shadowsKnown = None
  msgs = None


  def __init__(self, name):
    self.hp = LevelHP[1]
    self.maxHP = self.hp
    self.sp = LevelSP[1]
    self.maxSP = self.sp
    self.atk = LevelAtk[1]
    self.name = name
    self.persona = Persona('Izanagi')
    self.personaKnown = [ 'Izanagi' ]
    self.personaInited = [ self.persona ]
    self.shadowsKnown = []
    self.msgs = []
    self.dungeon = Dungeon()
    self.battle = Battle(self)

# change persona
  def changePersona(self, id):
    self.persona = self.personaInited[id]
    self.say('You change your persona to ' + self.persona.name + '.')


# give random persona of appropriate level
  def giveRandomPersona(self, always = False):
    # 40% chance
    if (not always and random.randint(0, 100) > 40):
      return

    # pick a persona
    tmp = []
    for p in PersonaList.values():
      if (p.level <= self.level and p.name not in self.personaKnown):
        tmp.append(p.name)
    if (len(tmp) == 0):
      return

    id = random.choice(tmp)
    self.givePersona(id)


# give specific persona
  def givePersona(self, id):
    self.personaKnown.append(id)
    self.personaInited.append(Persona(id))
    self.say(id + ' joins you!')


# give experience and potentially new level
  def giveExp(self, exp):
    self.exp += exp
    newlevel = self.level
    maxexp = 0
    for i in range(0, len(LevelXP)):
      maxexp = LevelXP[i]
      if (self.exp >= LevelXP[i]):
        newlevel = i + 1
    if (newlevel > 10):
      newlevel = 10
    if (self.exp > maxexp):
      self.exp = maxexp

    if (self.level == newlevel):
      return

    # new level
    self.level = newlevel
    self.hp = LevelHP[self.level]
    self.maxHP = self.hp
    self.sp = LevelSP[self.level]
    self.maxSP = self.sp
    self.atk = LevelAtk[self.level]
    self.say('Leveru Uppu! You have gained level ' + str(self.level) + '!')


# print stats
  def stats(self):
    s = 'LV ' + str(self.level) + ', XP ' + str(self.exp) + '/' + \
      str(LevelXP[self.level])
    s += ', ATK ' + str(self.atk)
    s += ', HP ' + str(self.hp) + '/' + str(self.maxHP) + \
      ', SP ' + str(self.sp) + '/' + str(self.maxSP) + '.'
#      ', LV ' + str(self.persona.level) + \
    s += ' Persona: ' + self.persona.name + ' ' + \
      getPersonaInfo(self, self.persona, False) + '.'
    self.say(s)


# whisper to player
  def say(self, msg):
    self.msgs.append(msg)
#    globals['bot'].say('/w ' + self.name + ' ' + msg)


LevelAtk = [ 0, 42, 53, 60, 71, 78, 88, 108, 130, 140, 152,
  172, 180, 190, 200, 210, 220, 230, 240, 250, 300
  ]
LevelHP = [ 0, 70, 82, 90, 105, 116, 126, 136, 146, 155, 164,
   173, 182, 190, 199, 207, 215, 223, 230, 238, 245,
  ]
LevelSP = [ 0, 41, 49, 56, 64, 72, 77, 84, 90, 96, 102,
  107, 113, 118, 123, 128, 133, 138, 142, 147, 151,
  ]
LevelXP = [ 0, ]
for i in range(1, 16):
#  LevelXP.append(9 + 2 * i + i * i)
  LevelXP.append((9 + 2 * i + i * i) * 2)

