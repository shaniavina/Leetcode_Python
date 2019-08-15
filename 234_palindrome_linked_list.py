# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ## using stack
        stk = []
        slow, fast = head, head
        while fast and fast.next:
            stk.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next ### in case of adds
        while slow:
            val = stk.pop()
            if slow.val != val:
                return False
            slow = slow.next
        return True
        
