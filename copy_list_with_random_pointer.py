# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # Time:  O(n)  # Space: O(1)  通过两个链表的next指针把nodes连接起来（左二图），从而我们可以正确地复制random pointer（通过右二图中蓝色link)。最后我们可以通过修改next指针分离两个链表。这个实现虽然省空间，但是因为修改了输入，线程安全性不好
        # copy and combine copied list with original list
        current = head
        while current:
            copied = RandomListNode(current.label)
            copied.next = current.next
            current.next = copied
            current = copied.next
        
        # update random node in copied list
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # split copied list from combined one
        dummy = RandomListNode(0)
        copied_current, current = dummy, head
        while current:
            copied_current.next = current.next
            current.next = current.next.next
            copied_current, current = copied_current.next, current.next
        return dummy.next

        
        
        
        
#         # Time:  O(n), # Space: O(n): hashing wish hashmap 第一轮复制nodes并建立一个从输入到复制的映射，第二轮把link复制下来。
#         dummy = RandomListNode(0)
#         cur, pre, copies = head, dummy, {}
#         while cur:
#             copied = RandomListNode(cur.label)
#             copies[cur] = copied
#             pre.next = copied
#             pre, cur = pre.next, cur.next
        
#         cur = head
#         while cur:
#             if cur.random:
#                 copies[cur].random = copies[cur.random]
#             cur = cur.next
            
#         return dummy.next
