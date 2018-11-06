"""
ICS 32A: 36600
Worked by David Javier Parra and Yoshitaka Hiramatsu

Driver Script for Project 2:
You will be writing Driver script that will create a Minesweeper object every time a new game is started. This will be what “drives” the game. It should make the appropriate calls to the methods in Minesweeper depending on decisions made by the player. It should also keep track of how many games have been won or lost.
"""
from project2 import mineSweeper

def start()-> mineSweeper:
  valid = False
  while not valid:
    height = input("Enter a height: ")
    length = input("Enter a length: ")
    bombs = input("Enter the number of bombs: ")
    if height.isdigit() and length.isdigit() and bombs.isdigit():
      height = int(height)
      length = int(length)
      bombs = int(bombs)
      # The number of bombs should not exceed (number of squares - 1)
      if 0 < height < 101 and 0 < length < 101 and 0 <= bombs < height * length:
        valid = True
      else:
        print("Invalid input: 0 < height < 101 and 0 < length < 101 and 0 <= bombs < height * length - 1")
    else:
      print("Invalid input: Must be an positive integer")
  game = mineSweeper(height, length, bombs)
  game.print()
  game.selectFirst()
  game.print()
  return game


win = 0
lose = 0
playAgain = "yes"
while playAgain == "yes" or playAgain == "Yes":
  game = start()
  while game.checkStatus() == "in progress":
    command = str(input("\"select\" or \"flag\" or \"unflag\"?: "))
    if command == "select":
      game.select()
    elif command == "flag":
      game.flag()
    elif command == "unflag":
      game.unflag()
    else:
      print("Invalid input.")
    game.print()

  # After the game ends, check if the player wins or loses
  if game.checkStatus() == "win":
    print("You Win!")
    win += 1
  elif game.checkStatus() == "lose":
    print("Bomb! You lose.")
    game._printBombs()
    lose += 1
  askAgain = True
  while askAgain:
    playAgain = str(input("Do you want to play again (\"yes\" or \"no\")?: "))
    if playAgain == "yes" or playAgain == "Yes" or playAgain == "no" or playAgain == "No":
      askAgain = False
  print("Win: ", win, " Lose: ", lose)




