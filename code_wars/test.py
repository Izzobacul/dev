class Sudoku(object):
    def __init__(self, data):
        self.board = data
    def is_valid(self):
        v = True
        if len(self.board)!=len(self.board[0]):
            v = False
        for i in self.board:
            for n in range(1, len(self.board)):
                if i.count(n)>1:
                    v = False
        for i in range(0, len(self.board)):
            c = [x[y] for x in self.board for y in x if y==i]
            for n in c:
                if c.count(n)>1:
                    v = False
        return(v)

import math

hex

badSudoku1 = Sudoku([
  [0,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9]
])

badSudoku1.is_valid()