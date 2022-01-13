class Solution(object):
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        mark = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    mark[i][j] = 1
                    if self.DFS(i, j, mark, board, word[1:]) == True:
                        return True
                    mark[i][j] = 0

        return False

    def DFS(self, i, j, mark, board, word):
        if len(word) == 0:
            return True

        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]
            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and \
                mark[cur_i][cur_j] == 0 and board[cur_i][cur_j] == word[0]:

                mark[cur_i][cur_j] = 1
                if self.DFS(cur_i, cur_j, mark, board, word[1:]) == True:
                    return True
                mark[cur_i][cur_j] = 0

        return False

