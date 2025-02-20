#! python3

"""
Create a function that asks the player for their choice
The function should return:
  rock     : 0
  paper    : 1
  scissors : 2

```
Sample Run:
Enter your choice:
rock

Output: 0
"""
import os
def playerChoice():
  answered = 0
  while answered == 0:
    print('Please make your choice of "Rock", "Paper", or "Scissors".')
    rpsp = input()
    if "rock" in rpsp or "Rock" in rpsp:
      print("You picked Rock.")
      pchoice = 0
      answered = 1
    elif "paper" in rpsp or "Paper" in rpsp:
      print("You picked Paper.")
      pchoice = 1
      answered = 1
    elif "scissors" in rpsp or "Scissors" in rpsp:
      print("You picked Scissors.")
      pchoice = 2
      answered = 1
    else:
      os.system('cls')
      print('You didn\'t select an option.')
  return pchoice


if __name__ == "__main__":
  player = playerChoice()
  print(player)
