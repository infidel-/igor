# Battle class

import random
from .Enum import *
from .Game import Game
from .Dungeon import Dungeon
from .Persona import *
from .Shadow import *

class Battle:
  player = None
  shadow = None

  def __init__(self, player):
    self.player = player
    self.shadow = Shadow(player)


# start new battle
  def start(self):
    self.player.state = PlayerState.BATTLE

    # find random shadow for that level
    floor = self.player.dungeon.level
    if (not floor in ShadowCache):
      raise Exception("No shadows for floor " + str(floor))
    sh = random.choice(ShadowCache[floor])
    self.shadow.reset(sh)

    Game.look(self.player)


# look in battle mode
  def look(self):
    cmds = []
    cmds.append('attack')

    # show skill action only if enough HP/SP
    skill = self.player.persona.skill
    cost = skill.getCost(self.player)
    val = self.player.hp if skill.costType == 'HP' else self.player.sp
    if (cost < val):
      cmds.append('skill')

    if (not self.shadow.isKnown):
      cmds.append('analyze')
    cmds.append('retreat')
    s = 'You are in a battle with ' + self.shadow.name + '.'
    s += ' You have ' + str(self.player.hp) + '/' + str(self.player.maxHP) + \
      ' HP, ' + str(self.player.sp) + '/' + str(self.player.maxSP) + ' SP.'
    s += ' Your persona is ' + self.player.persona.name + ' ' + \
      getPersonaInfo(self.player.persona) + ' (' + \
      self.player.persona.skill.getNameAndCost(self.player) + ').'
    self.player.say(s)

    # list commands
    s = 'You can: ";' + '", ";'.join(cmds) + '".'
    self.player.say(s)


# damage formula
  def damageFormula(self, power, damageType, target):
    # block damage
    if (damageType in target.block):
      return 0

    rnd = 100.0 + random.randint(-5, 5)
    damage = 5 * (power / 100.0) * (rnd / 100.0)
    if (damageType in target.weak):
      damage *= 1.5
    elif (damageType in target.strong):
      damage *= 0.5

    return int(damage)


# attack shadow
  def attack(self):
    # damage to shadow
    damage = self.damageFormula(self.player.atk, DamageType.Phys, self.shadow)
    self.shadow.hp -= damage
    self.player.say('You hit ' + self.shadow.name + ' for ' + str(damage) +
      ' damage.')

    # shadow is dead, win battle
    if (self.shadow.hp <= 0):
      self.finishWin()
      return

    # shadow response
    self.shadowAction()


# use skill
  def skill(self):
    skill = self.player.persona.skill
    cost = skill.getCost(self.player)
    costType = skill.costType
    val = self.player.hp if costType == 'HP' else self.player.sp

    # not enough HP/SP
    if (cost > val):
      return

    # spend cost
    if (costType == 'HP'):
      self.player.hp -= cost
    else:
      self.player.sp -= cost

    # calc and apply damage
    damage = self.damageFormula(skill.power, skill.damageType, self.shadow)
    self.shadow.hp -= damage
    self.player.say('You cast ' + skill.name + ' on ' + self.shadow.name + \
      ' for ' + str(damage) + ' damage.')

    # shadow is dead, win battle
    if (self.shadow.hp <= 0):
      self.finishWin()
      return

    # shadow response
    self.shadowAction()


# try to analyze
  def analyze(self):
    # shadow is already known
    if (self.shadow.isKnown):
      return

    self.shadow.isKnown = True
    self.shadow.name = self.shadow.trueName
    self.player.shadowsKnown.append(self.shadow.trueName)

    s = 'This shadow is called ' + self.shadow.name + '.'
    s += ' ' + getPersonaInfo(self.shadow)
    self.player.say(s)

    # shadow response
    self.shadowAction()


# try to retreat
  def retreat(self):
    rnd = random.randint(0, 100)
    if (rnd < 40):
      self.player.say('You manage to retreat from the battle.')
      self.player.state = PlayerState.IDLE
      return

    # shadow response
    self.shadowAction()


# shadow action
  def shadowAction(self):
    # randomly use skill
    rnd = random.randint(0, 100)
    damage = 0
    msg = ''
    if (self.shadow.skill != None and rnd < 30):
      skill = self.shadow.skill

      # calc and apply damage
      damage = self.damageFormula(skill.power, skill.damageType,
        self.player.persona)
      self.shadow.hp -= damage
      msg = self.shadow.name.capitalize() + ' casts ' + skill.name + \
        ' on you for ' + str(damage) + ' damage.'
    else:
      # damage to player
      damage = self.damageFormula(self.shadow.atk, DamageType.Phys,
        self.player.persona)
      msg = self.shadow.name + ' hits you for ' + \
        str(damage) + ' damage.'

    self.player.hp -= damage
    self.player.say(msg)

    # player is dead, lose battle
    if (self.player.hp <= 0):
      self.finishLose()
      return

    # look around
    Game.look(self.player)


# win battle
  def finishWin(self):
    exp = self.shadow.exp
    self.player.say('You win the battle. You gain ' + str(exp) + \
      ' experience.')
    self.player.giveExp(exp)
    self.player.state = PlayerState.IDLE
    self.player.dungeon.shadow = False

    Game.look(self.player)


# lose battle
  def finishLose(self):
    self.player.say('You lose the battle.')
    self.player.state = PlayerState.IDLE
    self.player.location = Location.VELVET_ROOM

    Game.look(self.player)

