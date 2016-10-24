# igor
Persona RPG IRC (actually Twitch) bot

This is an abandoned project to make Persona-like text RPG.

This bot is a module built on top of sopel (https://sopel.chat/) Python IRC bot. You will need Python 3 and a configured Sopel instance for it to work. By default this is is built to work on Twitch so each messages is prefixed with "/w NICK"

You can also play it offline if you want with "make play" or test it with the commands script by running "make".

Here's the gameplay example:
```
> start
/w NickName "I see that we have a guest."
/w NickName "Hello there."
/w NickName "My name is Igor and I welcome you to the Velvet Room."
/w NickName You are in the Velvet Room.
/w NickName You can: ";dungeon", ";leave".
> dungeon
/w NickName You are in the First dungeon on level 1, room 1.
/w NickName There is a shadow here.
/w NickName You can: ";attack", ";sneak".
> sneak
/w NickName The shadow attacks you!
/w NickName You are in a battle with the shadow. You have 70/70 HP, 41/41 SP. Your persona is Izanagi [Lv 1, Wind Weak, Elec Strong] (Skills 1:Zio [4 SP], 2:Cleave [3 HP], 3:Rakunda [12 SP]).
/w NickName You can: ";attack", ";skill", ";analyze", ";persona", ";retreat".
> analyze
/w NickName This shadow is called Calm Pesce. [Lv 6, ATK 58, HP 82, Ice Block, Wind Weak, Phys Strong]
/w NickName Calm pesce hits you for 11 damage.
/w NickName You are in a battle with Calm Pesce (HP 82/82). You have 59/70 HP, 41/41 SP. Your persona is Izanagi [Lv 1, Wind Weak, Elec Strong] (Skills 1:Zio [4 SP], 2:Cleave [3 HP], 3:Rakunda [12 SP]).
/w NickName You can: ";attack", ";skill", ";analyze", ";persona", ";retreat".
> skill 
/w NickName Usage: ;skill <skill number>
/w NickName Persona skills: 1:Zio [4 SP], 2:Cleave [3 HP], 3:Rakunda [12 SP]
> skill 3
/w NickName You cast Rakunda on Calm Pesce.
/w NickName Calm pesce hits you for 11 damage.
/w NickName You are in a battle with Calm Pesce (HP 82/82). You have 48/70 HP, 29/41 SP. Your persona is Izanagi [Lv 1, Wind Weak, Elec Strong] (Skills 1:Zio [4 SP], 2:Cleave [3 HP], 3:Rakunda [12 SP]).
/w NickName You can: ";attack", ";skill", ";analyze", ";persona", ";retreat".
> analyze
/w NickName This shadow is called Calm Pesce. [Lv 6, ATK 58, HP 82, Ice Strong, Fire Weak, Wind Weak, Elec Weak]
> skill 1
/w NickName You cast Zio on Calm Pesce for 25 damage. Weak! Knockdown!
/w NickName Calm pesce is trying to get up!
/w NickName You are in a battle with Calm Pesce (HP 57/82). You have 48/70 HP, 25/41 SP. Your persona is Izanagi [Lv 1, Wind Weak, Elec Strong] (Skills 1:Zio [4 SP], 2:Cleave [3 HP], 3:Rakunda [12 SP]).
/w NickName You can: ";attack", ";skill", ";analyze", ";persona", ";retreat".
> .
/w NickName You cast Zio on Calm Pesce for 25 damage. Weak! Knockdown!
/w NickName Calm pesce is trying to get up!
/w NickName You are in a battle with Calm Pesce (HP 32/82). You have 48/70 HP, 21/41 SP. Your persona is Izanagi [Lv 1, Wind Weak, Elec Strong] (Skills 1:Zio [4 SP], 2:Cleave [3 HP], 3:Rakunda [12 SP]).
/w NickName You can: ";attack", ";skill", ";analyze", ";persona", ";retreat".
> .
/w NickName You cast Zio on Calm Pesce for 23 damage. Weak! Knockdown!
/w NickName Calm pesce is trying to get up!
/w NickName Rakunda wears off.
/w NickName You are in a battle with Calm Pesce (HP 9/82). You have 48/70 HP, 17/41 SP. Your persona is Izanagi [Lv 1, Wind Weak, Elec Strong] (Skills 1:Zio [4 SP], 2:Cleave [3 HP], 3:Rakunda [12 SP]).
/w NickName You can: ";attack", ";skill", ";analyze", ";persona", ";retreat".
> attack
/w NickName You hit Calm Pesce for 3 damage. Strong!
/w NickName Calm pesce gets up!
/w NickName You are in a battle with Calm Pesce (HP 6/82). You have 48/70 HP, 17/41 SP. Your persona is Izanagi [Lv 1, Wind Weak, Elec Strong] (Skills 1:Zio [4 SP], 2:Cleave [3 HP], 3:Rakunda [12 SP]).
/w NickName You can: ";attack", ";skill", ";analyze", ";persona", ";retreat".
> skill 1
/w NickName You cast Zio on Calm Pesce for 16 damage.
/w NickName You win the battle. You gain 38 experience.
/w NickName Leveru Uppu! You have gained level 3!
/w NickName Pixie joins you!
/w NickName You are in the First dungeon on level 1, room 2.
/w NickName You can: ";forward", ";back".
> persona list
/w NickName 1: Izanagi [Lv 1, Elec Strong, Wind Weak] (Skills 1:Zio [4 SP], 2:Cleave [4 HP], 3:Rakunda [12 SP])
/w NickName 2: Pixie [Lv 2, Fire Weak, Wind Strong] (Skills 1:Dia [3 SP], 2:Zio [4 SP])
> persona
/w NickName ;persona: list - persona list, change <persona number> - change to different persona
> persona change 2
/w NickName You change your persona to Pixie.
```
