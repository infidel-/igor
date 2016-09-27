# Dungeon class

import random

class Dungeon:
  level = 1
  maxLevel = 8
  room = 1
  name = "First"
  shadow = False

  def __init__(self):
    self.initRoom()


# init new room
  def initRoom(self):
    if (random.randint(0, 100) < 70):
      self.shadow = True


# move forward
  def forward(self):
    # last room on this level
    if (self.room == 4):
      return False

    self.room += 1
    self.initRoom()
    return True


# move back
  def back(self):
    # first room on this level
    if (self.room == 1):
      return False

    self.room -= 1
    self.initRoom()
    return True


# move up
  def up(self):
    # last room on this level
    if (self.room != 4):
      return False

    self._up(self.level + 1)
    return True


# move up to specified level
  def _up(self, level):
    self.room = 1
    self.level = level
    self.initRoom()

