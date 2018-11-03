import random





class mineSweeper:
  def __init__(self, height, length, bombs):
    self._height = height
    self._length = length
    self._bombs = bombs
    self._board = self._createBoard()
    self._win = 0
    self._loss = 0
    self._inprogress = True

    # _revealed stores True for revealed cell, False for unrevealed cell, or "Flagged" for a flagged cell
    self._revealed = [0] * self._height
    for i in range(self._height):
      self._revealed[i] = [0] * self._length


  # Prints the board out in the desired form
  def print(self):
    top = ""
    row = ""
    for i in range(self._length):
      top += " " + i
    print(top)
    for j in range (self._height):
      row = ""
      for k in range(self._length):
        row += " "
        if self._revealed[j][k]:
          row += self._board[j][k]
        elif self._revealed[j][k] == "Flagged":
          row += "F"
        else:
          row += "-"
      print(row)


  # checkValid – check if the coordinates are a valid coordinate on the board 
  # and that the state of that coordinate has not been revealed yet
  def checkValid(self, x, y)-> bool:
      if not (x.isdigit() or y.isdigit()):
        print("Error: Enter an integer for the coordinate.")
        return False
      
      x = int(x)
      y = int(y)
      if 0 <= x <= self._length and 0 <= y <= self._height:
        if self._revealed[y][x] != "Flagged":
          if not self._revealed[y][x]:
            return True
          else:
            print("Error: The coordinate you entered has already been revealed.")
            return False
        else:
          print("Error: The coordinate you entered is flagged.")
          return False
      else:
        print("Error: The coordinate you entered is out of the board.")
        return False


  # Creates board with information if each cell has a bomb or not.
  # 1 for bomb, 0 for non bomb
  def _generateBomb(self)-> list:
    # bombCoords represents the board and stores 1 for cell with bomb, 0 for a cell with non bomb
    bombCoords = [0] * self._height
    for i in range(self._height):
      bombCoords[i] = [0] * self._length

    # The number of bombs should not exceed (number of squares - 1)
    if self._bombs <= (self._height * self._length - 1):
      bombs = self._bombs
    else:
      bombs = self._height * self._length - 1

    # Randomly generate bombs
    n = 0
    while n < bombs:
      x = random.randint(self._height, self._length - 1)
      y = random.randint(self._height, self._length - 1)
      if bombCoords[y][x] == 0:
        bombCoords[y][x] = 1
        n += 1

    return bombCoords


  # Count the number of neiboring bombs for each cell
  # Mark as 'B' for the cell with a bomb
  def _countBomb(self, bombCoords: [list])-> list:
    newMap = [[0 for x in range(self._length)] for x in range(self._height)]
    for height in self._height:
      for width in self._length:
        # if the cell is NOT a bomb
        if bombCoords[height][width] != 1:
          count = -bombCoords[i][j]   # count stores the number of neiboring bombs
          for x in [-1,0,1]:
            for y in [-1,0,1]:
              if 0 <= height + x < self._height and 0 <= width + y < self._length:
                count += bombCoords[height + x][width + y]
          newMap[height][width] = count
        # if the cell is a bomb
        else:
          newMap[height][width] = 'B'
    return newMap


  # Creates the board (2D list) for the game
  def _createBoard(self)-> list:
    bombCoords = self._generateBomb()
    newBoard = self._countBomb(bombCoords)
    return newBoard


  # Recreates the board by moving the bomb at (oldX, oldY) chosen in the first turn to new cell at (newX, newY)
  def _recreateBoard(self, oldX, oldY, newX, newY):
    oldBoard = self._board.copy()

    # bombCoords represents the board and stores 1 for cell with bomb, 0 for a cell with non bomb
    bombCoords = [0] * self._height
    for i in range(self._height):
      bombCoords[i] = [0] * self._length

    # Move the bomb and recreate the board
    for y in range(self._height):
      for x in range(self._length):
        if x == newX and y == newY:
          bombCoords[newY][newX] = 1
        elif x != oldX and y != oldY:
          if oldBoard[y][x] == 'B':
            bombCoords[y][x] = 1

    self._board = self._countBomb(bombCoords)


  # Moves the bomb in (x, y) to (newX, newY)
  def _moveBomb(self, x, y):
    moved = False
    while not moved:
      newX = random.randint(1, self._length - 1)
      newY = random.randint(1, self._height - 1)
      while not checkValid(newX, newY):
        newX = random.randint(1, self._length - 1)
        newY = random.randint(1, self._height - 1)
      if self._board[newY][newX] != 'B'
        self._recreateBoard(newX, newY)
        moved = True



  # Checks to see if the spot chosen is a bomb, returns nothing
  # (x, y) is supposed to be verified beforehand, in select().
  def _checkBomb(self, x, y,first = False):
    self._revealed[y][x] = True
    if self._board[y][x] == 'B'
      if first:
        self._moveBomb(x,y)
      else:
        self._lose()
    else:
      self.select(False)


  # Takes the coordinate and returns a message if it is not a valid coordinate or if it is not blank. 
  # If it is, it will reveal the appropriate information for the square and its adjacent squares (according to the rules)
  def select(self, first):
    selected = False
    while not selected:
      x = print("Select an x coordinate: ")
      y = print("Select an y coordinate: ")

      if self.checkValid(x, y):
        selected = True

    # After a valid coodinate is selected...
    self._revealed[y][x] = True

  # Takes the coordinate on the first turn
  # If it is a bomb, it will randomly select another position for the bomb and do everything in select.
  def selectFirst(self):
    self.select(True)


  #  returns the solution of the board for testing purposes only. This method will allow us to test your program, but you should not be calling/using it, other than for testing purposes.
  def _getSolution(self):
    for y in self._board:
      for x in self._board[y]:
        print(self._board[x][y], end = '')

  # flag – takes a coordinate to flag for a bomb. Should give an error message if the coordinate is not blank or if it is invalid. 
  def flag(self, x, y):
    if self._checkValid4Flag(x, y):
      self._revealed = "Flagged"


  # unflag - takes a coordinate to unflag a bomb. Should give an error message if the coordinate was not flagged or if it is an invalid coordinate. 
  def unflag(self, x, y):
    if self._checkValid4Unflag(x, y):
      self._revealed = False


  # checkStatus – returns the status of the game: win, lose, in progress
  def checkStatus(self):
    print("Win: ", self._win, " Lose: ", self._lose)



"""
END OF CLASS DEFINITION
========================
START OF MAIN
"""
def start():
    height = int(input("Enter a height: "))
    length = int(input("Enter a length: "))
    bombs = int(input("Enter the number of bombs: "))
    game = mineSweeper(height, length, bombs)
    game.selectFirst()


start()

