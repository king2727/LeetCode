class Solution(object):
    def __init__(self):
        self.cols = set()
        self.pies = set()
        self.nas = set()
        self.result = []

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        self.DFS(n, 0, [])

        return len(self.result)

    def DFS(self, n, row, state):
        if row >= n:
            self.result.append(state)
            return

        for col in range(n):
            if col in self.cols or row+col in self.pies or row-col in self.nas:
                continue

            self.cols.add(col)
            self.pies.add(row+col)
            self.nas.add(row-col)

            self.DFS(n, row+1, state+[col])

            self.cols.remove(col)
            self.pies.remove(row+col)
            self.nas.remove(row-col)