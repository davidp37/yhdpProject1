import random





class mineSweeper:
  def __init__(self, height, length, bombs):
    self._height = height
    self._length = length
    self._bombs = bombs
    self._revealed = []
    self._board = self.createBoard(height,length,bombs)

  def generateBomb(self)-> list:
    # bombCoords stores the coordinates of bombs. 1 for bomb, 0 for no bomb
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
      x = random.randint(self._height, self._length)
      y = random.randint(self._height, self._length)
      if bombCoords[y][x] == 0:
        bombCoords[y][x] = 1
        n += 1

      return bombCoords

  def countBomb(self, bombCoords: [list])-> list:
    newMap = [[0 for x in range(self._length)] for x in range(self._height)]
    for height in self._height:
      for width in self._length:
        count = -bombCoords[i][j]   # count stores the number of neiboring bombs
          for x in [-1,0,1]:
            for y in [-1,0,1]:
              if 0 <= height + x < self._height and 0 <= width + y < self._length:
                count += bombCoords[height + x][width + y]
        newMap[height][width] = count

  def createBoard(self)-> list:
    bombCoords = generateBomb()
    newBoard = countBomb(bombCoords)
    return newBoard

  def play(self):
    self.select()
    self.choose()

  def select(self):
    revealed = True
    while(revealed):
      x = self.chooseX()
      y = self.chooseY()
      if not self._revealed[x-1][y-1]:
        revealed = False
      else:
        print("You have already chosen that coordinate")
    self.check(x,y)
      
  def chooseX(self):
    xLoop = True
    while(xLoop):
      x = input("Select an x coordinate: ")
      if x>self._length or x<0:
        print("Invalid x")
      else:
        yloop = False
    return x
      
  def chooseY(self):
    yLoop = True
    while(yLoop):
      y = input("Select a y coordinate: ")
      if y>self._height or y<0:
        print("Invalid y")
      else:
        yLoop = False
    return y

  def check(self,x,y):
    if self._board[x][y] == "-1":
      self._lose()



def start():
  height = input("Enter a height: ")
  length = input("Enter a length: ")
  bombs = input("Enter the number of bombs: ")
  game = mineSweeper(height,length,bombs)
  game.play()

start()
