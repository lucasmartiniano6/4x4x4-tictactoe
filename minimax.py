import grid
import numpy as np

state = grid.Grid([np.zeros((4,4)) for _ in range(4)])

def valution(pos):
  # pos -> [plane, line, column]  
  pass

MAX_VAL = 10000
def minimax(pos, depth, a, b, maximizing):
  if depth <= 0:
    return valution(pos)
  
  if maximizing:
    value = -MAX_VAL
    for plane in range(4):
      for line in range(4):
        for col in range(4):
          if plane==pos[0] and line==pos[1] and col==pos[2]:
            continue
          e_val = minimax(state[plane, line, col], depth-1, a, b, False)
          max_eval = max(max_eval, e_val)
          a = max(a, e_val)
          if b <= a:
            break
    return MAX_VAL
  else:
    value = + MAX_VAL
    for i in range(pos[1]-1, pos[1]+1):
      for j in range(pos[2]-1, pos[2]+1):
        if i==pos[1] and j==pos[2]:
          continue
        e_val = minimax(state[plane,line,col], depth-1,a,b,True)
        min_eval = min(min_eval, e_val)
        b = min(b, e_val)
        if b <= a:
          break
        return min_eval

if __name__ == '__main__':
  minimax(state[0,0,0], 2, 0, 0, True)
