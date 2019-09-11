# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

### merge sort
## O(nklgk) O(1)
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) / 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge2Lists(left, right)
    def merge2Lists(self, list1, list2):
        dummy = ListNode(-1)
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next =list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return dummy.next
    
    
    
    
    
    ### priority queus (min heap)
    ### nk*lgk O(n)
        from heapq import heapify, heapreplace, heappop
        dummy = ListNode(0)
        cur = dummy
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next:
                heapreplace(h, (n.next.val, n.next))
            else:
                heappop(h)
            cur.next = n
            cur = cur.next
        return dummy.next
