import numpy as np

class Board:
  def __init__(self):
    self.board = np.zeros((4,4))
  def mark(self, x, y, marker):
    self.board[x, y] = marker
