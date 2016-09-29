# Game class

import random
from .Global import *
from .Enum import *

class Game:

# parse command
  def command(player, cmds):
    cmd = cmds[0]

    # ANY: repeat last command
    if (cmd == '.' and player.lastCommand != None):
      cmds = player.lastCommand
      cmd = cmds[0]

    # ANY: help
    if (cmd in [ 'help', 'h' ]):
      player.say(';help - show this list, ;look - look around (shows a list of commands), ;start - (re)start a game, ;info - player stats and info')

    # ANY: look around
    elif (cmd in [ 'look', 'l', 'x' ]):
      Game.look(player)

    # ANY: stats
    elif (cmd in [ 'info', 'stats', 'st', 'i' ]):
      player.stats()

    # VELVET: go to dungeon
    elif (cmd in [ 'dungeon', 'dung', 'dun' ]):
      Game.dungeon(player)

    # VELVET: leave
    elif (cmd in [ 'leave' ]):
      Game.leave(player)

    # DUNGEON, BATTLE: attack shadow
    elif (cmd in [ 'attack', 'att', 'at', 'a' ]):
      Game.attack(player)

    # BATTLE: analyze shadow
    elif (cmd in [ 'analyze', 'anal', 'an' ]):
      Game.analyze(player)

    # BATTLE: use persona skill
    elif (cmd in [ 'skill', 'sk' ]):
      Game.skill(player, cmds)

    # BATTLE: retreat
    elif (cmd in [ 'retreat', 'r' ]):
      Game.retreat(player)

    # DUNGEON: sneak to next room
    elif (cmd in [ 'sneak', 's' ]):
      Game.sneak(player)

    # DUNGEON: go to next room
    elif (cmd in [ 'forward', 'f' ]):
      Game.forward(player)

    # DUNGEON: go to previous room
    elif (cmd in [ 'back', 'b' ]):
      Game.back(player)

    # DUNGEON: go to next level
    elif (cmd in [ 'up', 'u' ]):
      Game.up(player)

    # hehe
    elif (cmd == 'xyzzy'):
      player.say('Something happens.')

    # save last command
    if (cmd != '.'):
      player.lastCommand = cmds


# new player intro
  def intro(player):
    player.say('"I see that we have a guest."')
    player.say('"Why, hello there."')
    player.say('"My name is Igor and I welcome you to the Velvet Room."')
    player.say('"Unfortunately, my assistant is on vacation."')

    Game.look(player)
    Game.command(player, [ 'help' ])


# ANY: look around
  def look(player):
    cmds = []

    # velvet room
    if (player.location == Location.VELVET_ROOM):
      player.say('You are in the Velvet Room.')
      cmds.append('dungeon')
      cmds.append('leave')

    # dungeon
    elif (player.location == Location.DUNGEON):
      # in battle
      if (player.state == PlayerState.BATTLE):
        player.battle.look()
        return

      player.say('You are in the ' + player.dungeon.name +
        ' dungeon on level ' + str(player.dungeon.level) + ', room ' +
        str(player.dungeon.room) + '.')
      if (player.dungeon.shadow == True):
        player.say('There is a shadow here.')

        cmds.append('attack')
        if (player.dungeon.level != player.dungeon.maxLevel or
            player.dungeon.room != 4):
          cmds.append('sneak')
      else:
        if (player.dungeon.room < 4):
          cmds.append('forward')
        else:
          cmds.append('up')

      if (not player.dungeon.room == 1):
        cmds.append('back')

    # list commands
    s = 'You can: ";' + '", ";'.join(cmds) + '".'
    player.say(s)


# VELVET: go to dungeon
  def dungeon(player):
    # only from velvet room
    if (player.location != Location.VELVET_ROOM):
      return

    player.location = Location.DUNGEON

    Game.look(player)


# game over
  def gameOver(player):
    player.say('Game over.')

    del globals['bot'].memory['players'][player.name]


# VELVET: leave (game over)
  def leave(player):
    # only from velvet room
    if (player.location != Location.VELVET_ROOM):
      return

    player.say('You leave the Velvet Room and return to reality.')

    Game.gameOver(player)


# DUNGEON, BATTLE: attack shadow
  def attack(player):
    if (player.location == Location.VELVET_ROOM):
      player.say('"Interesting, he-he. I will personally dispose of you."')
      Game.gameOver(player)
      return

    elif (player.state == PlayerState.BATTLE):
      player.battle.attack()
      return

    elif (player.dungeon.shadow == False):
      player.say('There is nobody here.')
      return

    player.say('You attack the shadow.')
    player.battle.start()


# BATTLE: use persona skill
  def skill(player, cmds):
    if (player.state != PlayerState.BATTLE):
      return

    if (len(cmds) < 2):
      player.say('Usage: ;skill <skill number>')
      return

    index = -1
    try:
      index = int(cmds[1])
    except ValueError:
      return

    player.battle.skill(int(cmds[1]) - 1)


# BATTLE: analyze
  def analyze(player):
    if (player.state != PlayerState.BATTLE):
      return

    player.battle.analyze()


# BATTLE: retreat
  def retreat(player):
    if (player.state != PlayerState.BATTLE):
      return

    player.battle.retreat()


# DUNGEON: go to next room
  def forward(player):
    if (player.location != Location.DUNGEON):
      return
    elif (player.state == PlayerState.BATTLE):
      return
    elif (player.dungeon.shadow == True):
      player.say('There is a shadow blocking your path.')
      return

    ret = player.dungeon.forward()
    if (not ret):
      return

    player.say('You move to the next room.')

    Game.look(player)


# DUNGEON: go to previous room
  def back(player):
    if (player.location != Location.DUNGEON):
      return
    elif (player.state == PlayerState.BATTLE):
      return
#TODO: maybe exploited by going back and forth until there's no shadow
#    elif (player.dungeon.shadow == True):
#      player.say('There is a shadow blocking your path.')
#      return

    ret = player.dungeon.back()
    if (not ret):
      return

    player.say('You return to the previous room.')

    Game.look(player)


# DUNGEON: sneak to next room
  def sneak(player):
    if (player.location != Location.DUNGEON):
      return
    elif (player.state == PlayerState.BATTLE):
      return
    elif (player.dungeon.shadow == False):
      return

    rnd = random.randint(0, 100)

    if (player.dungeon.room < 4):
      ret = player.dungeon.forward()
      if (not ret):
        return

      if (rnd >= 30):
        player.say('The shadow attacks you!')
        player.battle.start()
        return

      player.say('You sneak around the shadow to the next room.')
    else:
      # cannot sneak past the boss
      if (player.dungeon.level == player.dungeon.maxLevel):
        return

      if (rnd >= 30):
        player.say('The shadow attacks you!')
        player.battle.start()
        return

      player.dungeon.up()
      player.say('You sneak around the shadow up the stairs.')

    Game.look(player)


# DUNGEON: go to next level
  def up(player):
    if (player.location != Location.DUNGEON):
      return
    elif (player.state == PlayerState.BATTLE):
      return
    elif (player.dungeon.shadow == True):
      player.say('There is a shadow blocking your path.')
      return

    # game over
    if (player.dungeon.level == player.dungeon.maxLevel and
        player.dungeon.room == 4):
      player.say('You finish the ' + player.dungeon.name + ' dungeon. Thanks for playing!')
      Game.gameOver(player)
      return

    ret = player.dungeon.up()
    if (not ret):
      return

    player.say('You go up to the next level.')

    Game.look(player)

