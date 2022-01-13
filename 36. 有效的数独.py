class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board is None or len(board) == 0:
            return False

        rows = dict()
        cols = dict()
        r = len(board)
        c = len(board[0])
        blocks = [[dict() for _ in range(3)] for _ in range(3)]
        for i in range(r):
            for j in range(c):
                if board[i][j] != '.':
                    index = int(board[i][j]) - int('0')
                    rows.setdefault(i, dict()).setdefault(index, 0)
                    rows[i][index] += 1
                    cols.setdefault(j, dict()).setdefault(index, 0)
                    cols[j][index] += 1
                    blocks[i//3][j//3].setdefault(index, 0)
                    blocks[i//3][j//3][index] += 1
                    if rows[i][index] > 1 or cols[j][index] > 1 or blocks[i//3][j//3][index] > 1:
                        return False

        return True
