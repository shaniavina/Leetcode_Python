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
        return self.sortedListToBSTRecu(head, length)
    def sortedListToBSTRecu(self, head, length):
        if length == 0:
            return None
        guard = ListNode(0)
        guard.next = head
        slow, quick = guard, head
        
        mid = length / 2
        for i in range(mid):
            slow = slow.next   ####step diff is 1; since there is one middle point
            quick = quick.next
        slow.next = None
        cur = TreeNode(quick.val)
        cur.left = self.sortedListToBSTRecu(head, mid)
        cur.right = self.sortedListToBSTRecu(quick.next, length - mid - 1)
        return cur
        
        
#         cur, length = head, 0
#         while cur:
#             cur, length = cur.next, length + 1
        
#         return self.sortedListToBSTRecu(0, length, head)[0]
#     def sortedListToBSTRecu(self, start, end, pointer):
#         if start == end:
#             return None, pointer
#         mid = (start + end) / 2
#         left, pointer = self.sortedListToBSTRecu(start, mid, pointer)
#         cur = TreeNode(pointer.val)
#         cur.left = left
#         pointer = pointer.next
#         cur.right, pointer = self.sortedListToBSTRecu(mid + 1, end, pointer)
#         return cur, pointer
    
    
