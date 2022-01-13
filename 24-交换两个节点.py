# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
# 你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
