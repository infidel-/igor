#import sys
#sys.path.append("./")
import os
from sopel import module
from sopel import tools

from .VERSION import *
from .Global import *
from .Admin import Admin
from .Game import Game
from .Player import Player

# convert version string to string array
version = VERSION.split("\n")

# game setup
def setup(bot):
  bot.cap_req('igor', 'twitch.tv/tags')
  bot.cap_req('igor', 'twitch.tv/commands')
  if (not bot.memory.contains('players')):
    bot.memory['players'] = tools.SopelMemory()

# all chat lines
@module.rule('.*')
def command(bot, trigger):
  # skip common chat
  if (not trigger.group(0).startswith(bot.config.core.prefix)):
    return

  _command(bot, trigger)


# all whispers to bot
@module.event('WHISPER')
@module.rule('.*')
def event(bot, trigger):
  _command(bot, trigger)


# common command
def _command(bot, trigger):
    g = trigger.group(0)
    if (g.startswith(bot.config.core.prefix)):
      g = g[1:]
    cmds = g.split()
    cmd = cmds[0]

    # we do initial command thing here to avoid circular deps in
    # Game -> Player -> Battle -> Game
    # start new game
    if (cmd in [ 'start', 'restart' ]):
      p = initPlayer(bot, trigger)
      Game.intro(p)

    # ANY: game version and changes
    elif (cmd in [ 'version', 'changes' ]):
      for msg in version:
        say(bot, trigger.nick, msg)

    # ADMIN: admin entry point
    elif (cmd in [ 'admin' ]):
      p = getPlayer(bot, trigger)
      if (p == None):
        say(bot, trigger.nick, 'You must ";start" a new game first.')
        return

      cmds.pop(0)
      Admin.command(p, cmds)

    # any other command
    else:
      p = getPlayer(bot, trigger)
      if (p == None):
        say(bot, trigger.nick, 'You must ";start" a new game first.')
        return

      Game.command(p, cmds)


############################################

# whisper to user
def say(bot, nick, msg):
  bot.say('/w ' + nick + ' ' + msg)


# init new player instance
def initPlayer(bot, trigger):
  globals['bot'] = bot

  # new player instance
  p = Player(trigger.nick)

  # set player record
  bot.memory['players'][trigger.nick] = p

  return p


# returns the player instance for this user
def getPlayer(bot, trigger):
  globals['bot'] = bot

  # init memory if needed
  if (not bot.memory.contains('players')):
    return None

  # player exists, return it
  if (bot.memory['players'].contains(trigger.nick)):
    return bot.memory['players'][trigger.nick]

  return None


if __name__ == "__main__":
  from sopel.test_tools import run_example_tests
  run_example_tests(__file__, verbose = False)
