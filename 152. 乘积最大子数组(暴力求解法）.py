class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        res = [[nums[i] if i==j else 0 for i in range(length)] for j in range(length)]
        maxres = max(nums)
        for i in range(length):
            for j in range(i+1, length):
                res[i][j] = res[i][j-1] * nums[j]
                if res[i][j] > maxres:
                    maxres = res[i][j]

        return maxres


