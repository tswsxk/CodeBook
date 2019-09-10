class Solution(object):
  def solveSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    rowChecker = [set() for y in range(0, 9)]
    colChecker = [set() for y in range(0, 9)]
    subboxChecker = [set() for y in range(0, 9)]
    nums = set(range(1, 10))
    check = []

    for i, row in enumerate(board):
      for j, c in enumerate(row):
        if c != ".":
          subboxRow = i // 3
          subboxCol = j // 3
          rowChecker[i].add(int(c))
          colChecker[j].add(int(c))
          subboxChecker[subboxRow * 3 + subboxCol].add(int(c))
        else:
          check.append((i, j))

    def putNums(checklist):
      if not checklist:
        return True
      row, col = checklist[0]
      subboxRow = row // 3
      subboxCol = col // 3
      candidate = nums - (rowChecker[row] | colChecker[col] | subboxChecker[subboxRow * 3 + subboxCol])
      if candidate:
        for num in candidate:
          board[row][col] = str(num)
          rowChecker[row].add(num)
          colChecker[col].add(num)
          subboxChecker[subboxRow * 3 + subboxCol].add(num)
          if putNums(checklist[1:]):
            return True
          rowChecker[row].remove(num)
          colChecker[col].remove(num)
          subboxChecker[subboxRow * 3 + subboxCol].remove(num)
        return False
      else:
        return False
    putNums(check)


if __name__ == "__main__":
  sol = Solution()
  sol.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])