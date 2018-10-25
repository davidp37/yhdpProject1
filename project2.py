





class mineSweeper:
  def __init__(self, height, length, bombs):
    createMap(height,length,bombs)


  def createMap(self,h,l,b):
    print("")

  def play(self):
    print("")




def start():
  height = input("Enter a height: ")
  length = input("Enter a length: ")
  bombs = input("Enter the number of bombs: ")
  game = mineSweeper(height,length,bombs)
  game.play()