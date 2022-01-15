class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        n = len(triangle[-1])

        res = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            res[m-1][i] = triangle[m-1][i]

        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])):
                res[i][j] = triangle[i][j] + min(res[i+1][j], res[i+1][j+1])

        return res[0][0]
