class Solution(object):
    def count1(self, num):
        count = 0
        while num:
            count += 1
            num = num & (num-1)
        return count

    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n+1):
            result.append(self.count1(i))
        return result