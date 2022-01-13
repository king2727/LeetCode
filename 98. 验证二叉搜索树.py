# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     inorder = self.inorder(root)
    #     return inorder == list(sorted(set(inorder)))
    #
    # def inorder(self, root):
    #     if root is None:
    #         return []
    #     return self.inorder(root.left) + [self.val] + self.inorder(root.right)
    def isValidBST(self, root):
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)
