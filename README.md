# BoredomBot

This is the github repository for my discord bot [BoredomBot](https://discord.com/oauth2/authorize?client_id=711448228993826817&permissions=8&scope=bot) (Click on the name to invite).

- [x] Name: Reduce Boredom
#1039
- [x] Prefix: `'!b '`
- [x] Id: `711448228993826817` 

## Feautures

### **Table of Commands**


- [COVID-19 Cases](https://github.com/BrimCap/BoredomBot#covid-19-cases)
- [Countdown](https://github.com/BrimCap/BoredomBot#countdown)
- [Guess Game](https://github.com/BrimCap/BoredomBot#guess-game)
- [KTANE](https://github.com/BrimCap/BoredomBot#ktane)
  - [Setup](https://github.com/BrimCap/BoredomBot#setup)
  - [Button](https://github.com/BrimCap/BoredomBot#button)
  - [Wires](https://github.com/BrimCap/BoredomBot#wires)
  - [Reset](https://github.com/BrimCap/BoredomBot#reset)
- [Poof](https://github.com/BrimCap/BoredomBot#poof)
- [Rock Paper Scissors](https://github.com/BrimCap/BoredomBot#rps)
- [Test](https://github.com/BrimCap/BoredomBot#test)
- [Unpoof](https://github.com/BrimCap/BoredomBot#unpoof)

---
  
> **NOTE:** *In the usage section every argument between '<>' is optional and every argument between '[ ]' is necessary. Do not put '<>', or '[ ]' while doing the command itself.*

---
  
### ***COVID-19 CASES***

Usage: `!b corona <country>`

Could be slow. But it does return:

- [x] Confirmed Cases
- [x] Recoverd
- [x] Deaths
- [x] Closed Cases
- [x] Active Cases 

Does not return (might be added in the future):

- [ ] Graphs
- [ ] Percentages

---

### ***COUNTDOWN***

Usage: `!b cd [seconds]`

Countsdown from the number of seconds you entered into the `seconds` section.

---

### ***Guess Game***

Usage: `!b guess`

You guess a number between `1` and `10`, the computer also guesses a number between `1` and `10`. If both of yours match up, you win!

---

### ***KTANE***

Can defuse any button or wire in the game `Keep Talking and Nobody Explodes (KTANE)`. 

First you need to setup the bomb before you can move on to any modules.

### *SETUP*

Usage: `!b setup`

Sets up the bomb, the bot asks you some questions like the battries present, some lit indicators and the serial number. Once setup you can do other modules.

### *BUTTON*

Usage: `!b button [color] [text]`

Gives the correct output for the button.

### *WIRES*

Usage: `!b wire [*wires]`

Gives the correct output for the wires specified.

### *RESET*

Usage: `!b reset`

Resets the setup for aother bomb.

---

### ***POOF***

Usage: `!b poof [discord.Member]`

Kicks the specified `member`.

---

### ***RPS***

Usage: `!b rps [discord.Member]`

Play Rock Paper Scissors with the specified member.

---

### ***TEST***

Usage: `!b test`

Test to see if the bot is working!

---

### ***UNPOOF***

Usage: `!b unpoof [Member.name]`

> **Don't give the discm of the member just the name.**

Unbans the specified member from the guild.

---

## Known Issues

- There is no ban command.