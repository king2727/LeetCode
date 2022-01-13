class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self.gen(0, 0, n, "")
        return self.list

    def gen(self, left, right, n, result):
        if left == n and right == n:
            self.list.append(result)
            return

        if left < n:
            self.gen(left+1, right, n, result+'(')

        if left > right and right < n:
            self.gen(left, right+1, n, result+')')