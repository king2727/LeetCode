class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])

        for i in range(r):
            for j in range(c):
                if board[i][j] == '.':
                    for x in range(1, 10):
                        if self.isValid(board, i, j, str(x)):
                            board[i][j] = str(x)
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def isValid(self, board, i, j, num):
        for x in range(9):
            if board[i][x] == num or board[x][j] == num or board[3*(i//3)+x//3][3*(j//3)+x%3] == num:
                return False
        return True
