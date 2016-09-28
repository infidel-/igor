# Player class

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
  shadowsKnown = None


  def __init__(self, name):
    self.hp = LevelHP[1]
    self.maxHP = self.hp
    self.sp = LevelSP[1]
    self.maxSP = self.sp
    self.atk = LevelAtk[1]
    self.name = name
    self.persona = Persona('Izanagi')
    self.personaKnown = []
    self.shadowsKnown = []
    self.dungeon = Dungeon()
    self.battle = Battle(self)


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
      getPersonaInfo(self.persona, False) + \
      ' (' + self.persona.skill.getNameAndCost(self) + ').'
    self.say(s)


# whisper to player
  def say(self, msg):
    globals['bot'].say('/w ' + self.name + ' ' + msg)


LevelAtk = [ 0, 42, 53, 60, 71, 78, 88, 108, 130, 140, 152 ]
LevelHP = [ 0, 70, 82, 90, 105, 116, 126, 136, 146, 155, 164 ]
LevelSP = [ 0, 41, 49, 56, 64, 72, 77, 84, 90, 96, 102 ]
LevelXP = [ 0, ]
for i in range(1, 11):
  LevelXP.append(9 + 2 * i + i * i)

