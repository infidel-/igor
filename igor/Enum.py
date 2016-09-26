# All enums

from enum import Enum

class PlayerState(Enum):
  IDLE = 0
  BATTLE = 1

class Location(Enum):
  VELVET_ROOM = 0
  DUNGEON = 1

class DamageType(Enum):
  Phys = 0,
  Fire = 1,
  Ice = 2,
  Elec = 3,
  Wind = 4,

class Arcana(Enum):
  Fool = 0,
  Magician = 1,
  Priestess = 2,
  Empress = 3,
  Emperor = 4,
  Hierophant = 5,
  Lovers = 6,
  Chariot = 7,
  Strength = 8,
  Hermit = 9,
  Fortune = 10,
  Justice = 11,
  HangedMan = 12,
  Death = 13,
  Temperance = 14,
  Devil = 15,
  Tower = 16,
  Star = 17,
  Moon = 18,
  Sun = 19,
  Judgement = 20,
  World = 21,

