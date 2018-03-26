# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        
        heap = []
        for l in lists:
            if l: ###discuss if it exists
                heapq.heappush(heap, (l.val, l))
        while heap:
            smallest = heapq.heappop(heap)[1]
            cur.next = smallest
            cur = cur.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))
        return dummy.next
