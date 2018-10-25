





class mineSweeper:
  def __init__(self, height, length, bombs):
    
    self._height = height
    self._length = length
    self._bombs = bombs
    self._revealed = []
    self._map = self.createMap(height,length,bombs)


  def createMap(self,h,l,b):
    print("")

  def play(self):
    self.select()
    self.choose()

  def select(self):
    xLoop = True
    while(xLoop):
      x = input("Select an x coordinate: ")
      if (x>length or x<0) and  :
        xLoop = True
      else:
        print("Invalid X")





def start():
  height = input("Enter a height: ")
  length = input("Enter a length: ")
  bombs = input("Enter the number of bombs: ")
  game = mineSweeper(height,length,bombs)
  game.play()
