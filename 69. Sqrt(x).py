class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        left = 1
        right = x
        res = 1
        while left <= right:
            mid = (left + right) / 2
            if mid == x / mid:
                return mid
            elif mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1
                res = mid
        return res