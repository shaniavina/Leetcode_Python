# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        pa = headA
        pb = headB

        while pa != pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next 
        ###switch the head, at the second traversal, they either meet or hit the end
        return pa
