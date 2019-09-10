class Solution(object):
  def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    def reset_checkArray():
      return [0 for x in range(0, 11)]

    # row check
    for row in board:
      checkArray = reset_checkArray()
      for c in row:
        if c != ".":
          if checkArray[int(c)] >= 1:
            return False
          else:
            checkArray[int(c)] += 1

    #col check
    for col in  range(0, 9):
      checkArray = reset_checkArray()
      for row in board:
        c = row[col]
        if c != ".":
          if checkArray[int(c)] >= 1:
            return False
          else:
            checkArray[int(c)] += 1

    #subbox check
    for boxrow in range(0, 3):
      for boxcol in range(0, 3):
        checkArray = reset_checkArray()
        for row in range(boxrow * 3, boxrow * 3 + 3):
          for col in range(boxcol * 3, boxcol * 3 + 3):
            c = board[row][col]
            if c != ".":
              if checkArray[int(c)] >= 1:
                return False
              else:
                checkArray[int(c)] += 1

    return True

if __name__ == "__main__":
  sol = Solution()
  sol.isValidSudoku(["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"])