class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0, 1, 2]

        if n <= 2:
            return arr[n]

        for i in range(3, n+1):
            s = arr[i-1] + arr[i-2]
            arr.append(s)
        return arr[n]