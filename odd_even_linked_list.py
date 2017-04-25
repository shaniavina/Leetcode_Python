# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
            
        p = head
        q = head
        guard = ListNode(-1)
        tail = guard
        while p and p.next:
            tail.next = p.next
            tail = tail.next
            
            p.next = p.next.next
            p = p.next
            
            if p:
                q = p
        tail.next = None
        q.next = guard.next
        return head

    ###fabulous
