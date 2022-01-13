class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        ans = []

        for first in range(n):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            third = n - 1
            target = -nums[first]
            for second in range(first+1, n):
                if second > first + 1 and nums[second] == nums[second-1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[first] + nums[second] + nums[third] == 0:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans

    def threeSum2(self, nums):
        if len(nums) < 3:
            return
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)
