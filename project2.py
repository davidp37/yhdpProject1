import random





class mineSweeper:
  def __init__(self, height, length, bombs):
    createMap(height,length,bombs)


  def generateBomb(self)-> list:
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

  def countBomb(self, bombCoords: [list])-> list:
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
        count = -bombCoords[i][j]   # count stores the number of neiboring bombs
          for x in [-1,0,1]:
            for y in [-1,0,1]:
              if 0 <= height + x < _height and 0 <= width + y < _width:
                count += bombCoords[height + x][width + y]
        newMap[height][width] = count



  def createBoard(self)-> list:
    # newMap = [0] * _height
    # for i in range(_height):
    #   newMap[i] = [0] * _length
    # newMap = [[0 for x in range(_width)] for x in range(_height)]
    bombCoords = generateBomb()
    newBoard = countBomb(bombCoords)
    return newBoard







  def play(self):
    print("")




def start():
  height = input("Enter a height: ")
  length = input("Enter a length: ")
  bombs = input("Enter the number of bombs: ")
  game = mineSweeper(height,length,bombs)
  game.play()

start()