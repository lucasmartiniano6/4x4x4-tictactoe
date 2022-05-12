import numpy as np

class Grid:
  def __init__(self, boards):
    self.grid = np.stack((boards))
  def __repr__(self):
    for board in self.grid:
      for line in board:
        for el in line:
          print(el, '|', end='')
        print('\n')
      print('*'*35)
    return ' '
  def checkPlane(self, n):
    for line in range(4):
      if self.grid[n, line, 0] == 0:
        continue
      if self.grid[n, line, 0] ==  self.grid[n, line, 1] == self.grid[n, line, 2] ==self.grid[n, line, 3]:
        return True

    for col in range(4):
      if self.grid[n, 0, col]== 0:
        continue
      if self.grid[n, 0, col] == self.grid[n, 1, col] == self.grid[n, 2, col] == self.grid[n, 3, col]:
        return True
    return False

  def interPlane(self):
    # all-down
    for i in range(4):
      for j in range(4):
        if self.grid[0, i, j] == self.grid[1, i, j] ==  self.grid[2, i, j] ==  self.grid[3, i, j]: 
          if self.grid[0,i,j] != 0:
            print('All down on', i, j)
            return True 
    #diagonal
    if self.grid[0,0,0] == self.grid[1, 1,1] == self.grid[2,2,2] == self.grid[3,3,3]:
      if self.grid[0,0,0] != 0:
        print('Diagonal')
        return True
    if self.grid[0,3,0] == self.grid[1,2,1] == self.grid[2,1,2] == self.grid[3,0,3]:
      if self.grid[0,3,0] != 0:
        print('Diagonal')
        return True
    return False

  def winner(self):
    for n in range(4):
      if self.checkPlane(n):
        print(f'Plane {n} wins')
        return True
    return self.interPlane()
      
grid = Grid([np.zeros((4,4)) for _ in range(4)])

player = 1
while True:
  print(grid)
  board_number = int(input('board:'))
  x_board = int(input('x_board:'))
  y_board = int(input('y_board:'))
  grid.grid[board_number, x_board, y_board] = player

  if grid.winner():
    print(f'player {player} wins')
    break
  player *= -1
