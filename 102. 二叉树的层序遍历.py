# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # DFS
        self.result = []
        self.dfs(root, 0)
        # return self.result

        # BFS
        if not root:
            return []

        result = []
        queue = collections.deque()
        queue.append(root)

        # visited = set(root)

        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(current_level)

        return result

    def dfs(self, node, level):
        if not node:
            return
        if len(self.result) < level+1:
            self.result.append([])

        self.result[level].append(node.val)
        self.dfs(node.left, level+1)
        self.dfs(node.right, level+1)


