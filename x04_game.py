#!python3

"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""

import x01_player as p
import x02_computer as c
import x03_winner as w


player = p.playerChoice()
computer = c.computerChoice() 
result = w.playerWins(computer, player)
if result == -1:
  print('You lost.')
elif result == 0:
  print('You tied.')
else:
  print('You won.')

if __name__ == "__main__":
  pass

