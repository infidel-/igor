# ;persona command stuff

from .Persona import *

class PersonaCommand:

  # ;persona command entry-point
  def command(player, cmds):
    # help
    if (len(cmds) == 0):
      player.say(';persona: list - persona list, switch <persona number> - switch to different persona')
      return

    cmd = cmds[0]

    # ANY: persona list
    if (cmd == 'list'):
      cnt = 1
      for id in player.personaKnown:
        p = PersonaList[id]
        msg = ''
        msg += str(cnt) + ': ' + p.name + ' ' + \
          getPersonaInfo(player, p, False)
        cnt += 1
        player.say(msg)

    # ANY: switch persona
    elif (cmd == 'switch'):
      id = int(cmds[1])
      if (id > len(player.personaKnown)):
        return

      # persona switch during the battle is different
      if (player.state == PlayerState.BATTLE):
        player.battle.switchPersona(id - 1)
      else:
        player.switchPersona(id - 1)

