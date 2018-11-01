
class mineSweeper:
  def __init__(self, height, length, bombs):

    self._height = height
    self._length = length
    self._bombs = bombs
    self._revealed = []
    self._board = self.createBoard(height ,length ,bombs)


  def createBoard(self ,h ,l ,b):
    print("")

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


def start():
    height = int(input("Enter a height: "))
    length = int(input("Enter a length: "))
    bombs = int(input("Enter the number of bombs: "))
    game = mineSweeper(height, length, bombs)
    game.play()


start()