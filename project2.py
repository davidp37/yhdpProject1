
class mineSweeper:
  def __init__(self, height, length, bombs):

    self._height = height
    self._length = length
    self._bombs = bombs
    self._revealed = []
    self._board = self.createBoard()

  def generateBomb(self) -> list:
    # bombCoords stores the coordinates of bombs. 1 for bomb, 0 for no bomb
    bombCoords = [0] * _height
    for i in range(_height):
      bombCoords[i] = [0] * _length

    # Randomly generate bombs
    n = 0
    while n < bombs:
      x = random.randint(_height, _length)
      y = random.randint(_height, _length)
      if bombCoords[y][x] == 0:
        bombCoords[y][x] = 1
        n += 1

      return bombCoords

  def countBomb(self, bombCoords: [list]) -> list:
    newMap = [[0 for x in range(_width)] for x in range(_height)]
    # for height in _height:
    #   for width in _width:
    #     # if the coordinate has bomb
    #     if bombCoords[height][width] == 1:
    #       newMap[width][height] = -1    # -1 indicates a bomb
    #     # else the coordinate does not has bomb, count how many neighboring bombs the coordinate has.
    #     else:
    for height in _height:
      for width in _width:
        count = -bombCoords[i][j]  # count stores the number of neiboring bombs
        for x in [-1, 0, 1]:
          for y in [-1, 0, 1]:
            if 0 <= height + x < _height and 0 <= width + y < _width:
              count += bombCoords[height + x][width + y]
      newMap[height][width] = count


  def createBoard(self) -> list:
    # newMap = [0] * _height
    # for i in range(_height):
    #   newMap[i] = [0] * _length
    # newMap = [[0 for x in range(_width)] for x in range(_height)]
    bombCoords = self._generateBomb()
    newBoard = self._countBomb(bombCoords)
    return newBoard


  def play(self):
    self.select()
    self.choose()

  # calls the functions to decide the coordinate to be chosen then checks if that coordinate has already been chosen or not
  def select(self):
    revealed = True
    while revealed:
      x = self.chooseX()
      y = self.chooseY()
      if not self._revealed[ x -1][ y -1]:
        revealed = False
      else:
        print("You have already chosen that coordinate")
    self.check(x ,y)

  # Prompts the user to select a valid x coordinate, then returns that x coordinate
  def chooseX(self):
    xLoop = True
    while xLoop :
      x = int(input("Select an x coordinate: "))
      if x> self._length or x < 0:
                print("Invalid x")
      else:
        xLoop = False
      return x

    # Prompts the user to select a valid y coordinate, then returns that y coordinate
  def chooseY(self):
    yLoop = True
    while yLoop:
      y = int(input("Select a y coordinate: "))
      if y > self._height or y < 0:
        print("Invalid y")
      else:
        yLoop = False
    return y

    # Checks to see if the spot chosen is a bomb, returns nothing
  def check(self, x, y):
    if self._board[x][y] == "-1":
      self._lose()

  def printMap(self):
    top = ""
    row = ""
    for i in range(self._length):
      top += " " + i
    print(top)
    for j in range (self._height):
      row = ""
      for k in range(self._length):
        row += " "
        if self._revealed[j][k] == 1:
          row += self._board[j][k]
        elif self._revealed[j][k] == "F":
          row += "F"
        else:
          row += "-"
      print(row)



def start():
    height = int(input("Enter a height: "))
    length = int(input("Enter a length: "))
    bombs = int(input("Enter the number of bombs: "))
    game = mineSweeper(height, length, bombs)
    game.play()


start()