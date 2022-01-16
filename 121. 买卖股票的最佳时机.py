class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxf = 0
        minf = 1e9

        for price in prices:
            maxf = max(price-minf, maxf)
            minf = min(price, minf)

        return maxf