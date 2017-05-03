# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        cur, length = head, 0
        while cur:
            cur, length = cur.next, length + 1
        self.head = head
        return self.sortedListToBSTRecu(0, length)
    def sortedListToBSTRecu(self, start, end):
        if start == end:
            return None
        mid = (start + end) / 2
        left = self.sortedListToBSTRecu(start, mid)
        cur = TreeNode(self.head.val)
        cur.left = left
        self.head = self.head.next
        cur.right = self.sortedListToBSTRecu(mid + 1, end)
        return cur
