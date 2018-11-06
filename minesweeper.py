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

    # Stores the status of the game: "win", "lose", "in progress"
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


  # Prints unselected bombs besides whatever selected so far
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
        return False
      x = int(x)
      y = int(y)

    if type(x) == type(y) == int:
      if 0 <= x < self._length and 0 <= y < self._height:
        if self._revealed[y][x] == False:
          return True
    return False

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
        # if the cell is aleady a bomb, leave it
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


  # Choose the new coordinate (newX, newY) for the bomb in (x, y) to be moved to
  def _moveBomb(self, x: int, y: int):
    moved = False
    while not moved:
      valid = False
      while not valid:
        newX = random.randint(0, self._length - 1)
        newY = random.randint(0, self._height - 1)
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
              zeroCells.append([X, Y])
            else:
              self._revealed[Y][X] = True


  # Takes the coordinate and returns a message if it is not a valid coordinate or if it is not blank. 
  # If it is, it will reveal the appropriate information for the square and its adjacent squares (according to the rules)
  def select(self, isSelectedFirst = False):
    selected = False
    while not selected:
      x = input("Select an x coordinate: ")
      y = input("Select an y coordinate: ")
      if self.checkValid(x, y):
        x = int(x)
        y = int(y)
        selected = True
      else:
        print("Invalid input")

    # After a valid coodinate is selected
    self._revealed[y][x] = True

    # Check lose condtion
    if self._board[y][x] == 'B':
      if isSelectedFirst:
        self._moveBomb(x, y)
      else:
        self._status = "lose"

    # If you open a square with 0 neighboring bombs, all its neighbors will automatically open.
    if self._board[y][x] == 0:
      self._revealAroundZero(x, y)

    # Check win condtion
    if self._isWin():
      self._status = "win"


  # Takes the coordinate on the first turn
  # If it is a bomb, it will randomly select another position for the bomb and do everything in select.
  def selectFirst(self):
    self.select(True)


  # Returns the solution of the board for testing purposes only. 
  # This method will allow us to test your program, but you should not be calling/using it, other than for testing purposes.
  def _getSolution(self)-> list:
    return self._board


  # Check if the coordinate is valid and if the cell of that coordinate is "Flagged" or "not flagged"
  # Returns empty string when the coordinate is invalid
  def _checkFlag(self, x = "", y = "")-> str:
      if not (x.isdigit() and y.isdigit()):
        return ""
      
      x = int(x)
      y = int(y)
      if 0 <= x < self._length and 0 <= y < self._height:
        if self._revealed[y][x] == "Flagged":
          return "Flagged"
        elif self._revealed[y][x] == False:
          return "not flagged"
        elif self._revealed[y][x] == True:
          return ""
      else:
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
      print("Invalid Input: The coordinate you entered is already flagged.")
    else:
      print("Invalid Input")


  # unflag - takes a coordinate to unflag a bomb. Should give an error message if the coordinate was not flagged or if it is an invalid coordinate. 
  def unflag(self):
    x = input("Select an x coordinate: ")
    y = input("Select an y coordinate: ")
    if self._checkFlag(x, y) == "Flagged":
      x = int(x)
      y = int(y)
      self._revealed[y][x] = False
    elif self._checkFlag(x, y) == "not flagged":
      print("Invalid Input: The coordinate you entered is not flagged yet.")
    else:
      print("Invalid Input")


  # checkStatus – returns the status of the game: win, lose, in progress
  def checkStatus(self):
    return self._status

