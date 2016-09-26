# Player class

from .Global import *
from .Enum import *
from .Dungeon import Dungeon
from .Battle import Battle
from .Persona import Persona

class Player:
  location = Location.VELVET_ROOM
  name = None
  hp = 100
  maxHP = 100
  sp = 50
  maxSP = 50
  dungeon = None
  battle = None
  persona = None
  state = PlayerState.IDLE
  personaKnown = None
  shadowsKnown = None


  def __init__(self, name):
    self.name = name
    self.persona = Persona('Izanagi')
    self.personaKnown = []
    self.shadowsKnown = []
    self.dungeon = Dungeon()
    self.battle = Battle(self)


# whisper to player
  def say(self, msg):
    globals['bot'].say('/w ' + self.name + ' ' + msg)

