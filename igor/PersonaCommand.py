# ;persona command stuff

from .Persona import *

class PersonaCommand:

  # ;persona command entry-point
  def command(player, cmds):
    # help
    if (len(cmds) == 0):
      player.say(';persona: list - persona list, ' +
        'change <persona number> - change to different persona')
      return

    cmd = cmds[0]

    # ANY: persona list
    if (cmd in [ 'list', 'l' ]):
      cnt = 1
      for id in player.personaKnown:
        p = PersonaList[id]
        msg = ''
        msg += str(cnt) + ': ' + p.name + ' ' + \
          getPersonaInfo(player, p, False)
        cnt += 1
        player.say(msg)

    # ANY: change persona
    elif (cmd in [ 'change', 'c' ]):
      id = int(cmds[1])
      if (id > len(player.personaKnown)):
        return

      # persona switch during the battle is different
      if (player.state == PlayerState.BATTLE):
        player.battle.changePersona(id - 1)
      else:
        player.changePersona(id - 1)

