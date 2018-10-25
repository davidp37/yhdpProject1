





class mineSweeper:
  def __init__(self, height, length, bombs):
    
    self._height = height
    self._length = length
    self._bombs = bombs
    self._revealed = []
    self._board = self.createBoard(height,length,bombs)


  def createBoard(self,h,l,b):
    print("")

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
    if self._board[x][y] == "B":
      self._lose()



def start():
  height = input("Enter a height: ")
  length = input("Enter a length: ")
  bombs = input("Enter the number of bombs: ")
  game = mineSweeper(height,length,bombs)
  game.play()
