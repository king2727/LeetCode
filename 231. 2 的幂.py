class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = 1
        while res < n:
            res *= 2
        if res == n:
            return True
        return False