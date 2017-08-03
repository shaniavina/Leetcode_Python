from heapq import heappush, heappop
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # Balance smaller half and larger half. min_heap has the minimum on top, max_heap has the opposite no of element on top
        if not self.max_heap or num > -self.max_heap[0]:
            heappush(self.min_heap, num)
            if len(self.min_heap) > len(self.max_heap) + 1:
                heappush(self.max_heap, -heappop(self.min_heap))
        else:
            heappush(self.max_heap, -num)
            if len(self.max_heap) > len(self.min_heap):
                heappush(self.min_heap, -heappop(self.max_heap))



    def findMedian(self):
        """
        :rtype: float
        """
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0 if len(self.max_heap) == len(self.min_heap) else self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
