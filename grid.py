import numpy as np
from board import Board

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

grid = Grid([Board().board for _ in range(4)])
print(grid)
