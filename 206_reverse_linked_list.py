# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         return self.doReverse(head, None)
#     def doReverse(self, head, newHead):
#         if head is None:
#             return newHead
#         next = head.next
#         head.next = newHead
#         return self.doReverse(next, head)
    
        cur, pre = head, None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
