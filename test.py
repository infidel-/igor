# coding=utf-8
"""This module has classes and functions that can help in writing tests.

test_tools.py - Sopel misc tools
Copyright 2013, Ari Koivula, <ari@koivu.la>
Licensed under the Eiffel Forum License 2.

https://sopel.chat
"""
from __future__ import unicode_literals, absolute_import, print_function, division

import os
import re
import sys
import tempfile

import igor

try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

import sopel.config
import sopel.config.core_section
import sopel.tools
import sopel.trigger


class MockConfig(sopel.config.Config):
    def __init__(self):
        self.filename = tempfile.mkstemp()[1]
        #self._homedir = tempfile.mkdtemp()
        #self.filename = os.path.join(self._homedir, 'test.cfg')
        self.parser = ConfigParser.RawConfigParser(allow_no_value=True)
        self.parser.add_section('core')
        self.parser.set('core', 'owner', 'Embolalia')
        self.define_section('core', sopel.config.core_section.CoreSection)
        self.get = self.parser.get

    def define_section(self, name, cls_):
        if not self.parser.has_section(name):
            self.parser.add_section(name)
        setattr(self, name, cls_(self, name))


class MockSopel(object):
    def __init__(self, nick, admin=False, owner=False):
        self.nick = nick
        self.user = "sopel"

        self.channels = ["#channel"]

        self.memory = sopel.tools.SopelMemory()

        self.ops = {}
        self.halfplus = {}
        self.voices = {}

        self.config = MockConfig()
        self._init_config()

        if admin:
            self.config.core.admins = [self.nick]
        if owner:
            self.config.core.owner = self.nick

    def cap_req(self, module, cap):
        None

    def _init_config(self):
        cfg = self.config
        cfg.parser.set('core', 'admins', '')
        cfg.parser.set('core', 'owner', '')
        home_dir = os.path.join(os.path.expanduser('~'), '.sopel')
        if not os.path.exists(home_dir):
            os.mkdir(home_dir)
        cfg.parser.set('core', 'homedir', home_dir)


class MockSopelWrapper(object):
    def __init__(self, bot, pretrigger):
        self.bot = bot
        self.pretrigger = pretrigger
        self.output = []

    def _store(self, string, recipent=None):
        print(string.strip())
        self.output.append(string.strip())

    say = reply = action = _store

    def __getattr__(self, attr):
        return getattr(self.bot, attr)


# run test

bot = MockSopel("NickName", admin=False, owner=False)
bot.config.core.prefix = ';'

# full playthrough
msg1 = [
  "start",
  "leave",
  "start",
  "attack",
  "start",
  "look",
  "dungeon",

# room 1
  "attack",
  "attack",
  "attack",
  "forward",

# room 2
  "attack",
  "attack",
  "attack",
  "forward",

# room 3
  "attack",
  "attack",
  "attack",
  "forward",

# room 4
  "attack",
  "attack",
  "attack",
  "forward",

# level 2
  "up",

# level 10
  "admin dungeon 10",

# room 1
  "attack",
  "attack",
  "attack",
  "forward",

# room 2
  "back",
  "forward",
  "attack",
  "attack",
  "attack",
  "forward",

# room 3
  "sneak",
  "attack",
  "attack",
  "attack",
  "forward",

# room 4
  "attack",
  "attack",
  "attack",
  "up",
  ]

# random battle
msg_battle = [
  "start",
  "info",
  "dungeon",

  "admin battle",
  "analyze",
  "admin kill",
  "admin dungeon 3",
  "admin battle",
  "analyze",
  ]
msg_battle2 = [
  "start",
  "info",
  "dungeon",

  "admin battle",
  "analyze",
  "admin kill",
  "admin dungeon 2",

  "admin battle",
  "analyze",
  "skill",
  "attack",
  "admin kill",
  "info",
  ]

msg_battle3 = [
  "start",
  "dungeon",

  "admin battle",
  "analyze",
  "skill 3",
  "analyze",
  "attack",
  "attack",
  "analyze",
  "attack",
  "analyze",
  ]

msg_battle4 = [
  "start",
  "dungeon",

  "admin battle",
  "admin kill",
  "admin battle",
  "admin kill",
  "admin battle",
  "admin kill",
  "admin battle",
  "admin kill",
  "admin battle",
  "admin kill",
  ]

msg_persona = [
  "start",
  "dungeon",
  "admin level 5",
  "admin persona give",
  "admin persona give",
  "persona",
  "persona list",
  "persona switch 2",
  "info",
  "persona switch 3",
  "info",
  "admin battle",
  "skill 1",
  "persona switch 2",
  "skill 1",
  "look",
  ]

#msgs = msg1
msgs = msg_persona


def message(bot, m):
  msg = ";" + m
  match = None

  # get command
  command = m
  if (m.find(' ') > 0):
    arr = m.split()
    command = arr[0]

  regexp = sopel.tools.get_command_regexp(".", command)
  match = regexp.match(msg)
  assert match, "Example did not match any command."

  sender = "#channel"
  hostmask = "%s!%s@%s " % (bot.nick, "UserName", "example.com")
  full_message = ':{} PRIVMSG {} :{}'.format(hostmask, sender, msg)

  pretrigger = sopel.trigger.PreTrigger(bot.nick, full_message)
  trigger = sopel.trigger.Trigger(bot.config, pretrigger, match)

  module = sys.modules['igor']
  if hasattr(module, 'setup'):
      module.setup(bot)

  wrapper = MockSopelWrapper(bot, trigger)
  module.command(wrapper, trigger)


play = (len(sys.argv) > 1 and sys.argv[1] == '-i')

if (play):
  message(bot, 'start')
  message(bot, 'dungeon')
  while True:
    m = input('> ')
    message(bot, m)
else:
  for m in msgs:
    print("\n> " + m)
    message(bot, m)

