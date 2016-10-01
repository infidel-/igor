# Admin functions

import random
from .Enum import *
from .Game import Game
from .Dungeon import Dungeon
from .Persona import *
from .Player import *

class Admin:

# ADMIN: entry point
  def command(player, cmds):
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

    # ALL: give level
    elif (cmd == 'level'):
      level = int(cmds[1])
      player.giveExp(LevelXP[level - 1])

    # ALL: persona commands
    elif (cmd == 'persona'):
      if (len(cmds) == 1):
        player.say("give, list")
        return

      cmd2 = cmds[1]

      # give persona
      if (cmd2 == 'give'):
        # help
        if (player.level == 1):
          player.say('No personas on level 1.')

        # give random
        if (len(cmds) == 2):
          player.giveRandomPersona(always = True)
        else:
          id = cmds[2]
          if (id not in PersonaList):
            player.say('No such persona.')
            return
          player.givePersona(id)

      # list personas
      elif (cmd2 == 'list'):
        msg = ''
        for p in PersonaList.values():
          msg += p.id + ' '
        player.say(msg)

