# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next:  #####fast always comes before fast.next
            fast, slow = fast.next.next, slow.next   ####one step, two step; finally meet
            if fast == slow:
                return True
        return False
