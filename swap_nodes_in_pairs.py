# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode('-inf')
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            next_one, next_two, next_three = cur.next, cur.next.next, cur.next.next.next
            cur.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            cur = next_one
        return dummy.next
