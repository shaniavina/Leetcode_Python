# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def move(self, head, steps):
        node = head
        for i in range(steps):
            node = node.next
        return node
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        tailA = headA
        countA = 1
        while tailA.next != None:
            tailA = tailA.next
            countA += 1
        
        tailB = headB
        countB = 1
        while tailB.next != None:
            tailB = tailB.next
            countB += 1
            
        if tailA != tailB:
            return None
        else:
            diff = abs(countA - countB)
            curA = headA
            curB = headB
            if countA > countB:
                curA = self.move(headA, diff)
            else:
                curB = self.move(headB, diff)
            while curA != curB:
                curA = curA.next
                curB = curB.next
        return curA
