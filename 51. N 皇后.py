class Solution(object):
    def __init__(self):
        self.result = []
        self.cols = set()
        self.pies = set()
        self.nas = set()

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1:
            return []

        self.DFS(n, 0, [])

        return self.result

    def DFS(self, n, row, state):
        if row >= n:
            s = []
            for i in state:
                arr = ['.'] * n
                arr[i] = 'Q'

                arr = ''.join(arr)
                s.append(arr)
            self.result.append(s)
            return

        for col in range(n):
            if col in self.cols or row + col in self.pies or row - col in self.nas:
                continue

            self.cols.add(col)
            self.pies.add(row+col)
            self.nas.add(row-col)

            self.DFS(n, row+1, state+[col])

            self.cols.remove(col)
            self.pies.remove(row+col)
            self.nas.remove(row-col)




