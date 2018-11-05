"""
ICS 32A: 36600
Worked by David Javier Parra and Yoshitaka Hiramatsu

project2.py
"""
import random

class mineSweeper:
  def __init__(self, height: int, length: int, bombs: int):
    self._height = height
    self._length = length
    self._bombs = bombs
    self._board = self._createBoard()

    # [str] Stores the status of the game: "win", "lose", "in progress"
    self._status = "in progress"

    self._revealed = [[0 for x in range(self._length)] for x in range(self._height)]


  # Prints the board out in the desired form
  def print(self):
    print("  ", end = '')
    for x in range(self._length):
      print("%3d" % x, end = '')
    print()
    for y in range(self._height):
      print("%2d" % y, end = '')
      for x in range(self._length):
        if self._revealed[y][x] == True:
          cell = self._board[y][x]
          if type(cell) == int:
            print("%3d" % cell, end = '')
          elif cell == 'B':
            print("%3s" % cell, end = '')
        elif self._revealed[y][x] == "Flagged":
          print("  F", end = '')
        elif self._revealed[y][x] == False:
          print("  -", end = '')
      print()


  # Prints unselected bombs besides whatever selected
  # Only called when the player loses
  def _printBombs(self):
    if self._status == "lose":
      for y in range(self._height):
        for x in range(self._length):
          if self._board[y][x] == 'B':
            self._revealed[y][x] = True
      self.print()


  # checkValid – check if the coordinates are a valid coordinate on the board 
  # and that the state of that coordinate has not been revealed yet
  def checkValid(self, x = "", y = "")-> bool:
    # type of parameters of checkValid can be either string or integer
    if type(x) == type(y) == str:
      if not (x.isdigit() and y.isdigit()):
        print("Error: Enter integers for the coordinate.")
        return False
      x = int(x)
      y = int(y)

    if type(x) == type(y) == int:
      if 0 <= x < self._length and 0 <= y < self._height:
        if self._revealed[y][x] == False:
          return True
        elif self._revealed[y][x] == True:
          print("Error: The coordinate you entered has already been revealed.")
          return False
        elif self._revealed[y][x] == "Flagged":
          print("Error: The coordinate you entered is flagged.")
          return False
      else:
        print("Error: The coordinate you entered is out of the board.")
        return False
    else:
      print("Error: parameters must be either str or int (checkValid")


  # Creates board with information if each cell has a bomb or not.
  # 1 for bomb, 0 for non bomb
  def _generateBomb(self)-> list:
    bombCoords = [[0 for x in range(self._length)] for x in range(self._height)]

    # Randomly generate bombs
    n = 0
    while n < self._bombs:
      x = random.randint(0, self._length - 1)
      y = random.randint(0, self._height - 1)
      if bombCoords[y][x] == 0:
        bombCoords[y][x] = 1
        n += 1

    return bombCoords


  # Count the number of neiboring bombs for each cell
  # Mark as 'B' for the cell with a bomb
  def _countBomb(self, bombCoords: list)-> list:
    newMap = [[0 for x in range(self._length)] for x in range(self._height)]
    for y in range(self._height):
      for x in range(self._length):
        # if the cell is NOT a bomb
        if bombCoords[y][x] != 1:
          count = -bombCoords[y][x]   # count stores the number of neiboring bombs
          for s in [-1,0,1]:
            for t in [-1,0,1]:
              if 0 <= y + s < self._height and 0 <= x + t < self._length:
                count += bombCoords[y + s][x + t]
          newMap[y][x] = count
        # if the cell is a bomb
        else:
          newMap[y][x] = 'B'
    return newMap


  # Creates the board (2D list) for the game
  def _createBoard(self)-> list:
    bombCoords = self._generateBomb()
    newBoard = self._countBomb(bombCoords)
    return newBoard


  # Recreates the board by moving the bomb at (oldX, oldY) chosen in the first turn to new cell at (newX, newY)
  def _recreateBoard(self, oldX: int, oldY: int, newX: int, newY: int):
    oldBoard = [row[:] for row in self._board.copy()]
    bombCoords = [[0 for x in range(self._length)] for x in range(self._height)]

    # Move the bomb and recreate the board
    for y in range(self._height):
      for x in range(self._length):
        if x == newX and y == newY:
          bombCoords[newY][newX] = 1
        elif not (x == oldX and y == oldY):
          if oldBoard[y][x] == 'B':
            bombCoords[y][x] = 1
    self._board = self._countBomb(bombCoords)

    ### !!!Remove this line before submission
    print("_recreateBoard() -> ", end = '')
    self._getSolution()
    ### !!!


  # Choose the new coordinate (newX, newY) for the bomb in (x, y) to be moved to
  def _moveBomb(self, x: int, y: int):
    moved = False
    while not moved:
      valid = False
      while not valid:
        newX = random.randint(1, self._length - 1)
        newY = random.randint(1, self._height - 1)
        if self.checkValid(newX, newY):
          valid = True
      # Make sure (newX, newY) is not already Bomb
      if self._board[newY][newX] != 'B':
        self._recreateBoard(x, y, newX, newY)
        moved = True


  # Check if the win condition is met. If it is, this returns True.
  def _isWin(self):
    for y in range(self._height):
      for x in range(self._length):
        if self._board[y][x] != 'B' and self._revealed[y][x] != True:
          return False
    return True


  # Reveal all the neibors of a square with 0 neighboring bombs.
  # Takes the coordinate of such a square as a parameter
  def _revealAroundZero(self, x: int, y: int):
    # zeroCells stores the coordinates of cells of 0 as a list of lists of 2 elements, x and y
    zeroCells = [[x, y]]
    while len(zeroCells) > 0:
      currentX = zeroCells[0][0]
      currentY = zeroCells[0][1]
      zeroCells.pop(0)
      for s in [-1,0,1]:
        for t in [-1,0,1]:
          X = currentX + t
          Y = currentY + s
          if 0 <= Y < self._height and 0 <= X < self._length:
            if self._revealed[Y][X] == False and self._board[Y][X] == 0:
              self._revealed[Y][X] = True
              # self._revealAroundZero(x + t, y + s)
              zeroCells.append([X, Y])
            else:
              self._revealed[Y][X] = True


  # Takes the coordinate and returns a message if it is not a valid coordinate or if it is not blank. 
  # If it is, it will reveal the appropriate information for the square and its adjacent squares (according to the rules)
  def select(self):
    selected = False
    while not selected:
      x = input("Select an x coordinate: ")
      y = input("Select an y coordinate: ")
      if self.checkValid(x, y):
        x = int(x)
        y = int(y)
        selected = True

    # After a valid coodinate is selected
    self._revealed[y][x] = True

    # If you open a square with 0 neighboring bombs, all its neighbors will automatically open.
    if self._board[y][x] == 0:
      self._revealAroundZero(x, y)

    # Check lose condtion
    if self._board[y][x] == 'B':
      self._status = "lose"

    # Check win condtion
    if self._isWin():
      self._status = "win"


  # Takes the coordinate on the first turn
  # If it is a bomb, it will randomly select another position for the bomb and do everything in select.
  def selectFirst(self):
    selected = False
    while not selected:
      x = str(input("Select an x coordinate: "))
      y = str(input("Select an y coordinate: "))
      if self.checkValid(x, y):
        x = int(x)
        y = int(y)
        selected = True

    # After a valid coodinate is selected...
    self._revealed[y][x] = True

    # Check if the first select is Bomb. If so, move it randomly.
    if self._board[y][x] == 'B':
      self._moveBomb(x, y)

    # If you open a square with 0 neighboring bombs, all its neighbors will automatically open.
    if self._board[y][x] == 0:
      self._revealAroundZero(x, y)

    # Check win condtion
    if self._isWin():
      self._status = "win"


  # Returns the solution of the board for testing purposes only. 
  # This method will allow us to test your program, but you should not be calling/using it, other than for testing purposes.
  def _getSolution(self):
    print("!!!_getSolution: Make sure any call on this function must be deleted!!!")
    copy = self._revealed.copy()
    copy = [row[:] for row in self._revealed]
    status = self._status
    self._status = "lose"
    self._printBombs()
    self._revealed = [row[:] for row in copy]
    self._status = status
    print()


  # Check if the coordinate is valid and if the cell of that coordinate is "Flagged" or "not flagged"
  def _checkFlag(self, x = "", y = "")-> str:
      if not (x.isdigit() and y.isdigit()):
        print("Error: Enter an integer for the coordinate.")
        return False
      
      x = int(x)
      y = int(y)
      if 0 <= x < self._length and 0 <= y < self._height:
        if self._revealed[y][x] == "Flagged":
          return "Flagged"
        elif self._revealed[y][x] == False:
          return "not flagged"
        elif self._revealed[y][x] == True:
          print("Error: The coordinate you entered has already been revealed.")
          return ""
      else:
        print("Error: The coordinate you entered is out of the board.")
        return ""


  # flag – takes a coordinate to flag for a bomb. Should give an error message if the coordinate is not blank or if it is invalid. 
  def flag(self):
    x = input("Select an x coordinate: ")
    y = input("Select an y coordinate: ")
    if self._checkFlag(x, y) == "not flagged":
      x = int(x)
      y = int(y)
      self._revealed[y][x] = "Flagged"
    elif self._checkFlag(x, y) == "Flagged":
      print("Error: The coordinate you entered is already flagged.")


  # unflag - takes a coordinate to unflag a bomb. Should give an error message if the coordinate was not flagged or if it is an invalid coordinate. 
  def unflag(self):
    x = input("Select an x coordinate: ")
    y = input("Select an y coordinate: ")
    if self._checkFlag(x, y) == "Flagged":
      x = int(x)
      y = int(y)
      self._revealed[y][x] = False
    elif self._checkFlag(x, y) == "not flagged":
      print("Error: The coordinate you entered is not flagged yet.")


  # checkStatus – returns the status of the game: win, lose, in progress
  def checkStatus(self):
    return self._status


"""
END OF CLASS DEFINITION
========================
START OF DRIVER SCRIPT
You will be writing Driver script that will create a Minesweeper object every time a new game is started. This will be what “drives” the game. It should make the appropriate calls to the methods in Minesweeper depending on decisions made by the player. It should also keep track of how many games have been won or lost.
"""
"""
def start():
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
      if 0 < height < 101 and 0 < length < 101 and 0 < bombs < height * length:
        valid = True
      else:
        print("Invalid input: 0 < height < 101 and 0 < length < 101 and 0 < bombs < height * length - 1")
    else:
      print("Invalid input: Must be an integer")
  game = mineSweeper(height, length, bombs)

  ### Remove this line before submission
  print("start() -> ", end = '')
  game._getSolution()
  ### 

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

  if game.checkStatus() == "win":
    print("You Win!")
    win += 1
  elif game.checkStatus() == "lose":
    print("You Lose.")
    lose += 1
  playAgain = str(input("Do you want to play again (\"yes\" or \"no\")?:  "))
  print("Win: ", win, " Lose: ", lose)
"""



