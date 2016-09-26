# Admin functions

import random
from .Enum import *
from .Game import Game
from .Dungeon import Dungeon

class Admin:

# ADMIN: entry point
  def admin(player, cmds):
    cmd = cmds[0]

    # DUNGEON: go to dungeon level
    if (cmd == 'dungeon'):
      if (player.location != Location.DUNGEON):
        return
      level = int(cmds[1])
      player.dungeon._up(level)
      Game.look(player)

    # DUNGEON: battle
    elif (cmd == 'battle'):
      if (player.location != Location.DUNGEON):
        return
      player.dungeon.shadow = True
      Game.attack(player)

    # BATTLE: kill shadow
    elif (cmd == 'kill'):
      if (player.state != PlayerState.BATTLE):
        return
      player.battle.shadow.hp = 0
      Game.attack(player)

