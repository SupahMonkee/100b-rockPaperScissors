#!python3
"""
Create a function that creates a random choice for the computer player:
input parameters: none required
output:

0 : rock
1 : paper
2 : scissors
"""
import random
def computerChoice():
  cchoice = random.randrange(0,3)
  return cchoice


if __name__ == "__main__":
  computer = computerChoice()
  print(computer)
