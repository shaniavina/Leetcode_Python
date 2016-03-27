# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        cur = head
        while cur:
            runner = cur.next
            while runner and runner.val == cur.val:
                runner = runner.next
                cur.next = runner
            cur = cur.next
        return head
                
